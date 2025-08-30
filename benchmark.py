import ctypes
import time
import random


# -------------------------
# Load C DLL
# -------------------------
minmax_lib = ctypes.CDLL(r"C:\Users\hp\minmax\minmax.dll")

# Function signatures
minmax_lib.findMax.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
minmax_lib.findMax.restype = ctypes.c_int

minmax_lib.findMin.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
minmax_lib.findMin.restype = ctypes.c_int


# -------------------------
# Benchmark function
# -------------------------
def benchmark_array(size: int):
    """Compare C DLL vs Python min/max for an array of given size."""
    
    # Generate random test array
    py_values = [random.randint(-10**9, 10**9) for _ in range(size)]
    c_array = (ctypes.c_int * size)(*py_values)

    # --- C DLL test ---
    start_c = time.perf_counter()
    c_max = minmax_lib.findMax(c_array, size)
    c_min = minmax_lib.findMin(c_array, size)
    end_c = time.perf_counter()

    # --- Python test ---
    start_py = time.perf_counter()
    py_max = max(py_values)
    py_min = min(py_values)
    end_py = time.perf_counter()

    # --- Validation ---
    correct = (c_max == py_max) and (c_min == py_min)

    return {
        "size": size,
        "c_time": end_c - start_c,
        "py_time": end_py - start_py,
        "c_max": c_max,
        "c_min": c_min,
        "py_max": py_max,
        "py_min": py_min,
        "match": correct
    }


# -------------------------
# Run benchmarks
# -------------------------
test_sizes = [10**2,10**3, 10**5, 10**6]

print("Benchmarking C DLL vs Python min/max\n")
for size in test_sizes:
    result = benchmark_array(size)
    print(f"Array size: {result['size']}")
    print(f"Results match? {result['match']}")
    print(f"C DLL -> min: {result['c_min']}, max: {result['c_max']}, time: {result['c_time']:.6f} sec")
    print(f"Python -> min: {result['py_min']}, max: {result['py_max']}, time: {result['py_time']:.6f} sec")
    print(f"C DLL faster? {result['c_time'] < result['py_time']}")
    print("-" * 50)
