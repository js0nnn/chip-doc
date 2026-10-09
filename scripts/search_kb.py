import sys
import pickle
from pathlib import Path

import faiss
from sentence_transformers import SentenceTransformer


# ============================================================
# CONFIG
# ============================================================

KB_DIR = Path("../dataset/kb")

INDEX_FILE = KB_DIR / "index.faiss"
METADATA_FILE = KB_DIR / "metadata.pkl"

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

DEFAULT_TOP_K = 5

# Maximum amount of retrieved text to display per result
MAX_TEXT_CHARS = 2500


# ============================================================
# LOAD KNOWLEDGE BASE
# ============================================================

def load_kb():

    print("=" * 70)
    print("LOADING KNOWLEDGE BASE")
    print("=" * 70)

    print(f"FAISS index : {INDEX_FILE}")
    print(f"Metadata    : {METADATA_FILE}")

    # --------------------------------------------------------
    # Load FAISS
    # --------------------------------------------------------

    index = faiss.read_index(str(INDEX_FILE))

    # --------------------------------------------------------
    # Load metadata
    # --------------------------------------------------------

    with open(METADATA_FILE, "rb") as f:
        raw_metadata = pickle.load(f)

    # --------------------------------------------------------
    # Extract chunk metadata
    #
    # build_kb.py stores more than just the chunk list.
    # Therefore raw_metadata may be a dictionary containing
    # the actual chunks under "data" or "chunks".
    # --------------------------------------------------------

    metadata = extract_chunk_metadata(raw_metadata)

    print()
    print(f"Vectors     : {index.ntotal}")
    print(f"Dimension   : {index.d}")
    print(f"Metadata    : {len(metadata)}")

    # --------------------------------------------------------
    # Verify FAISS <-> metadata alignment
    # --------------------------------------------------------

    if index.ntotal != len(metadata):

        raise RuntimeError(
            f"FAISS contains {index.ntotal} vectors "
            f"but metadata contains {len(metadata)} entries."
        )

    print("Knowledge base loaded.")

    return index, metadata


# ============================================================
# EXTRACT METADATA
# ============================================================

def extract_chunk_metadata(raw_metadata):

    """
    Extract the list containing one metadata entry per
    FAISS vector.

    Supports several possible metadata.pkl structures.
    """

    # --------------------------------------------------------
    # Case 1:
    #
    # metadata.pkl itself is already a list
    # --------------------------------------------------------

    if isinstance(raw_metadata, list):

        return raw_metadata

    # --------------------------------------------------------
    # Case 2:
    #
    # metadata.pkl is a dictionary
    # --------------------------------------------------------

    if isinstance(raw_metadata, dict):

        # Most likely possibilities
        possible_keys = [
            "data",
            "chunks",
            "metadata",
            "items",
            "records"
        ]

        for key in possible_keys:

            value = raw_metadata.get(key)

            if isinstance(value, list):

                return value

        # ----------------------------------------------------
        # Automatic detection
        #
        # Look for a list whose elements look like chunks.
        # ----------------------------------------------------

        for key, value in raw_metadata.items():

            if not isinstance(value, list):
                continue

            if len(value) == 0:
                continue

            first = value[0]

            if isinstance(first, dict):

                # A chunk normally has at least one of these
                # fields.
                chunk_fields = {
                    "document",
                    "title",
                    "text",
                    "hierarchy",
                    "start_page",
                    "end_page"
                }

                if chunk_fields.intersection(first.keys()):

                    print(
                        f"Using metadata field: '{key}'"
                    )

                    return value

        # ----------------------------------------------------
        # Nothing worked
        # ----------------------------------------------------

        print()
        print("ERROR: Could not find chunk metadata.")
        print()
        print("Metadata structure:")
        print(f"Type: {type(raw_metadata)}")

        print()

        if isinstance(raw_metadata, dict):

            print("Keys:")

            for key, value in raw_metadata.items():

                if hasattr(value, "__len__"):
                    length = len(value)
                else:
                    length = "N/A"

                print(
                    f"  {key}: "
                    f"{type(value).__name__}, "
                    f"length={length}"
                )

        raise RuntimeError(
            "Could not determine where chunk metadata is stored."
        )

    # --------------------------------------------------------
    # Unknown structure
    # --------------------------------------------------------

    raise RuntimeError(
        f"Unsupported metadata type: {type(raw_metadata)}"
    )


# ============================================================
# LOAD EMBEDDING MODEL
# ============================================================

def load_model():

    print()
    print("=" * 70)
    print("LOADING EMBEDDING MODEL")
    print("=" * 70)

    print(f"Model : {EMBEDDING_MODEL}")

    model = SentenceTransformer(EMBEDDING_MODEL)

    print("Model loaded.")

    return model


# ============================================================
# SEARCH
# ============================================================

