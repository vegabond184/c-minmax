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
## Performance

- On small arrays, **Python** and **C** perform similarly.  
- On large arrays (e.g., **1 million integers**):  
  - **C implementation (`findMin` / `findMax`)** runs ~2× faster.  
- Performance gain increases with input size because **C avoids Python’s interpreter overhead**.  

✅ This makes the **C DLL approach** useful when you need **high-performance numeric operations**.
---

## 📂 Project Structure
<pre>
  |── minmax.c 
  ├── minmax.dll 
  ├── benchmark.py 
  └── README.md 
</pre>



---

## ⚙️ Usage

### 1. Compile the C code
On Windows, you can use **MinGW** or **MSVC** to compile:

```sh
gcc -shared -o minmax.dll -fPIC minmax.c

```
### 2. Run python script

```sh
python benchmark.py

```

--------------------------------------------------
