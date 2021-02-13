import numpy as np
import matplotlib.pyplot as plt
from csv import writer

alpha = 0.5
xs = np.arange(-2, 5)
x_func = lambda n: alpha**n * int(n >= 0)
g = lambda x: lambda n: x(n) - alpha * x(n - 1)

q7_1 = list(map(g(x_func), xs))

with open("hw03/q7-1.csv", 'w') as f:
    csv_data = writer(f)
    csv_data.writerow(['n', "gn"])
    csv_data.writerows(zip(xs, q7_1))
