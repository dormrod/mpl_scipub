import numpy as np
import sys
from dormrod_mpl.dataset import DataSet
from dormrod_mpl.plotter import Plot


##### Example data #####

# Random
n_pnts = 100
random_1d_a = np.random.rand(n_pnts)
random_1d_b = np.random.rand(n_pnts)
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
oscillating = np.zeros((n_pnts,2))
oscillating[:,0] = np.linspace(0.0,3.0,n_pnts)
oscillating[:,1] = (np.sin(10*oscillating[:,0])+oscillating[:,0])*np.exp(oscillating[:,1])
oscillating_error = np.exp(oscillating[:,0]/2)/5.0

##### Examples #####

def simple_line():
    """Example of two overlaid line graphs"""

    # Make two datasets
    dataset_a = DataSet(sine)
    dataset_b = DataSet(cosine)

    # Make plot and add data
    plot = Plot()
    plot.set_text()
    plot.add_dataset(dataset_a)
    plot.add_dataset(dataset_b)

    # Plot graph and display
    plot.plot()
    plot.save(name='./figures/2d_simple_line',fmt='png')
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
    plot.save(name='./figures/2d_simple_scatter',fmt='png')
    plot.display()


def advanced_line():
    """Example of line graphs demonstrating options"""

    # Make dataset specifying arguments
    dataset_a = DataSet(sine,line_style='-',line_width=1.5,marker_style='o',marker_size='4')

    # Make dataset changing options using setters
    dataset_b = DataSet(cosine)
    dataset_b.set_line(style='--',width=1.5)
    dataset_b.set_colour(colour='royalblue')

    # Make plot object and adjust properties using setters
    plot = Plot()
    plot.set_text(latex=True,label=12)
    plot.add_dataset(dataset_a)
    plot.add_dataset(dataset_b)
    plot.set_axes(xlim=(0,8),ylim=(-1.1,1.1),xlabel=r'$x$',ylabel=r'$f\left(x\right)$',xticks=(1.0,0.2),yticks=(0.2,0.05))

    # Plot graph and display
    plot.plot()
    plot.save(name='./figures/2d_advanced_line',fmt='png')
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
    plot.set_text(latex=True)
    plot.add_dataset(dataset_a)
    plot.add_dataset(dataset_b)
    plot.set_legend(legend=True)

    # Plot graph and display
    plot.plot()
    plot.save(name='./figures/2d_scatter_and_line',fmt='png')
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
    dataset_a = DataSet(discrete_a,colour='pink',bar_width=0.8,plot='bar',label='A')
    dataset_b = DataSet(discrete_b,colour='violet',bar_width=0.8,plot='bar',label='B')
    dataset_c = DataSet(discrete_c,colour='darkviolet',bar_width=0.8,plot='bar',label='C')

    # Make plot object and add data sets
    plot = Plot()
    plot.add_dataset(dataset_a)
    plot.add_dataset(dataset_b)
    plot.add_dataset(dataset_c)
    plot.set_axes(xticks=(1,1),xlim=(-0.5,7.5),ylim=(0,12))
    plot.set_legend(legend=True,location='upper right')
    plot.set_text(legend=8)

    # Plot graph and display
    plot.plot()
    plot.save(name='./figures/2d_simple_bar',fmt='png')
    plot.display()


def error():
    """Example of a simple line graph with error bars, or line graph with shading"""

    # Make data set using errors
    dataset_a = DataSet(oscillating,error_y=oscillating_error,plot='error_bar',label='Data and error')
    dataset_a.set_error(interval=5,width=1,cap=2)
    dataset_b = DataSet(oscillating,plot='error_shade',error_y=oscillating_error,order=0,colour='lightgrey',label='Error')
    dataset_c = DataSet(oscillating,plot='line',order=1,colour='firebrick',label='Data')

    # Make line graph with error bars
    plot_bar = Plot()
    plot_bar.set_legend(legend=True)
    plot_bar.add_dataset(dataset_a)
    plot_bar.plot()
    plot_bar.save(name='./figures/2d_error_bar',fmt='png')
    plot_bar.display()

    # Make line graph with shaded errors
    plot_shade = Plot()
    plot_shade.set_legend(legend=True,location='upper left')
    plot_shade.add_dataset(dataset_b)
    plot_shade.add_dataset(dataset_c)
    plot_shade.plot()
    plot_shade.save(name='./figures/2d_error_shade',fmt='png')
    plot_shade.display()


if __name__ == '__main__':

    examples = {
        0: simple_line,
        1: simple_scatter,
        2: advanced_line,
        3: scatter_and_line,
        4: simple_bar,
        5: error
    }

    if len(sys.argv) == 1:
        for i in range(6):
            examples[i]()
    else:
        i = int(sys.argv[1])
        examples[i]()

