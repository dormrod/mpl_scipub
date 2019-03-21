"""Helper functions and classes for styles and colours"""
import matplotlib.markers as markers


def get_marker_styles(sub_style='full'):
    """Get list of all marker styles"""

    if sub_style == 'all':
        styles = markers.MarkerStyle().markers
    elif sub_style == 'full':
        styles = markers.MarkerStyle().filled_markers
    return styles
