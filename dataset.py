import numpy as np
import matplotlib.pyplot as plt
from properties import get_marker_styles


class DataSet:
    """Holds data set and plotting properties"""

    # Static variables to set different automatic styles for colours, markers etc.
    auto_id = 0
    auto_markers = get_marker_styles()
    auto_colours = plt.cm.get_cmap('Set1')


    def __init__(self,data,**kwargs):
        """Initialise with data and plot properties"""

        # Get data
        self.id = self.__class__.auto_id # Set id for default properties
        self.data = np.array(data) # Ensure data stored as numpy array
        self.label = kwargs.get('label','data') # Label for legend

        # Unpack plot options
        self.plot_type = kwargs.get('plot','scatter') # Plot type
        self.zorder = kwargs.get('zorder',1) # Overlay order
        line_style = kwargs.get('line_style','-')
        line_width = kwargs.get('line_width',1)
        marker_style = kwargs.get('marker_style',None)
        marker_size = kwargs.get('marker_size',10) # Float or array of floats
        colour = kwargs.get('colour',None) # Colour or array of floats
        colour_map = kwargs.get('colour_map',None)

        # Set plot properties as default or from passed kwargs
        self.set_line(style=line_style,width=line_width)
        self.set_marker(style=marker_style,size=marker_size)
        self.set_colour(c=colour,map=colour_map)

        # Increment unique id
        self.__class__.auto_id += 1


    def set_line(self,style='-',width=1):
        """Set line style and width"""

        self.line_style = style
        self.line_width = width


    def set_marker(self,style=None,size=10):
        """Set marker style and size"""

        if style is None:
            self.marker_style = self.__class__.auto_markers[self.id]
        else:
            self.marker_style = style
        self.marker_size = size


    def set_colour(self,c=None,map=None):
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
        # Use colour map with array of floats
        elif isinstance(c,np.ndarray):
            self.colour = c
            if map is not None:
                self.colour_map = map
            else:
                self.colour_map = 'coolwarm'

