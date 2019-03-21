from dormrod_mpl import DataSet, Plot
import numpy as np

random_xy1 = np.random.rand(100,2)
random_xy2 = np.random.rand(100,2)
random_ds1=DataSet(random_xy1)
random_ds2=DataSet(random_xy2)

plot=Plot()
plot.add_dataset(random_ds1)
plot.add_dataset(random_ds2)
plot.plot()
plot.display()
