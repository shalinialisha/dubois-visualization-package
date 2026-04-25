"""
dubois-viz: W.E.B. Du Bois-Inspired Data Visualizations
========================================================

A Python package for creating data visualizations inspired by W.E.B. Du Bois'
groundbreaking data portraits from the 1900 Paris Exposition.

Quick Start
-----------
>>> import dubois
>>>
>>> # Use Du Bois colors
>>> dubois.colors.crimson
>>>
>>> # Apply Du Bois theme to matplotlib
>>> dubois.set_theme()
>>>
>>> # Get a color palette
>>> palette = dubois.colors.get_categorical(4)
>>>
>>> # Build a Du Bois-style chart
>>> from dubois.charts import bar
>>> fig, ax = bar.bar(['A', 'B', 'C'], [10, 20, 30], title='Demo')

Modules
-------
colors
    Color palettes and color utilities
themes
    Matplotlib style themes inspired by Du Bois
charts
    Specialized chart types: bar, area, butterfly, spiral, wrapped, pictorial
typography
    Title blocks, annotations, source notes, plate numbering
layouts
    Multi-panel plate composition (DuBoisPlate)

Historical Context
------------------
W.E.B. Du Bois and his team at Atlanta University created 63 innovative
data visualizations for the "American Negro" exhibit at the 1900 Paris
Exposition. These hand-painted charts used bold colors, creative chart
types, and compelling narratives to challenge racist assumptions and
demonstrate Black American progress since emancipation.

More information:
- Library of Congress Collection: https://www.loc.gov/collections/african-american-photographs-1900-paris-exposition/
- #DuBoisChallenge: https://github.com/ajstarks/dubois-data-portraits
"""

__version__ = '1.0.0'
__author__ = 'Shalini Thinakaran'

# Import main modules
from dubois import colors
from dubois import themes
from dubois import charts
from dubois import typography
from dubois import layouts

# Import key functions for convenience
from dubois.themes import set_theme, reset_theme, list_themes
from dubois.colors import (
    get_palette,
    get_sequential,
    get_categorical,
    get_diverging,
)

# Define what gets imported with "from dubois import *"
__all__ = [
    # Version info
    '__version__',
    # Modules
    'colors',
    'themes',
    'charts',
    'typography',
    'layouts',
    # Key functions
    'set_theme',
    'reset_theme',
    'list_themes',
    'get_palette',
    'get_sequential',
    'get_categorical',
    'get_diverging',
]
