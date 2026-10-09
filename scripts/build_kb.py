import json
import pickle
from pathlib import Path

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


# ============================================================
# CONFIG
# ============================================================

CHUNKS_FILE = Path("../dataset/chunks/chunks.json")

KB_DIR = Path("../dataset/kb")

INDEX_FILE = KB_DIR / "index.faiss"
METADATA_FILE = KB_DIR / "metadata.pkl"

MODEL_NAME = "BAAI/bge-small-en-v1.5"

BATCH_SIZE = 32


# ============================================================
# LOAD CHUNKS
# ============================================================

def load_chunks():

    print("=" * 70)
    print("LOADING CHUNKS")
    print("=" * 70)

    print(f"Chunks file : {CHUNKS_FILE}")

    with open(
        CHUNKS_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        data = json.load(f)

    chunks = data["data"]

    print(f"Chunks loaded : {len(chunks)}")
    print()

    return chunks


# ============================================================
# BUILD EMBEDDING TEXT
# ============================================================

def build_embedding_text(chunk):
    """
    Build the text that will be embedded.

    We include the hierarchy because it provides important
    contextual information for datasheet retrieval.

    Example:

        nRF52832
        > 5 Electrical specification
        > 5.1 Recommended operating conditions

        <actual chunk text>
    """

    hierarchy = chunk.get(
        "hierarchy",
        []
    )

    hierarchy_text = " > ".join(
        hierarchy
    )

    return (
        f"Document: {chunk['document']}\n"
        f"Section: {hierarchy_text}\n\n"
        f"{chunk['text']}"
    )


# ============================================================
# LOAD MODEL
# ============================================================

def load_model():

    print("=" * 70)
    print("LOADING EMBEDDING MODEL")
    print("=" * 70)

    print(f"Model : {MODEL_NAME}")
    print()

    model = SentenceTransformer(
        MODEL_NAME
    )

    print("Model loaded.")
    print()

    return model


# ============================================================
# GENERATE EMBEDDINGS
# ============================================================

def generate_embeddings(
    model,
    chunks
):

    print("=" * 70)
    print("GENERATING EMBEDDINGS")
    print("=" * 70)

    texts = [
        build_embedding_text(chunk)
        for chunk in chunks
    ]

    print(
        f"Texts to embed : {len(texts)}"
    )

    print(
        f"Batch size     : {BATCH_SIZE}"
    )

    print()

    embeddings = model.encode(
        texts,

        batch_size=BATCH_SIZE,

        show_progress_bar=True,

        convert_to_numpy=True,

        normalize_embeddings=True,

        # Makes the embedding generation deterministic
        # and avoids unnecessary tensor copies.
        convert_to_tensor=False,
    )

    embeddings = np.asarray(
        embeddings,
        dtype=np.float32
    )

    print()

    print(
        f"Embedding shape : {embeddings.shape}"
    )

    print(
        f"Embedding dtype : {embeddings.dtype}"
    )

    return embeddings


# ============================================================
# BUILD FAISS INDEX
# ============================================================

def build_faiss_index(
    embeddings
):

    print("=" * 70)
    print("BUILDING FAISS INDEX")
    print("=" * 70)

    dimension = embeddings.shape[1]

    print(
        f"Embedding dimension : {dimension}"
    )

    # Because embeddings are normalized,
    # inner product == cosine similarity.
    index = faiss.IndexFlatIP(
        dimension
    )

    index.add(
        embeddings
    )

    print(
        f"Vectors in index : {index.ntotal}"
    )

    print()

    return index


# ============================================================
# SAVE KNOWLEDGE BASE
# ============================================================

def save_kb(
    index,
    chunks
):

    print("=" * 70)
    print("SAVING KNOWLEDGE BASE")
    print("=" * 70)

    KB_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    # --------------------------------------------------------
    # Save FAISS index
    # --------------------------------------------------------

    faiss.write_index(
        index,
        str(INDEX_FILE)
    )

    print(
        f"FAISS index : {INDEX_FILE}"
    )

    # --------------------------------------------------------
    # Save metadata
    # --------------------------------------------------------

    metadata = {
        "model": MODEL_NAME,
        "dimension": index.d,
        "metric": "cosine_similarity",
        "chunks": chunks,
    }

    with open(
        METADATA_FILE,
        "wb"
    ) as f:

        pickle.dump(
            metadata,
            f,
            protocol=pickle.HIGHEST_PROTOCOL
        )

    print(
        f"Metadata    : {METADATA_FILE}"
    )

    print()


# ============================================================
# MAIN
# ============================================================

def main():

    print()
    print("=" * 70)
    print("DATASHEET KNOWLEDGE BASE BUILDER")
    print("=" * 70)
    print()

    # --------------------------------------------------------
    # Load chunks
    # --------------------------------------------------------

    chunks = load_chunks()

    if not chunks:

        raise RuntimeError(
            "No chunks found."
        )

    # --------------------------------------------------------
    # Load embedding model
    # --------------------------------------------------------

    model = load_model()

    # --------------------------------------------------------
    # Generate embeddings
    # --------------------------------------------------------

    embeddings = generate_embeddings(
        model,
        chunks
    )

    # --------------------------------------------------------
    # Build FAISS
    # --------------------------------------------------------

    index = build_faiss_index(
        embeddings
    )

    # --------------------------------------------------------
    # Save
    # --------------------------------------------------------

    save_kb(
        index,
        chunks
    )

    # --------------------------------------------------------
    # Final summary
    # --------------------------------------------------------

    print("=" * 70)
    print("KNOWLEDGE BASE READY")
    print("=" * 70)

    print(
        f"Documents/chunks : {len(chunks)}"
    )

    print(
        f"Vector dimension  : {embeddings.shape[1]}"
    )

    print(
        f"FAISS vectors     : {index.ntotal}"
    )

    print()
    print("Files:")
    print(f"  {INDEX_FILE}")
    print(f"  {METADATA_FILE}")

    print("=" * 70)


if __name__ == "__main__":
    main()