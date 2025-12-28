import pandas as pd
import matplotlib.pyplot as p

d = {
    'k1': [10, 45, 11, 67, 32, 12, 87, 99, 33, 22],
    'k2': [109, 415, 111, 671, 16, 121, 87, 919, 333, 32],
    'k3': [70, 99, 121, 637, 312, 18, 99, 119, 43, 212],
    'k4': [110, 445, 41, 69, 36, 14, 822, 199, 233, 322],
    'k5': [111, 415, 154, 267, 342, 126, 867, 616, 334, 44]
}

k = pd.DataFrame(d)
z = k[['k1', 'k3']]
z.plot()
p.show()

p.scatter(k['k1'], k['k3'], s=200, c='red')
p.savefig("/storage/emulated/0/Download/my_plot.png")
p.show()
