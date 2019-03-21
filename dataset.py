import numpy as np
from properties import get_marker_styles


class DataSet:
    """Holds data set and plotting properties"""

    # Static variables to set different automatic styles for colours, markers etc.
    auto_id = 0
    auto_markers = get_marker_styles()


    def __init__(self,data,**kwargs):
        """Initialise with data and plot properties"""

        self.id = self.__class__.auto_id # Set id for default properties
        self.data = np.array(data) # Ensure data stored as numpy array
        self.plot_type = kwargs.get('plot','scatter') # Plot type
        self.zorder = kwargs.get('zorder',1) # Overlay order
        self.label = kwargs.get('label','data') # Label for legend
        self.colour = kwargs.get('colour','k') # Colour of points/line
        self.set_line() # Default line properties
        self.set_marker() # Default marker properties
        self.__class__.auto_id += 1 # Increment unqie id


    def set_line(self,style='-',width=1):
        """Set line style and width"""

        self.line_style = style
        self.line_width = width


    def set_marker(self,style=None,size=5):
        """Set marker style and size"""

        if style is None:
            self.marker_style = self.__class__.auto_markers[self.id]
        else:
            self.marker_style = style
        self.marker_size = size
