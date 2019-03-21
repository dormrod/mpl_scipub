import numpy as np
import sys
from dormrod_mpl.dataset import DataSet
from dormrod_mpl.plotter import Plot


##### Example data #####

# Random
n_pnts = 100
random_1d = np.random.rand(n_pnts)
random_2d_a = np.random.rand(n_pnts,2)
random_2d_b = np.random.rand(n_pnts,2)

# Functions
sine = np.zeros_like(random_2d_a)
sine[:,0] = np.linspace(0,10,n_pnts)
sine[:,1] = np.sin(sine[:,0])
cosine = np.zeros_like(random_2d_a)
cosine[:,0] = np.linspace(0,10,n_pnts)
cosine[:,1] = np.cos(cosine[:,0])
gaussian = np.zeros_like(random_2d_a)
gaussian[:,0] = np.linspace(-5,5,n_pnts)
gaussian[:,1] = np.exp(-0.5*gaussian[:,0]**2)
linear = np.zeros_like(random_2d_a)
linear[:,0] = np.linspace(0,10,n_pnts)
linear[:,1] = linear[:,0]*2.0+1.0


##### Examples #####

def simple_line():
    """Example of two overlaid line graphs"""

    # Make two datasets
    dataset_a = DataSet(sine)
    dataset_b = DataSet(cosine)

    # Make plot and add data
    plot = Plot()
    plot.add_dataset(dataset_a)
    plot.add_dataset(dataset_b)

    # Plot graph and display
    plot.plot()
    plot.display()


def simple_scatter():
    """Example of two overlaid scatter plots"""

    # Make two datasets specifying scatter graph
    dataset_a = DataSet(random_2d_a,plot='scatter')
    dataset_b = DataSet(random_2d_b,plot='scatter')

    # Make plot object and add data sets
    plot = Plot()
    plot.add_dataset(dataset_a)
    plot.add_dataset(dataset_b)

    # Plot graph and display
    plot.plot()
    plot.display()


def advanced_line():
    """Example of line graphs demonstrating options"""

    # Make dataset specifying arguments
    dataset_a = DataSet(sine,line_style='--',line_width=2,marker_style='x',marker_size='5',colour='firebrick')

    # Make dataset changing options using setters
    dataset_b = DataSet(cosine)
    dataset_b.set_line(style=':',width=1)
    dataset_b.set_marker(style='+',size=5)
    dataset_b.set_colour(colour='skyblue')

    # Make plot object and adjust properties using setters
    plot = Plot()
    plot.add_dataset(dataset_a)
    plot.add_dataset(dataset_b)
    plot.set_axes(xlim=(0,8),ylim=(-1.1,1.1),xlabel=r'$x$',ylabel=r'$f\left(x\right)$',xticks=(1,0.1),yticks=(0.2,0.05))

    # Plot graph and display
    plot.plot()
    plot.display()


def scatter_and_line():
    """Example containing both a scatter and line graph"""

    # Make random data points around straight line
    random_linear = np.zeros((1000,2))
    random_linear[:,0] = np.random.uniform(0,10,1000)
    random_error = np.random.normal(0.0,2.0,1000)
    random_linear[:,1] = random_linear[:,0]*2.0+1.0+random_error

    # Make datasets, order determining line graph on top
    dataset_a = DataSet(random_linear,plot='scatter',order=0,label='Random')
    dataset_b = DataSet(linear,plot='line',colour='black',order=1,label='Linear')

    # Colour scatter graph by error
    dataset_a.set_colour(map='coolwarm',colour=random_error)

    # Make plot object and add datasets
    plot = Plot()
    plot.add_dataset(dataset_a)
    plot.add_dataset(dataset_b)
    plot.set_legend(legend=True)

    # Plot graph and display
    plot.plot()
    plot.display()


def simple_bar():
    """Example of simple bar chart"""

    # Make random discrete data
    discrete_a = np.zeros((8,2))
    discrete_b = np.zeros((8,2))
    discrete_c = np.zeros((8,2))
    discrete_a[:,0] = np.arange(8)
    discrete_b[:,0] = np.arange(8)
    discrete_c[:,0] = np.arange(8)
    discrete_a[:,1] = np.random.rand(8)*10
    discrete_b[:,1] = np.random.rand(8)*10
    discrete_c[:,1] = np.random.rand(8)*10

    # Make data sets, if using multiple bar_width must be the same
    dataset_a = DataSet(discrete_a,colour='black',bar_width=0.8,plot='bar')
    dataset_b = DataSet(discrete_b,colour='steelblue',bar_width=0.8,plot='bar')
    dataset_c = DataSet(discrete_c,colour='forestgreen',bar_width=0.8,plot='bar')

    # Make plot object and add data sets
    plot = Plot()
    plot.add_dataset(dataset_a)
    plot.add_dataset(dataset_b)
    plot.add_dataset(dataset_c)
    plot.set_axes(xticks=(1,1),ylim=(0,15))
    plot.set_legend(legend=True)
    plot.set_text_size(legend=8)

    # Plot graph and display
    plot.plot()
    plot.display()


if __name__ == '__main__':

    example = int(sys.argv[1])

    options = {
        0: simple_line,
        1: simple_scatter,
        2: advanced_line,
        3: scatter_and_line,
        4: simple_bar
    }

    options[example]()

