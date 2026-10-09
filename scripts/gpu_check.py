"""Sanity check: CUDA visible to PyTorch, matmul correct on GPU, rough throughput."""
import time

import torch

assert torch.cuda.is_available(), "CUDA not available - is the nvidia driver loaded? (nvidia-smi)"
dev = torch.device("cuda")
p = torch.cuda.get_device_properties(dev)
print(f"torch {torch.__version__} | CUDA {torch.version.cuda} | cuDNN {torch.backends.cudnn.version()}")
print(f"GPU: {p.name} | {p.total_memory / 2**30:.1f} GiB | SM {p.major}.{p.minor}")

# Correctness: GPU result must match CPU.
a, b = torch.randn(512, 512), torch.randn(512, 512)
assert torch.allclose((a.cuda() @ b.cuda()).cpu(), a @ b, atol=1e-3), "GPU matmul mismatch"
print("matmul correctness: OK")

# Throughput: fp32 and fp16 TFLOPS on a 4096^2 matmul.
n = 4096
for dtype in (torch.float32, torch.float16):
    x, y = torch.randn(n, n, device=dev, dtype=dtype), torch.randn(n, n, device=dev, dtype=dtype)
    for _ in range(3):
        x @ y
    torch.cuda.synchronize()
    t, iters = time.perf_counter(), 20
    for _ in range(iters):
        x @ y
    torch.cuda.synchronize()
    dt = (time.perf_counter() - t) / iters
    print(f"{str(dtype):14} {2 * n**3 / dt / 1e12:6.2f} TFLOPS")

# Tiny training step: autograd + cuDNN conv on GPU.
model = torch.nn.Sequential(torch.nn.Conv2d(3, 16, 3), torch.nn.ReLU(), torch.nn.Flatten(), torch.nn.LazyLinear(10)).to(dev)
opt = torch.optim.SGD(model.parameters(), lr=0.01)
loss = torch.nn.functional.cross_entropy(model(torch.randn(32, 3, 32, 32, device=dev)), torch.randint(0, 10, (32,), device=dev))
loss.backward()
opt.step()
print(f"train step OK (loss {loss.item():.3f}) | peak mem {torch.cuda.max_memory_allocated() / 2**20:.0f} MiB")
