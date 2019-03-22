import numpy as np
import sys
from mpl_scipub.dataset import DataSet
from mpl_scipub.plotter import Plot


##### Example data #####

x,y = np.meshgrid(np.arange(-1,1,0.1),np.arange(-2,2,0.1))
z = (x**2+y**2)*np.exp(-(x**2+y**2)) # Arbitrary radially symmetric function


##### Examples #####

def simple_heatmap():
    """Example heatmap of function z(x,y)"""

    # Make dataset, with data provided [x,y,z]
    dataset_a = DataSet([x,y,z],plot='heat')

    # Make plot and add data
    plot = Plot()
    plot.add_dataset(dataset_a)

    # Plot graph and display
    plot.plot()
    plot.display()


def advanced_heatmap():
    """Example heatmap of function z(x,y) with additional options"""

    # Make dataset, with data provided [x,y,z], colour normalisation conditions and interpolation method
    dataset_a = DataSet([x,y,z],plot='heat',colour_map='Blues',colour_norm=(0.0,0.2),surface_interpolation='bilinear')

    # Make plot and add data
    plot = Plot()
    plot.add_dataset(dataset_a)

    # Plot graph and display
    plot.plot()
    plot.display()


def simple_contour():
    """Example contour plot of function z(x,y)"""

    # Make dataset, with data provided [x,y,z]
    dataset_a = DataSet([x,y,z],plot='contour',colour_map='Greys')

    # Make plot and add data
    plot = Plot()
    plot.add_dataset(dataset_a)

    # Plot graph and display
    plot.plot()
    plot.display()


def advanced_contour():
    """Example contour plot of function z(x,y)"""

    # Make dataset, with data provided [x,y,z]
    dataset_a = DataSet([x,y,z-0.2],plot='contour',colour_map='coolwarm',colour_norm=(-0.2,0.2),line_width=1,line_style='--')
    dataset_a.set_contours(number=30,limits=(-0.5,0.5)) # Set number of contours, limits or specific values

    # Make plot and add data
    plot = Plot()
    plot.add_dataset(dataset_a)

    # Plot graph and display
    plot.plot()
    plot.display()


if __name__ == '__main__':

    options = {
        0: simple_heatmap,
        1: advanced_heatmap,
        2: simple_contour,
        3: advanced_contour
    }

    example = int(sys.argv[1])
    options[example]()
