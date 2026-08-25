import numpy as np

t: float = 10
old_t: float = 5
s: float = 2
old_s: float = 0
v: float = 0

def calculate_velocity():
    v = (s-old_s)/(t-old_t)
    print(v)
