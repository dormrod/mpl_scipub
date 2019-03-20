import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import numpy as np


class Plot:
    """Plot wide variety of matplotlib graphs with common interface"""


    ##### Functions to control plot settings #####

    def __int__(self):
        """Set default parameters"""

        self._num_datasets = 0 # Total number of added data sets
        self._datasets = [] # List of added data sets
        self._initialised = False # Figure and axes initialised
        self._finalised = False # Final plot properties adjusted
        self.set_plot_size() # Initialise plot size to 4x4cm
        self.set_text_size() # Initialise text size to 10pt
        self.set_dimensions() # 2D/3D plot


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

        # Initialise plot if not already called
        if self._initialised:
            pass
        else:
            self._fig, self._ax = plt.subplots()
            self._initialised = True


    def finalise_plot(self):
        """Finalise plot properties - called when saved or visualised"""

        # Finalise plot if not already called
        if self._finalised:
            pass
        else:
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
