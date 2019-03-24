import numpy as np
import sys
from mpl_scipub.dataset import DataSet
from mpl_scipub.plotter import Plot


##### Example data #####

x_mesh,y_mesh = np.meshgrid(np.arange(-5,5.1,0.1),np.arange(-5,5.1,0.1))
z = (x_mesh**2+y_mesh**2)*np.exp(-(x_mesh**2+y_mesh**2)) # Arbitrary radially symmetric function
z = np.cos(x_mesh**2+y_mesh**2)*np.exp(-(x_mesh**2+y_mesh**2)/10)

##### Examples #####

def simple_heat():
    """Example heatmap of function z=z(x,y)"""

    # Make dataset, with data provided [x,y,z]
    dataset_a = DataSet([x_mesh,y_mesh,z],plot='heat')

    # Make plot and add data
    plot = Plot()
    plot.set_axes(xlim=(-2,2),ylim=(-2,2))
    plot.add_dataset(dataset_a)

    # Plot graph and display
    plot.plot()
    plot.display()


def advanced_heat():
    """Example heatmap of function z=z(x,y) with additional options"""

    # Make dataset, with data provided [x,y,z], colour normalisation conditions and interpolation method
    dataset_a = DataSet([x_mesh,y_mesh,z],plot='heat',colour_map='Blues',colour_norm=(-1,1),surface_interpolation='bilinear')

    # Make plot and add data
    plot = Plot()
    plot.add_dataset(dataset_a)
    plot.set_axes(xlim=(-4,4),ylim=(-4,4))

    # Plot graph and display
    plot.plot()
    plot.save(name='./figures/2d_heat',fmt='png')
    plot.display()


def simple_contour():
    """Example contour plot of function z(x,y)"""

    # Make dataset, with data provided [x,y,z]
    dataset_a = DataSet([x_mesh,y_mesh,z],plot='contour',colour_map='Greys')

    # Make plot and add data
    plot = Plot()
    plot.add_dataset(dataset_a)

    # Plot graph and display
    plot.plot()
    plot.display()


def advanced_contour():
    """Example contour plot of function z(x,y)"""

    # Make two datasets, with same data provided [x,y,z], to highlight different contours
    dataset_a = DataSet([x_mesh,y_mesh,z],plot='contour',colour_map='coolwarm',colour_norm=(-0.5,0.5),line_width=1,line_style='--')
    dataset_a.set_contours(number=9,limits=(-1,1)) # Set number of contours and limits
    dataset_b = DataSet([x_mesh,y_mesh,z],plot='contour',colour_map='Greys',colour_norm=(-1,0),line_width=0.5,line_style='-')
    dataset_b.set_contours(levels=[0.0]) # Set specific contour values

    # Make plot and add data
    plot = Plot()
    plot.add_dataset(dataset_a)
    plot.add_dataset(dataset_b)
    plot.set_axes(xlim=(-4,4),ylim=(-4,4))

    # Plot graph and display
    plot.plot()
    plot.save(name='./figures/2d_contour',fmt='png')
    plot.display()


if __name__ == '__main__':

    examples = {
        0: simple_heat,
        1: advanced_heat,
        2: simple_contour,
        3: advanced_contour,
    }

    if len(sys.argv) == 1:
        for i in range(4):
            examples[i]()
    else:
        i = int(sys.argv[1])
        examples[i]()
