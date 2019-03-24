import numpy as np
import sys
from mpl_scipub.dataset import DataSet
from mpl_scipub.plotter import Plot


##### Example data #####

# Random
n_pnts = 100
random_1d_a = np.random.rand(n_pnts)
random_1d_b = np.random.rand(n_pnts)
random_3d_a = np.random.rand(n_pnts,3)
random_3d_b = np.random.rand(n_pnts,3)

# Functions
n_pnts = 1000
heart = np.zeros((n_pnts,3))
heart_z = np.linspace(0.0,30.0,n_pnts)
heart_x = 16.0*np.sin(heart_z)**3
heart_y = 13.0*np.cos(heart_z)-5.0*np.cos(2.0*heart_z)-2.0*np.cos(3.0*heart_z)-np.cos(4.0*heart_z)
heart[:,0] = heart_x
heart[:,1] = heart_y
heart[:,2] = heart_z
mesh_x, mesh_y = np.meshgrid(np.arange(-1,1,0.1),np.arange(-2,2,0.1))
func_1 = (mesh_x**2+mesh_y**2)*np.exp(-(mesh_x**2+mesh_y**2))

##### Examples #####

def simple_line():
    """Example of parametric line graph"""

    # Make datasets
    dataset_a = DataSet(heart,plot='line')

    # Make plot and add data
    plot = Plot(dim=3,elevation=115,angle=-90)
    plot.set_axes(xlim=(-20,20),ylim=(-20,20),zlim=(-5,35),xticks=(10,10),yticks=())
    plot.add_dataset(dataset_a)

    # Plot graph and display
    plot.plot()
    plot.display()


def simple_scatter():
    """Example of two overlaid scatter plots"""

    # Make two datasets specifying scatter graph, first coloured by random points, second sized by random points
    dataset_a = DataSet(random_3d_a,plot='scatter',colour_map='Reds',colour=random_1d_a)
    dataset_b = DataSet(random_3d_b,plot='scatter',colour='blue',marker_size=random_1d_b*10)

    # Make plot object, set as 3d and add data sets
    plot = Plot()
    plot.set_dimensions(dim=3)
    plot.add_dataset(dataset_a)
    plot.add_dataset(dataset_b)

    # Plot graph and display
    plot.plot()
    plot.display()


def simple_surface():
    """Example of surface plot, using either mesh or points"""

    # Make dataset with data provided as [x,y,z], where x,y,z, are meshes
    dataset_a = DataSet([mesh_x,mesh_y,func_1],plot='surface_mesh',colour_map='Blues')

    # Make plot and add data
    plot = Plot(dim=3,elevation=20,angle=130)
    plot.add_dataset(dataset_a)

    # Plot graph and display
    plot.plot()
    plot.set_axes(xlim=(-1.05,1.05),ylim=(-2.05,2.05),zlim=(-0.55,0.55))
    plot.display()

    # Make dataset with data provided as (n,3)
    dataset_b = DataSet(random_3d_b,plot='surface_points',colour_map='Reds')

    # Make plot and add data
    plot = Plot(dim=3,elevation=20,angle=130)
    plot.add_dataset(dataset_a)

    # Plot graph and display
    plot.plot()
    # plot.set_axes(xlim=(-1.05,1.05),ylim=(-2.05,2.05),zlim=(-0.55,0.55))
    plot.display()



if __name__ == '__main__':

    options = {
        0: simple_line,
        1: simple_scatter,
        2: simple_surface,
        # 2: advanced_line,
        # 3: scatter_and_line,
        # 4: simple_bar,
        # 5: simple_error,
    }

    example = int(sys.argv[1])
    options[example]()


