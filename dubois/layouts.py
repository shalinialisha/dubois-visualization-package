"""
Du Bois Multi-Panel Layout System

Utilities for composing multiple Du Bois charts into cohesive
multi-panel figures that replicate the complex plate designs from
the 1900 Paris Exposition.

Du Bois' original plates often combined:
- A large main visualization
- Title blocks with hierarchical text
- Multiple sub-panels for comparison
- Consistent color and typography across panels
"""

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib as mpl
from typing import List, Optional, Tuple, Dict, Union
from dubois import colors as dubois_colors
from dubois.themes import set_theme, reset_theme

__all__ = ['DuBoisPlate', 'plate_layout']


class DuBoisPlate:
    """
    A multi-panel layout builder for creating Du Bois-style plates.

    This class provides a structured way to compose multiple charts
    into a single figure with consistent styling, similar to Du Bois'
    original exposition plates.

    Parameters
    ----------
    nrows : int
        Number of rows in the grid.
    ncols : int
        Number of columns in the grid.
    title : str
        Plate title (displayed at top in Du Bois style).
    subtitle : str
        Plate subtitle.
    theme : str
        Du Bois theme to apply ('classic', 'modern', 'minimal').
    figsize : tuple, optional
        Figure size.
    plate_number : int, optional
        Plate number to display.

    Examples
    --------
    >>> from dubois.layouts import DuBoisPlate
    >>> plate = DuBoisPlate(2, 2, title='Negro Population')
    >>> ax1 = plate.get_axes(0, 0)
    >>> ax2 = plate.get_axes(0, 1)
    >>> # ... draw on each axes ...
    >>> plate.show()
    """

    def __init__(self,
                 nrows: int = 1,
                 ncols: int = 1,
                 title: str = '',
                 subtitle: str = '',
                 theme: str = 'classic',
                 figsize: Optional[Tuple[float, float]] = None,
                 plate_number: Optional[int] = None):
        self.nrows = nrows
        self.ncols = ncols
        self.title = title
        self.subtitle = subtitle
        self.theme = theme
        self.plate_number = plate_number

        if figsize is None:
            figsize = (ncols * 6, nrows * 5 + 1.5)

        # Apply theme
        set_theme(theme)

        # Create figure with gridspec
        self.fig = plt.figure(figsize=figsize)

        # Reserve top space for title block
        title_height = 0.12 if title else 0.02
        self.gs = gridspec.GridSpec(
            nrows, ncols,
            figure=self.fig,
            top=1.0 - title_height,
            bottom=0.05,
            left=0.08,
            right=0.95,
            hspace=0.35,
            wspace=0.3,
        )

        self._axes = {}

        # Add title block
        if title:
            self.fig.text(0.5, 1.0 - title_height / 3,
                          title.upper(),
                          ha='center', va='center',
                          fontsize=16, fontweight='bold',
                          fontfamily='serif')
        if subtitle:
            self.fig.text(0.5, 1.0 - title_height * 0.75,
                          subtitle,
                          ha='center', va='center',
                          fontsize=11, style='italic',
                          fontfamily='serif')
        if plate_number is not None:
            self.fig.text(0.95, 0.98, f'PLATE {plate_number}',
                          ha='right', va='top',
                          fontsize=9, fontweight='bold',
                          fontfamily='serif',
                          color='#444444')

    def get_axes(self, row: int, col: int,
                 rowspan: int = 1, colspan: int = 1) -> plt.Axes:
        """
        Get a matplotlib Axes for a specific panel position.

        Parameters
        ----------
        row : int
            Row index (0-based).
        col : int
            Column index (0-based).
        rowspan : int
            Number of rows this panel spans.
        colspan : int
            Number of columns this panel spans.

        Returns
        -------
        matplotlib.axes.Axes
        """
        key = (row, col, rowspan, colspan)
        if key not in self._axes:
            gs_slice = self.gs[row:row + rowspan, col:col + colspan]
            ax = self.fig.add_subplot(gs_slice)
            self._axes[key] = ax
        return self._axes[key]

    def add_panel_title(self, row: int, col: int, text: str,
                        fontsize: float = 12) -> None:
        """
        Add a title to a specific panel.

        Parameters
        ----------
        row : int
            Row index.
        col : int
            Column index.
        text : str
            Panel title text.
        fontsize : float
            Font size.
        """
        ax = self.get_axes(row, col)
        ax.set_title(text.upper(), fontsize=fontsize,
                     fontweight='bold', pad=10)

    def save(self, path: str, dpi: int = 300, **kwargs) -> None:
        """
        Save the plate to a file.

        Parameters
        ----------
        path : str
            Output file path.
        dpi : int
            Resolution in dots per inch.
        **kwargs
            Additional kwargs passed to fig.savefig.
        """
        self.fig.savefig(path, dpi=dpi, bbox_inches='tight', **kwargs)

    def show(self) -> None:
        """Display the plate."""
        plt.show()

    def close(self) -> None:
        """Close the figure and reset theme."""
        plt.close(self.fig)
        reset_theme()

    @property
    def figure(self) -> plt.Figure:
        """The matplotlib Figure object."""
        return self.fig


def plate_layout(panels: List[dict],
                 title: str = '',
                 subtitle: str = '',
                 theme: str = 'classic',
                 figsize: Optional[Tuple[float, float]] = None) -> Tuple[plt.Figure, List[plt.Axes]]:
    """
    Create a multi-panel plate from a list of panel specifications.

    A simpler functional interface for creating multi-panel layouts
    without using the DuBoisPlate class directly.

    Parameters
    ----------
    panels : list of dict
        Each dict describes a panel with keys:
        - 'position': (row, col) or (row, col, rowspan, colspan)
        - 'title': optional panel title
    title : str
        Plate title.
    subtitle : str
        Plate subtitle.
    theme : str
        Du Bois theme.
    figsize : tuple, optional
        Figure size.

    Returns
    -------
    tuple of (Figure, list of Axes)

    Examples
    --------
    >>> from dubois.layouts import plate_layout
    >>> fig, axes = plate_layout(
    ...     [{'position': (0, 0), 'title': 'Chart A'},
    ...      {'position': (0, 1), 'title': 'Chart B'},
    ...      {'position': (1, 0, 1, 2), 'title': 'Full Width Chart'}],
    ...     title='Negro Population Statistics',
    ... )
    >>> # axes[0], axes[1], axes[2] are ready for drawing
    """
    # Determine grid size from panel positions
    max_row = 0
    max_col = 0
    for panel in panels:
        pos = panel['position']
        row, col = pos[0], pos[1]
        rowspan = pos[2] if len(pos) > 2 else 1
        colspan = pos[3] if len(pos) > 3 else 1
        max_row = max(max_row, row + rowspan)
        max_col = max(max_col, col + colspan)

    plate = DuBoisPlate(
        nrows=max_row,
        ncols=max_col,
        title=title,
        subtitle=subtitle,
        theme=theme,
        figsize=figsize,
    )

    axes_list = []
    for panel in panels:
        pos = panel['position']
        row, col = pos[0], pos[1]
        rowspan = pos[2] if len(pos) > 2 else 1
        colspan = pos[3] if len(pos) > 3 else 1

        ax = plate.get_axes(row, col, rowspan, colspan)

        if 'title' in panel:
            ax.set_title(panel['title'].upper(),
                         fontsize=12, fontweight='bold', pad=10)

        axes_list.append(ax)

    return plate.figure, axes_list
