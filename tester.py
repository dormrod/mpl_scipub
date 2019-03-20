from plotter import Plot
from dataset import DataSet
import numpy as np

xy=np.random.rand(100).reshape(50,2)
data=DataSet(xy)
plot=Plot()
plot.add_dataset(data)