def search_kb(
    query,
    model,
    index,
    metadata,
    top_k=DEFAULT_TOP_K
):

    # --------------------------------------------------------
    # Convert query into embedding
    # --------------------------------------------------------

    query_embedding = model.encode(
        [query],
        normalize_embeddings=True,
        convert_to_numpy=True
    )

    # --------------------------------------------------------
    # Search FAISS
    # --------------------------------------------------------

    scores, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for rank, (score, index_id) in enumerate(
        zip(scores[0], indices[0]),
        start=1
    ):

        # FAISS can return -1 when there isn't enough data
        if index_id < 0:
            continue

        # ----------------------------------------------------
        # FAISS vector ID corresponds directly to the metadata
        # list index because build_kb.py added vectors and
        # metadata in the same order.
        # ----------------------------------------------------

        item = metadata[index_id]

        results.append(
            {
                "rank": rank,
                "score": float(score),
                "index_id": int(index_id),
                "metadata": item,
            }
        )

    return results


# ============================================================
# DISPLAY
# ============================================================

def display_results(query, results):

    print()
    print("=" * 70)
    print("QUERY")
    print("=" * 70)

    print(query)

    print()
    print("=" * 70)
    print(f"TOP {len(results)} RESULTS")
    print("=" * 70)

    for result in results:

        item = result["metadata"]

        print()
        print("-" * 70)

        print(f"RANK      : {result['rank']}")
        print(f"SCORE     : {result['score']:.4f}")
        print(f"VECTOR ID : {result['index_id']}")

        print(
            f"DOCUMENT  : "
            f"{item.get('document', 'N/A')}"
        )

        print(
            f"TITLE     : "
            f"{item.get('title', 'N/A')}"
        )

        hierarchy = item.get("hierarchy", [])

        if hierarchy:

            print(
                "HIERARCHY : "
                + " > ".join(hierarchy)
            )

        print(
            f"PAGES     : "
            f"{item.get('start_page', 'N/A')} - "
            f"{item.get('end_page', 'N/A')}"
        )

        print(
            f"PART      : "
            f"{item.get('part', 0) + 1} / "
            f"{item.get('total_parts', 1)}"
        )

        print()

        text = item.get("text", "")

        print("TEXT")
        print("-" * 70)

        if len(text) > MAX_TEXT_CHARS:

            print(
                text[:MAX_TEXT_CHARS]
            )

            print()

            print(
                f"... "
                f"[{len(text) - MAX_TEXT_CHARS} "
                f"more characters]"
            )

        else:

            print(text)

    print()
    print("=" * 70)


# ============================================================
# INTERACTIVE MODE
# ============================================================

def interactive_mode(
    model,
    index,
    metadata
):

    print()
    print("=" * 70)
    print("INTERACTIVE KB SEARCH")
    print("=" * 70)

    print()
    print(
        "Enter a question to search the "
        "datasheet knowledge base."
    )

    print(
        "Type 'exit' or 'quit' to stop."
    )

    print()

    while True:

        try:

            query = input("Query > ").strip()

        except (KeyboardInterrupt, EOFError):

            print()
            print("Exiting.")

            break

        if not query:
            continue

        if query.lower() in {
            "exit",
            "quit"
        }:

            break

        results = search_kb(
            query=query,
            model=model,
            index=index,
            metadata=metadata,
            top_k=DEFAULT_TOP_K
        )

        display_results(
            query,
            results
        )


# ============================================================
# MAIN
# ============================================================

def main():

    print("=" * 70)
    print("DATASHEET KNOWLEDGE BASE SEARCH")
    print("=" * 70)

    # --------------------------------------------------------
    # Load KB
    # --------------------------------------------------------

    index, metadata = load_kb()

    # --------------------------------------------------------
    # Load embedding model
    # --------------------------------------------------------

    model = load_model()

    # --------------------------------------------------------
    # Command-line mode
    #
    # Example:
    #
    # python search_kb.py \
    # "What is the SPI clock frequency?"
    #
    # Optional:
    #
    # python search_kb.py \
    # "SPI clock frequency" 10
    # --------------------------------------------------------

    if len(sys.argv) >= 2:

        query = " ".join(sys.argv[1:])

        # ----------------------------------------------------
        # If final argument is an integer, treat it as K
        # ----------------------------------------------------

        top_k = DEFAULT_TOP_K

        if len(sys.argv) >= 3:

            try:

                possible_k = int(sys.argv[-1])

                if possible_k > 0:

                    top_k = possible_k

                    query = " ".join(
                        sys.argv[1:-1]
                    )

            except ValueError:

                pass

        results = search_kb(
            query=query,
            model=model,
            index=index,
            metadata=metadata,
            top_k=top_k
        )

        display_results(
            query,
            results
        )

    # --------------------------------------------------------
    # Interactive mode
    # --------------------------------------------------------

    else:

        interactive_mode(
            model,
            index,
            metadata
        )


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()