import numpy as np
from dormrod_mpl.dataset import DataSet
from dormrod_mpl.plotter import Plot

# Generate data
cosine = np.zeros((100,2))
cosine[:,0] = np.linspace(0,10,100)
cosine[:,1] = np.cos(cosine[:,0])

random = np.zeros((50,2))
random[:,0] = np.random.uniform(0,10,50)
random[:,1] = np.random.uniform(-1,1,50)
random_size = np.random.uniform(5,50,50)
random_colour = np.random.uniform(0,1,50)


# Make DataSet specifying properties on instantiation
dataset_a = DataSet(cosine, plot='line', label='cosine', colour='black', line_width=2)

# Make DataSet specifiying properties through setters
dataset_b = DataSet(random, plot='scatter', label='random')
dataset_b.set_marker(style='o',size=random_size)
dataset_b.set_colour(map='coolwarm',colour=random_colour)

# Make Plot class and add DataSets
plot = Plot()
plot.add_dataset(dataset_a)
plot.add_dataset(dataset_b)

# Adjust plot properties
plot.set_axes(xlim=(0,10),xticks=(1,0.2),yticks=(0.2,0.05),xlabel=r'$x$',ylabel=r'$f\left(x\right)$') # Latex-style labels

# Plot graphs
plot.plot()
plot.save(fmt='png')
plot.display()
