import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import matplotlib.ticker as ticker
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


class Plot:
    """Plot wide variety of matplotlib graphs with common interface"""


    ##### Functions to control plot settings #####

    def __init__(self):
        """Set default parameters"""

        self.num_datasets = 0 # Total number of added data sets
        self.datasets = [] # List of added data sets
        self.initialised = False # Figure and axes initialised
        self.finalised = False # Final plot properties adjusted
        self.set_plot_size() # Initialise plot size to 4x4cm
        self.set_text_size() # Initialise text size to 10pt
        self.set_dimensions() # 2D/3D plot
        self.set_axes() # Default axes labels


    def set_plot_size(self, width = 4, height = 4):
        """Set plot size in cm"""

        params = {"figure.figsize": (width, height)}
        pylab.rcParams.update(params)


    def set_text_size(self, font = 10, title = 10, label = 10):
        """Set font, title and label size"""
        params = {"legend.fontsize": font,
                  "axes.labelsize": label,
                  "axes.titlesize": title,
                  "xtick.labelsize": label,
                  "ytick.labelsize": label}
        pylab.rcParams.update(params)


    def set_dimensions(self,dim=2):
        """Set dimensionality of plot, default 2D"""

        if dim<2 or dim>3:
            print("Must be 2D or 3D")
        else:
            self.dimensions = dim


    def set_axes(self, **kwargs):
        """Sets axes labels, limits and ticks etc."""

        self.axis_xlabel = kwargs.get("xlabel", "X")
        self.axis_ylabel = kwargs.get("ylabel", "Y")
        self.axis_zlabel = kwargs.get("zlabel", "Z")
        self.axis_xlim = kwargs.get("xlim", None)
        self.axis_ylim = kwargs.get("ylim", None)
        self.axis_zlim = kwargs.get("zlim", None)
        self.axis_xticks = kwargs.get("xticks", None)
        self.axis_yticks = kwargs.get("yticks", None)
        self.axis_zticks = kwargs.get("zticks", None)
        self.axis_xlog = kwargs.get("xlog", False)
        self.axis_ylog = kwargs.get("ylog", False)
        self.axis_zlog = kwargs.get("zlog", False)


    ##### Functions to add data sets #####

    def add_dataset(self,dataset,**kwargs):
        """Add DataSet object"""

        try:
            self.datasets.append(dataset) # Append to data sets
            self.num_datasets += 1
        except:
            print("Cannot add data set")


    ##### Plotting functions #####

    def initialise_plot(self):
        """Initialise axis and figure"""

        # Initialise plot if not already called as 2D or 3D plot
        if self.initialised:
            pass
        else:
            if self.dimensions == 2:
                self.fig, self.ax = plt.subplots()
            elif self.dimensions == 3:
                self.fig = plt.figure()
                self.ax = Axes3D(self.fig)
            self.initialised = True


    def plot(self):
        """Plot each data set"""

        if self.dimensions == 2:
            self.initialise_plot()
            for dataset in self.datasets:
                if dataset.plot_type == 'scatter':
                    self.scatter_2d(dataset)


    def scatter_2d(self,dataset):
        """Scatter graph in 2D"""

        self.ax.scatter(dataset.data[:,0], dataset.data[:,1], label = dataset.label,
                         marker = dataset.marker_style, s = dataset.marker_size,
                         color=dataset.colour)




    def finalise_plot(self):
        """Finalise plot properties - called when saved or visualised"""

        # Finalise plot if not already called
        if self.finalised:
            pass
        else:
            # Axes properties
            self.ax.set_xlabel(self.axis_xlabel)
            self.ax.set_ylabel(self.axis_ylabel)
            if self.axis_xlim is not None: self.ax.set_xlim(self.axis_xlim)
            if self.axis_ylim is not None: self.ax.set_xlim(self.axis_xlim)
            if self.axis_xticks is not None:
                majorLocator = ticker.MultipleLocator(self.axis_xticks[0])
                minorLocator = ticker.MultipleLocator(self.axis_xticks[1])
                self.ax.xaxis.set_major_locator(majorLocator)
                self.ax.xaxis.set_minor_locator(minorLocator)
            if self.axis_yticks is not None:
                majorLocator = ticker.MultipleLocator(self.axis_yticks[0])
                minorLocator = ticker.MultipleLocator(self.axis_yticks[1])
                self.ax.yaxis.set_major_locator(majorLocator)
                self.ax.yaxis.set_minor_locator(minorLocator)
            if self.axis_xlog: self.ax.set_xscale('log')
            if self.axis_ylog: self.ax.set_yscale('log')
            if self.dimensions == 3:
                # 3D additions
                self.ax.set_zlabel(self.axis_zlabel)
                if self.axis_zlim is not None: self.ax.set_zlim(self.axis_zlim)
                if self.axis_zticks is not None:
                    majorLocator = ticker.MultipleLocator(self.axis_zticks[0])
                    minorLocator = ticker.MultipleLocator(self.axis_zticks[1])
                    self.ax.zaxis.set_major_locator(majorLocator)
                    self.ax.zaxis.set_minor_locator(minorLocator)

            self.finalised = True


    ##### Save or visualise #####

    def display(self):
        """Display figure"""

        self.finalise_plot() # Apply final changes to plot
        plt.show()
        self.initialised = False
        self.finalised = False


    def save(self, name="plot", fmt="pdf", dpi_quality=400):
        """Save figure"""

        self.finalise_plot() # Apply final changes to plot
        filename = name+"."+fmt
        plt.savefig(filename, dpi=dpi_quality, bbox_inches="tight")


