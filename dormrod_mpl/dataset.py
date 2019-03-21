import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize


class DataSet:
    """Holds data set and plotting properties"""

    # Static variables to set different automatic styles for colours, markers etc.
    auto_id = 0
    auto_markers = mpl.markers.MarkerStyle().filled_markers
    auto_colours = plt.cm.get_cmap('Set1')


    def __init__(self,data,**kwargs):
        """Initialise with data and plot properties"""

        # Data
        self.id = self.__class__.auto_id # Set id for default properties
        self.data = np.array(data) # Ensure data stored as numpy array
        self.label = kwargs.get('label','data') # Label for legend
        self.zorder = kwargs.get('order',self.id) # Overlay order - default in order created

        # Data errors
        self.error_x = kwargs.get('error_x',None)
        self.error_y = kwargs.get('error_y',None)
        self.error_style = kwargs.get('error_style','bar')

        # Choose suitable default plot type or get user choice
        if isinstance(self.error_x,np.ndarray) or isinstance(self.error_y,np.ndarray):
            if self.error_style == 'bar':
                default_plot_type = 'error_bar'
            else:
                default_plot_type = 'error_shade'
        else:
            default_plot_type = 'line'
        self.plot_type = kwargs.get('plot',default_plot_type)

        # Markers
        if self.plot_type == 'scatter':
            default_marker_size = 10
        else:
            default_marker_size = 0
        marker_style = kwargs.get('marker_style',None)
        marker_size = kwargs.get('marker_size',default_marker_size) # Float or array of floats
        self.set_marker(style=marker_style,size=marker_size)

        # Line
        line_style = kwargs.get('line_style','-')
        line_width = kwargs.get('line_width',1)
        self.set_line(style=line_style,width=line_width)

        # Bar
        bar_width = kwargs.get('bar_width',1)
        self.set_bar(width=bar_width)

        # Colours
        colour = kwargs.get('colour',None) # Colour or array of floats
        colour_map = kwargs.get('colour_map',None)
        colour_norm = kwargs.get('colour_norm',None) # Normalisation bounds
        self.set_colour(c=colour,map=colour_map,norm=colour_norm)

        # Increment unique id
        self.__class__.auto_id += 1


    def set_line(self,style='-',width=1):
        """Set line style and width"""

        self.line_style = style
        self.line_width = width


    def set_bar(self,width=1):
        """Set bar width"""

        self.bar_width = width


    def set_marker(self,style=None,size=10):
        """Set marker style and size"""

        if style is None:
            if size>0:
                self.marker_style = self.__class__.auto_markers[self.id]
            else:
                self.marker_style = None
        else:
            self.marker_style = style
        self.marker_size = size


    def set_colour(self,c=None,map=None,norm=None):
        """Set as individual colour or map"""

        # No colour use map
        if c is None:
            # No map use automatic map
            if map is not None:
                self.__class__.auto_colours = plt.cm.get_cmap(map)
            self.colour = self.__class__.auto_colours(self.id)
            self.colour_map = None
        # Use single colour
        elif isinstance(c,str):
            self.colour = c
            self.colour_map = None
        # Use colour map with normalisation and colours as array of floats
        elif isinstance(c,np.ndarray):
            self.colour = c
            if map is not None:
                self.colour_map = map
            else:
                self.colour_map = 'coolwarm'
            if norm is None:
                self.colour_norm = Normalize(vmin=np.min(self.colour),vmax=np.max(self.colour))
            else:
                self.colour_norm = Normalize(vmin=norm[0],vmax=norm[1])


