import csv
import numpy as np

idxs = np.arange(-5, 2, 0.1)
unit_step = lambda x: 0 if x < 0 else 1
vals = [np.e**(2*i) * unit_step(-i) for i in idxs]

idxs2 = np.arange(-2, 5)
vals2 = [np.e**(-i) * unit_step(i) for i in idxs2]

with open("hw01/e5.csv", 'w') as f:
    csv_data = csv.writer(f)
    csv_data.writerow(["t", "exp"])
    csv_data.writerows(zip(idxs, vals))

with open("hw01/e6.csv", 'w') as f:
    csv_data = csv.writer(f)
    csv_data.writerow(["t", "exp"])
    csv_data.writerows(zip(idxs2, vals2))
