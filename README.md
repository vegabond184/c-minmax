# C Min/Max DLL with Python Integration

This project demonstrates how to implement **custom `min` and `max` functions in C**, expose them through a DLL, and call them from Python using `ctypes`.  
It also includes a **benchmarking script** that compares the performance of the C functions with Python's built-in `min` and `max`.

---

## 🚀 Features
- C implementation of `findMin` and `findMax`.
- Compiled into a DLL for use in Python.
- Python script to:
  - Call the DLL functions via `ctypes`.
  - Compare results with Python’s built-in `min` and `max`.
  - Benchmark performance on arrays of different sizes.

---

## 📂 Project Structure

.
├── minmax.c # C source code (DLL)
├── minmax.dll # Compiled DLL (Windows)
├── benchmark.py # Python benchmarking script
└── README.md # Project documentation



---

## ⚙️ Usage

### 1. Compile the C code
On Windows, you can use **MinGW** or **MSVC** to compile:

```sh
gcc -shared -o minmax.dll -fPIC minmax.c


python benchmark.py

yaml

Array size: 100000
Results match? True
C DLL -> min: -999872, max: 999421, time: 0.012345 sec
Python -> min: -999872, max: 999421, time: 0.045678 sec
C DLL faster? True
--------------------------------------------------
