import time
from ctypes import cdll

lib = cdll.LoadLibrary("target/release/liborz.dylib")
lib2 = cdll.LoadLibrary("main.dylib")

d = 35

# t1 = time.time()
# result = lib.fibonacci(d)
# t2 = time.time()

# print("=======Rust=======")
# print("use time: " + str(round(t2 - t1, 2)) + "s")
# print("result is: " + str(result) + "\n")


# t1 = time.time()
# result = lib2.fibonacci(d)
# t2 = time.time()

# print("=======Go=======")
# print("use time: " + str(round(t2 - t1, 2)) + "s")
# print("result is: " + str(result) + "\n")

# lib2.getData()

def F(n):
  if n == 0: return 0
  elif n == 1: return 1
  else: return F(n - 1) + F(n - 2)

def Print2(f, d, type):
  t1 = time.time()
  result = f(d)
  t2 = time.time()

  print("======" + type + "======")
  print("use time: " + str(round(t2 - t1, 2)) + "s")
  print("result is: " + str(result) + "\n")


Print2(lib.fibonacci, d, "Rust")
Print2(lib2.fibonacci, d, "Go")
Print2(F, d, "Python")
