import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize


class DataSet:
    """
    Holds data set and associated plot options. 
    """

    # Static variables to set different automatic styles for colours, markers etc.
    auto_id = 0
    auto_markers = mpl.markers.MarkerStyle().filled_markers
    auto_colours = plt.cm.get_cmap('Set1')


    def __init__(self,data,**kwargs):
        """
        Data as numpy array. Format depends on plot type but usually (n_points,2) for 2D plot and (n_points,3) for 3D plot.
        Can specifiy plot options through kwargs now, or later through setters.
        
        :param data: x,y,(z) data
        :type data: np.ndarray
        :param error_y: symmetric errors in given direction
        :type error_y: np.ndarray with n_points
        :param error_width: width of error bars 
        :type error_width: float
        :param error_interval: errors every n points 
        :type error_interval: int
        :param error_cap: error cap size 
        :type error_cap: int 
        :param plot: type of plot (line, scatter, bar ,error_bar, error_shade, heat, contour)
        :type plot: str
        :param label: data label for legend
        :type label: str
        :param order: ordering of overlaid datasets, higher number on top
        :type order: int
        :param line_style: line style (-,--,:,etc.)
        :type line_style: str
        :param line_width, int: line width
        :type line_width: float
        :param marker_style: marker style
        :type marker_style: int
        :param marker_size: fixed size for marker or array of sizes
        :type marker_size: float or np.ndarray
        :param bar_width: width of each bar in bar graph
        :type bar_width: float
        :param contour_levels: specified levels to draw contours
        :type contour_levels: np.ndarray
        :param contour_number: number of contours to draw if levels not supplied
        :type contour_number: int
        :param contour_limits: lower and upper bounds for contours
        :type contour_limits: tuple
        :param colour: colour code for all data points or array of floats if using colour map
        :type colour: str or np.ndarray
        :param colour_map: colour map 
        :type colour_map: str 
        :param colour_norm: normalisation condition for colour map
        :type colour_norm: tuple
        :param surface_interpolation: interpolation type for surface plots
        :type surface_interpolation: str
        """

        # Data
        self.id = self.__class__.auto_id # Set id for default properties
        self.data = np.array(data) # Ensure data stored as numpy array
        self.label = kwargs.get('label','data_{}'.format(self.id)) # Label for legend
        self.zorder = kwargs.get('order',self.id) # Overlay order - default in order created

        # Choose suitable default plot type or get user choice
        default_plot_type = 'line'
        self.plot_type = kwargs.get('plot',default_plot_type)

        # Errors
        self.error_x = kwargs.get('error_x',None)
        self.error_y = kwargs.get('error_y',None)
        error_width = kwargs.get('error_width',None)
        error_interval = kwargs.get('error_interval',1)
        error_cap = kwargs.get('error_cap',1)
        self.set_error(width=error_width,interval=error_interval,cap=error_cap)

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
        line_width = kwargs.get('line_width',2)
        self.set_line(style=line_style,width=line_width)

        # Bar
        bar_width = kwargs.get('bar_width',1)
        self.set_bar(width=bar_width)

        # Colours
        colour = kwargs.get('colour',None) # Colour or array of floats
        colour_map = kwargs.get('colour_map',None)
        colour_norm = kwargs.get('colour_norm',None) # Normalisation bounds
        self.set_colour(colour=colour,map=colour_map,norm=colour_norm)

        # Surface
        self.surface_interpolation = kwargs.get('surface_interpolation',None)

        # Contours
        contour_levels = kwargs.get('contour_levels',None)
        contour_number = kwargs.get('contour_number',10)
        contour_limits = kwargs.get('contour_limits',None)
        self.set_contours(levels=contour_levels,number=contour_number,limits=contour_limits)

        # Increment unique id
        self.__class__.auto_id += 1


    def set_line(self,style='-',width=2):
        """Set line style and width."""

        self.line_style = style
        self.line_width = width


    def set_bar(self,width=1):
        """Set bar width."""

        self.bar_width = width


    def set_marker(self,style=None,size=10):
        """Set marker style and size."""

        if style is None:
            if isinstance(size,np.ndarray):
                self.marker_style = self.__class__.auto_markers[self.id]
            elif size>0:
                self.marker_style = self.__class__.auto_markers[self.id]
            else:
                self.marker_style = None
        else:
            self.marker_style = style
        self.marker_size = size


    def set_error(self,width=None,interval=1,cap=1):
        """Set error width, interval and capsize"""

        self.error_width = width
        self.error_interval = interval
        self.error_cap = cap


    def set_contours(self,levels=None,number=10,limits=None):
        """Set contour properties."""

        # User defined levels take precedence, otherwise generate from data
        if levels is not None:
            self.contour_levels = levels
        else:
            if limits is not None:
                self.contour_levels=np.linspace(limits[0],limits[1],number)
            else:
                self.contour_levels=np.linspace(np.min(self.data[2]),np.max(self.data[2]),number)


    def set_colour(self,colour=None,map=None,norm=None):
        """Set colour as individual or map."""

        # Require normalised colour map for certain plots
        if self.plot_type == 'heat' or self.plot_type == 'contour' or self.plot_type == 'surface_mesh' or self.plot_type == 'surface_points':
            if map is not None:
                self.colour_map = map
            else:
                self.colour_map = 'coolwarm'
            if norm is None:
                self.colour_norm = Normalize(vmin=np.min(self.data[2]),vmax=np.max(self.data[2]))
            else:
                self.colour_norm = Normalize(vmin=norm[0],vmax=norm[1])
            return

        # No colour use map
        if colour is None:
            # No map use automatic map
            if map is not None:
                self.__class__.auto_colours = plt.cm.get_cmap(map)
            self.colour = self.__class__.auto_colours(self.id)
            self.colour_map = None
        # Use single colour
        elif isinstance(colour,str):
            self.colour = colour
            self.colour_map = None
        # Use colour map with normalisation and colours as array of floats
        elif isinstance(colour,np.ndarray):
            self.colour = colour
            if map is not None:
                self.colour_map = map
            else:
                self.colour_map = 'coolwarm'
            if norm is None:
                self.colour_norm = Normalize(vmin=np.min(self.colour),vmax=np.max(self.colour))
            else:
                self.colour_norm = Normalize(vmin=norm[0],vmax=norm[1])


