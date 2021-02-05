import numpy as np
from csv import writer

pts = np.arange(-2, 15)
f = lambda a, N: lambda n: np.power(a, n / N) * int(n >= 0)
vals_a = map(f(0.5, 2), pts)
vals_b = map(f(1 / np.sqrt(2), 2), pts)
vals_c = map(f(0.5, 4), pts)

with open("hw02/q3-3.csv", 'w') as f:
    csv_data = writer(f)
    csv_data.writerow(['n', "3a", "3b", "3c"])
    csv_data.writerows(zip(pts, vals_a, vals_b, vals_c))
