from dormrod_mpl import DataSet, Plot
import numpy as np

random_xy1 = np.random.rand(100,2)
random_xy2 = np.random.rand(100,2)
sine = np.zeros((100,2))
sine[:,0] = np.linspace(0,10,100)
sine[:,1] = np.sin(sine[:,0])
cos = np.zeros_like(sine)
cos[:,0] = sine[:,0]
cos[:,1] = np.cos(cos[:,0])
random_error = np.random.rand(100)

sine_ds=DataSet(sine,error_y=random_error,error_style='shade')
cos_ds=DataSet(cos)

plot=Plot()
plot.add_dataset(sine_ds)
plot.add_dataset(cos_ds)
plot.plot()
plot.display()
