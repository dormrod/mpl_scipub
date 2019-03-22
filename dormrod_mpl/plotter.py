import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import matplotlib.ticker as ticker
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


class Plot:
    """Plot DataSet objects with matplotlib."""


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
        self.set_legend() # No legend


    def set_plot_size(self, width = 4, height = 4):
        """Set plot size in cm."""

        params = {"figure.figsize": (width, height)}
        pylab.rcParams.update(params)


    def set_text_size(self, legend = 10, title = 10, label = 10):
        """Set text size."""

        params = {"legend.title_fontsize": legend,
                  "legend.fontsize": legend,
                  "axes.labelsize": label,
                  "axes.titlesize": title,
                  "xtick.labelsize": label,
                  "ytick.labelsize": label}
        pylab.rcParams.update(params)


    def set_legend(self,**kwargs):
        """
        Set legend properties.
        
        :param legend: turn legend on or off
        :type legend: bool
        :param legend_title: set legend title
        :type legend_title: str
        :param legend_columns: number of columns in legend
        :type legend_columns: int
        :param legend_reverse: reverse order of legend 
        :type legend_reverse: bool
        """

        self.legend = kwargs.get("legend", False)
        self.legend_title = kwargs.get("title", None)
        self.legend_columns = kwargs.get("cols", 1)
        self.legend_anchor = kwargs.get("anchor", None)
        self.legend_reverse = kwargs.get("reverse", False)


    def set_dimensions(self,dim=2):
        """Set dimensionality of plot."""

        if dim<2 or dim>3:
            print("Must be 2D or 3D")
        else:
            self.dimensions = dim


    def set_axes(self, **kwargs):
        """
        Sets axes properties for x,y,z axes.
        
        :param xlabel: x-axis label
        :type xlabel: str
        :param xlim: x-axis limits 
        :type xlim: tuple
        :param xticks: positions of major and minor ticks
        :type xticks: tuple
        :param xlog: use logarithmic scale for x-axis
        :type xlog: bool
        """

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

    def add_dataset(self,dataset):
        """Add DataSet object."""

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
                self.ax = self.fig.add_subplot(111, projection='3d')
            self.initialised = True


    def plot(self):
        """Plot graphs."""

        if self.dimensions == 2:
            self.initialise_plot()
            for i,dataset in enumerate(self.datasets):
                if dataset.plot_type == 'scatter':
                    self.scatter_2d(dataset)
                elif dataset.plot_type == 'line':
                    self.line_2d(dataset)
                elif dataset.plot_type == 'error_bar':
                    self.errorbar_2d(dataset)
                elif dataset.plot_type == 'error_shade':
                    self.errorshade_2d(dataset)
                elif dataset.plot_type == 'bar':
                    self.bar_2d(dataset,i)
                elif dataset.plot_type == 'heat':
                    self.heat_2d(dataset)
                elif dataset.plot_type == 'contour':
                    self.contour_2d(dataset)
        elif self.dimensions == 3:
            self.initialise_plot()
            for dataset in self.datasets:
                if dataset.plot_type == 'scatter':
                    self.scatter_3d(dataset)
                elif dataset.plot_type == 'line':
                    self.line_3d(dataset)


    def scatter_2d(self,dataset):
        """Scatter graph in 2D"""

        if dataset.colour_map is None:
            self.ax.scatter(dataset.data[:,0], dataset.data[:,1], label=dataset.label, zorder=dataset.zorder,
                            marker=dataset.marker_style, s=dataset.marker_size,
                            color=dataset.colour)
        else:
            self.ax.scatter(dataset.data[:,0], dataset.data[:,1], label=dataset.label, zorder=dataset.zorder,
                            marker=dataset.marker_style, s=dataset.marker_size,
                            c=dataset.colour, cmap=dataset.colour_map, norm=dataset.colour_norm)


    def scatter_3d(self,dataset):
        """Scatter graph in 3D"""

        if dataset.colour_map is None:
            self.ax.scatter(dataset.data[:,0], dataset.data[:,1], dataset.data[:,2], label=dataset.label, zorder=dataset.zorder,
                            marker=dataset.marker_style, s=dataset.marker_size,
                            color=dataset.colour)
        else:
            self.ax.scatter(dataset.data[:,0], dataset.data[:,1], dataset.data[:,2], label=dataset.label, zorder=dataset.zorder,
                            marker=dataset.marker_style, s=dataset.marker_size,
                            c=dataset.colour, cmap=dataset.colour_map, norm=dataset.colour_norm)


    def line_2d(self,dataset):
        """Line graph in 2D"""

        self.ax.plot(dataset.data[:,0], dataset.data[:,1], label=dataset.label, zorder=dataset.zorder,
                      marker=dataset.marker_style, ms=dataset.marker_size,
                      lw=dataset.line_width, ls=dataset.line_style,
                      color=dataset.colour)


    def line_3d(self,dataset):
        """Line graph in 3D"""

        self.ax.plot(dataset.data[:,0], dataset.data[:,1], dataset.data[:,2], label=dataset.label, zorder=dataset.zorder,
                     marker=dataset.marker_style, ms=dataset.marker_size,
                     lw=dataset.line_width, ls=dataset.line_style,
                     color=dataset.colour)


    def errorbar_2d(self,dataset):
        """Line graph with symmetric errors in 2D"""

        self.ax.errorbar(dataset.data[:,0], dataset.data[:,1], xerr=dataset.error_x, yerr=dataset.error_y,
                     label= dataset.label, zorder=dataset.zorder,
                     marker=dataset.marker_style, ms=dataset.marker_size,
                     lw=dataset.line_width, ls=dataset.line_style,
                     color=dataset.colour)


    def errorshade_2d(self,dataset):
        """Line graph with shaded region indicating y error"""

        data = dataset.data
        y1 = data[:,1] - dataset.error_y
        y2 = data[:,1] + dataset.error_y
        self.ax.fill_between(data[:,0],y1=y1,y2=y2,label=dataset.label, zorder=dataset.zorder, color=dataset.colour)


    def bar_2d(self,dataset,shift):
        """Bar graph"""

        total_bw = dataset.bar_width
        bw = total_bw/self.num_datasets
        data = dataset.data
        data[:,0] = data[:,0] - total_bw/2 + bw/2 + shift*bw
        self.ax.bar(data[:,0],data[:,1],label=dataset.label,zorder=dataset.zorder,
                    width=bw,color=dataset.colour,
                    xerr=dataset.error_x,yerr=dataset.error_y,error_kw={'zorder':dataset.zorder+self.num_datasets})


    def heat_2d(self,dataset):
        """Heat map"""

        x = dataset.data[0]
        y = dataset.data[1]
        z = dataset.data[2]
        self.ax.imshow(z,origin="lower",cmap=dataset.colour_map,norm=dataset.colour_norm,aspect='auto',
                       extent=(np.min(x),np.max(x),np.min(y),np.max(y)),interpolation=dataset.surface_interpolation)


    def contour_2d(self,dataset):
        """Contour plot"""

        x = dataset.data[0]
        y = dataset.data[1]
        z = dataset.data[2]
        self.ax.contour(x, y, z,levels=dataset.contour_levels,cmap=dataset.colour_map,norm=dataset.colour_norm,
                        linewidths=dataset.line_width,linestyles=dataset.line_style)


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
            # Legend properties
            if self.legend:
                handles, labels = self.ax.get_legend_handles_labels()
                if self.legend_reverse:
                    handles = handles[::-1]
                    labels = labels[::-1]
                if self.legend_anchor is None:
                    legend = self.ax.legend(handles, labels, title=self.legend_title, ncol=self.legend_columns)
                else:
                    legend = self.ax.legend(handles, labels, title=self.legend_title, ncol=self.legend_columns,
                                             bbox_to_anchor=self.legend_anchor)
                legend.get_frame().set_edgecolor('grey')

            self.finalised = True


    ##### Save or visualise #####

    def display(self):
        """Display figure."""

        self.finalise_plot() # Apply final changes to plot
        plt.show()
        self.initialised = False
        self.finalised = False


    def save(self, name="plot", fmt="pdf", dpi_quality=400):
        """Save figure."""

        self.finalise_plot() # Apply final changes to plot
        filename = name+"."+fmt
        plt.savefig(filename, dpi=dpi_quality, bbox_inches="tight")


