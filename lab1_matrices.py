import numpy as np
import time as tm
f = open("output.txt", "w")
n = int(input("Introduce la n: "))
for i in range(2, n + 1):
    A = np.random.randint(10, size=(i, i))
    B = np.random.randint(10, size=(i, i))
    inicio = tm.perf_counter()
    C = np.dot(A, B)
    fin = tm.perf_counter()
    f.write(str(fin - inicio) + "\n")
