"""
Matplotlib Themes Inspired by W.E.B. Du Bois

This module provides matplotlib style configurations that replicate
the aesthetic of Du Bois' original data visualizations.

Design Principles:
------------------
- Bold, saturated colors from a limited palette
- Clean, minimal styling
- Hand-drawn aesthetic (slightly irregular lines)
- Emphasis on data over decoration
- Typography inspired by turn-of-century design
- Generous whitespace
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
from typing import Dict, Optional
from dubois import colors as dubois_colors


# Du Bois theme parameters
DUBOIS_THEME = {
    # Figure
    'figure.facecolor': '#F5F5DC',      # Beige/cream background
    'figure.edgecolor': 'none',
    'figure.dpi': 100,
    
    # Axes
    'axes.facecolor': '#F5F5DC',        # Match figure background
    'axes.edgecolor': '#000000',        # Black borders
    'axes.linewidth': 1.5,              # Slightly heavier lines
    'axes.grid': False,                 # No grid by default
    'axes.axisbelow': True,             # Grid behind data
    'axes.labelsize': 11,
    'axes.labelweight': 'normal',
    'axes.labelcolor': '#000000',
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
    'axes.titlepad': 15,
    'axes.spines.left': True,
    'axes.spines.bottom': True,
    'axes.spines.top': False,           # No top spine
    'axes.spines.right': False,         # No right spine
    
    # Color cycle - Du Bois categorical palette
    'axes.prop_cycle': mpl.cycler(color=dubois_colors.DUBOIS_CATEGORICAL_8),
    
    # Grid
    'grid.color': '#CCCCCC',
    'grid.linestyle': '-',
    'grid.linewidth': 0.5,
    'grid.alpha': 0.5,
    
    # Ticks
    'xtick.major.size': 6,
    'xtick.minor.size': 3,
    'xtick.major.width': 1.0,
    'xtick.minor.width': 0.5,
    'xtick.direction': 'out',
    'xtick.color': '#000000',
    'xtick.labelsize': 10,
    
    'ytick.major.size': 6,
    'ytick.minor.size': 3,
    'ytick.major.width': 1.0,
    'ytick.minor.width': 0.5,
    'ytick.direction': 'out',
    'ytick.color': '#000000',
    'ytick.labelsize': 10,
    
    # Lines
    'lines.linewidth': 2.5,             # Thicker lines like hand-drawn
    'lines.markersize': 8,
    'lines.markeredgewidth': 0,
    'lines.solid_capstyle': 'round',    # Rounded line caps
    
    # Patches (bars, etc.)
    'patch.linewidth': 1.0,
    'patch.facecolor': dubois_colors.crimson,
    'patch.edgecolor': '#000000',
    'patch.force_edgecolor': True,
    
    # Font
    'font.family': 'serif',
    'font.serif': ['Georgia', 'Times New Roman', 'DejaVu Serif'],
    'font.size': 10,
    
    # Legend
    'legend.frameon': True,
    'legend.framealpha': 1.0,
    'legend.facecolor': '#F5F5DC',
    'legend.edgecolor': '#000000',
    'legend.fancybox': False,
    'legend.fontsize': 9,
    'legend.title_fontsize': 10,
    
    # Saving
    'savefig.dpi': 300,
    'savefig.facecolor': '#F5F5DC',
    'savefig.edgecolor': 'none',
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1,
}

# Alternative theme with white background (more modern)
DUBOIS_MODERN = {
    **DUBOIS_THEME,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'legend.facecolor': 'white',
    'savefig.facecolor': 'white',
}

# Minimalist theme (even cleaner)
DUBOIS_MINIMAL = {
    **DUBOIS_THEME,
    'axes.spines.left': False,
    'axes.spines.bottom': False,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0,
    'xtick.major.size': 0,
    'ytick.major.size': 0,
}


# Store original rcParams for reset
_original_params = None


def set_theme(theme: str = 'classic', context: str = 'notebook') -> None:
    """
    Apply a Du Bois-inspired theme to matplotlib.
    
    This function modifies matplotlib's global rcParams to match the
    aesthetic of W.E.B. Du Bois' data visualizations.
    
    Parameters
    ----------
    theme : str
        Theme variant to apply. Options:
        - 'classic': Cream background, traditional Du Bois aesthetic (default)
        - 'modern': White background, cleaner modern interpretation
        - 'minimal': Ultra-minimal, no spines or ticks
    context : str
        Context for scaling. Options:
        - 'notebook': For Jupyter notebooks (default)
        - 'paper': For publications
        - 'talk': For presentations
        - 'poster': For large posters
    
    Examples
    --------
    >>> import dubois
    >>> dubois.set_theme()  # Apply classic Du Bois theme
    >>> dubois.set_theme('modern', 'talk')  # Modern theme for presentations
    
    Notes
    -----
    This modifies matplotlib's global settings. Use reset_theme() to restore
    original settings.
    """
    global _original_params
    
    # Save original params if not already saved
    if _original_params is None:
        _original_params = mpl.rcParams.copy()
    
    # Select theme
    themes = {
        'classic': DUBOIS_THEME,
        'modern': DUBOIS_MODERN,
        'minimal': DUBOIS_MINIMAL,
    }
    
    if theme not in themes:
        raise ValueError(f"Unknown theme '{theme}'. Choose from: {list(themes.keys())}")
    
    theme_params = themes[theme]
    
    # Apply context scaling
    scale_factors = {
        'notebook': 1.0,
        'paper': 0.8,
        'talk': 1.3,
        'poster': 1.6,
    }
    
    if context not in scale_factors:
        raise ValueError(f"Unknown context '{context}'. Choose from: {list(scale_factors.keys())}")
    
    scale = scale_factors[context]
    
    # Apply theme
    mpl.rcParams.update(theme_params)
    
    # Apply scaling to font sizes
    if scale != 1.0:
        font_params = [
            'font.size', 'axes.labelsize', 'axes.titlesize',
            'xtick.labelsize', 'ytick.labelsize',
            'legend.fontsize', 'legend.title_fontsize'
        ]
        for param in font_params:
            if param in mpl.rcParams:
                mpl.rcParams[param] = mpl.rcParams[param] * scale
        
        # Scale line widths slightly
        mpl.rcParams['lines.linewidth'] *= scale ** 0.5
        mpl.rcParams['axes.linewidth'] *= scale ** 0.5


def reset_theme() -> None:
    """
    Reset matplotlib to its original settings.
    
    This undoes any changes made by set_theme().
    
    Examples
    --------
    >>> import dubois
    >>> dubois.set_theme()
    >>> # ... make plots ...
    >>> dubois.reset_theme()  # Restore original matplotlib settings
    """
    global _original_params
    
    if _original_params is not None:
        mpl.rcParams.update(_original_params)
        _original_params = None
    else:
        # Fallback: restore matplotlib defaults
        mpl.rcParams.update(mpl.rcParamsDefault)


def list_themes() -> list:
    """
    List available Du Bois themes.
    
    Returns
    -------
    list
        List of available theme names
    
    Examples
    --------
    >>> import dubois
    >>> dubois.list_themes()
    ['classic', 'modern', 'minimal']
    """
    return ['classic', 'modern', 'minimal']


def get_theme_params(theme: str = 'classic') -> Dict:
    """
    Get the rcParams dictionary for a theme without applying it.
    
    Useful for inspecting or modifying theme parameters before applying.
    
    Parameters
    ----------
    theme : str
        Theme name
    
    Returns
    -------
    Dict
        Dictionary of matplotlib rcParams
    
    Examples
    --------
    >>> import dubois
    >>> params = dubois.themes.get_theme_params('classic')
    >>> params['figure.facecolor']
    '#F5F5DC'
    """
    themes = {
        'classic': DUBOIS_THEME,
        'modern': DUBOIS_MODERN,
        'minimal': DUBOIS_MINIMAL,
    }
    
    if theme not in themes:
        raise ValueError(f"Unknown theme '{theme}'. Choose from: {list(themes.keys())}")
    
    return themes[theme].copy()


def dubois_style():
    """
    Context manager for temporarily applying Du Bois style.
    
    Use with Python's `with` statement to apply the style only within
    a specific code block.
    
    Returns
    -------
    context manager
        Matplotlib style context
    
    Examples
    --------
    >>> import dubois
    >>> import matplotlib.pyplot as plt
    >>> 
    >>> with dubois.themes.dubois_style():
    >>>     plt.plot([1, 2, 3], [1, 2, 3])
    >>>     plt.show()
    """
    return plt.style.context(DUBOIS_THEME)


class DuBoisStyle:
    """
    Context manager class for Du Bois styling.
    
    This is an alternative interface to dubois_style() that provides
    more control over theme selection.
    
    Parameters
    ----------
    theme : str
        Theme variant
    context : str
        Scaling context
    
    Examples
    --------
    >>> import dubois
    >>> import matplotlib.pyplot as plt
    >>> 
    >>> with DuBoisStyle('modern', 'talk'):
    >>>     plt.plot([1, 2, 3], [1, 2, 3])
    >>>     plt.title("My Plot")
    >>>     plt.show()
    """
    
    def __init__(self, theme: str = 'classic', context: str = 'notebook'):
        self.theme = theme
        self.context = context
        self.original_params = None
    
    def __enter__(self):
        # Save current params
        self.original_params = mpl.rcParams.copy()
        # Apply theme
        set_theme(self.theme, self.context)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Restore original params
        if self.original_params is not None:
            mpl.rcParams.update(self.original_params)


__all__ = [
    # Theme dictionaries
    'DUBOIS_THEME',
    'DUBOIS_MODERN',
    'DUBOIS_MINIMAL',
    # Functions
    'set_theme',
    'reset_theme',
    'list_themes',
    'get_theme_params',
    'dubois_style',
    # Classes
    'DuBoisStyle',
]
