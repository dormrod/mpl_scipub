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

        self._num_datasets = 0 # Total number of added data sets
        self._datasets = [] # List of added data sets
        self._initialised = False # Figure and axes initialised
        self._finalised = False # Final plot properties adjusted
        self.set_plot_size() # Initialise plot size to 4x4cm
        self.set_text_size() # Initialise text size to 10pt
        self.set_dimensions() # 2D/3D plot
        self.set_axes_properties() # Default axes labels


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
            self._dimensions = dim


    def set_axes_properties(self, **kwargs):
        """Sets axes labels, limits and ticks etc."""

        self._axis_xlabel = kwargs.get("xlabel", "X")
        self._axis_ylabel = kwargs.get("ylabel", "Y")
        self._axis_zlabel = kwargs.get("zlabel", "Z")
        self._axis_xlim = kwargs.get("xlim", None)
        self._axis_ylim = kwargs.get("ylim", None)
        self._axis_zlim = kwargs.get("zlim", None)
        self._axis_xticks = kwargs.get("xticks", None)
        self._axis_yticks = kwargs.get("yticks", None)
        self._axis_zticks = kwargs.get("zticks", None)
        self._axis_xlog = kwargs.get("xlog", False)
        self._axis_ylog = kwargs.get("ylog", False)
        self._axis_zlog = kwargs.get("zlog", False)


    ##### Functions to add data sets #####

    def add_dataset(self,data,**kwargs):
        """Add (n,dimensions) data set"""

        try:
            data = np.array(data) # Make sure data in numpy array
            self._datasets.append(data) # Append to data sets
            self._num_datasets += 1
        except:
            print("Cannot add data set")


    ##### Plotting functions #####

    def initialise_plot(self):
        """Initialise axis and figure"""

        # Initialise plot if not already called as 2D or 3D plot
        if self._initialised:
            pass
        else:
            if self._dimensions == 2:
                self._fig, self._ax = plt.subplots()
            elif self._dimensions == 3:
                self._fig = plt.figure()
                self._ax = Axes3D(self._fig)
            self._initialised = True


    def finalise_plot(self):
        """Finalise plot properties - called when saved or visualised"""

        # Finalise plot if not already called
        if self._finalised:
            pass
        else:
            # Axes properties
            self._ax.set_xlabel(self._axis_xlabel)
            self._ax.set_ylabel(self._axis_ylabel)
            if self._axis_xlim is not None: self._ax.set_xlim(self._axis_xlim)
            if self._axis_ylim is not None: self._ax.set_xlim(self._axis_xlim)
            if self._axis_xticks is not None:
                majorLocator = ticker.MultipleLocator(self._axis_xticks[0])
                minorLocator = ticker.MultipleLocator(self._axis_xticks[1])
                self._ax.xaxis.set_major_locator(majorLocator)
                self._ax.xaxis.set_minor_locator(minorLocator)
            if self._axis_yticks is not None:
                majorLocator = ticker.MultipleLocator(self._axis_yticks[0])
                minorLocator = ticker.MultipleLocator(self._axis_yticks[1])
                self._ax.yaxis.set_major_locator(majorLocator)
                self._ax.yaxis.set_minor_locator(minorLocator)
            if self._axis_xlog: self._ax.set_xscale('log')
            if self._axis_ylog: self._ax.set_yscale('log')
            if self._dimensions == 3:
                # 3D additions
                self._ax.set_zlabel(self._axis_zlabel)
                if self._axis_zlim is not None: self._ax.set_zlim(self._axis_zlim)
                if self._axis_zticks is not None:
                    majorLocator = ticker.MultipleLocator(self._axis_zticks[0])
                    minorLocator = ticker.MultipleLocator(self._axis_zticks[1])
                    self._ax.zaxis.set_major_locator(majorLocator)
                    self._ax.zaxis.set_minor_locator(minorLocator)

            self._finalised = True


    ##### Save or visualise #####

    def display(self):
        """Display figure"""

        self.finalise_plot() # Apply final changes to plot
        plt.show()


    def save(self, name="plot", fmt="pdf", dpi_quality=400):
        """Save figure"""

        self.finalise_plot() # Apply final changes to plot
        filename = name+"."+fmt
        plt.savefig(filename, dpi=dpi_quality, bbox_inches="tight")



if __name__ == "__main__":
    plot = Plot()
    xy = np.random.rand(100)
    xy = xy.reshape(50,2)
    plot.add_dataset(xy)
