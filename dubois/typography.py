"""
Du Bois Typography Utilities

Helpers for applying W.E.B. Du Bois' distinctive text styling to
matplotlib visualizations. Du Bois' original plates featured:

- ALL CAPS titles in bold serif fonts
- Centered, hierarchical title blocks
- Descriptive subtitles in italic
- Sparse, purposeful annotations
- Period-appropriate language and phrasing

These utilities make it easy to apply that typographic style
consistently across charts.
"""

import matplotlib.pyplot as plt
import matplotlib.axes
from typing import Optional, Tuple


# Default styling constants
TITLE_SIZE = 16
SUBTITLE_SIZE = 11
CAPTION_SIZE = 9
ANNOTATION_SIZE = 10

__all__ = [
    'TITLE_SIZE', 'SUBTITLE_SIZE', 'CAPTION_SIZE', 'ANNOTATION_SIZE',
    'title_block', 'annotate', 'source_note', 'format_label', 'plate_number',
]


def title_block(ax: matplotlib.axes.Axes,
                title: str,
                subtitle: str = '',
                caption: str = '',
                title_size: float = TITLE_SIZE,
                subtitle_size: float = SUBTITLE_SIZE,
                caption_size: float = CAPTION_SIZE) -> None:
    """
    Add a Du Bois-style hierarchical title block to an axes.

    Creates a centered, multi-line title in the style of Du Bois'
    original plate headers: bold uppercase title, italic subtitle,
    and an optional smaller caption.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes to add the title block to.
    title : str
        Main title text (will be uppercased).
    subtitle : str, optional
        Subtitle text (displayed in italic).
    caption : str, optional
        Caption text (smaller, below subtitle).
    title_size : float
        Font size for the title.
    subtitle_size : float
        Font size for the subtitle.
    caption_size : float
        Font size for the caption.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> from dubois.typography import title_block
    >>> fig, ax = plt.subplots()
    >>> title_block(ax,
    ...     'City and Rural Population',
    ...     subtitle='Among American Negroes in the Former Slave States',
    ...     caption='Done by Atlanta University, 1900')
    """
    y_pos = 1.0

    # Main title — bold uppercase
    ax.text(0.5, y_pos + 0.08, title.upper(),
            transform=ax.transAxes,
            ha='center', va='bottom',
            fontsize=title_size, fontweight='bold',
            fontfamily='serif')

    # Subtitle — italic
    if subtitle:
        ax.text(0.5, y_pos + 0.02, subtitle,
                transform=ax.transAxes,
                ha='center', va='bottom',
                fontsize=subtitle_size, style='italic',
                fontfamily='serif')

    # Caption — smaller
    if caption:
        offset = -0.02 if subtitle else 0.02
        ax.text(0.5, y_pos + offset, caption,
                transform=ax.transAxes,
                ha='center', va='top',
                fontsize=caption_size,
                fontfamily='serif',
                color='#444444')


def annotate(ax: matplotlib.axes.Axes,
             text: str,
             xy: Tuple[float, float],
             xytext: Optional[Tuple[float, float]] = None,
             fontsize: float = ANNOTATION_SIZE,
             uppercase: bool = True,
             box: bool = True,
             arrow: bool = True,
             **kwargs) -> matplotlib.text.Annotation:
    """
    Add a Du Bois-style annotation to a chart.

    Creates annotations with bold text, optional box backgrounds,
    and clean arrow connectors.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes to annotate.
    text : str
        Annotation text.
    xy : tuple of (float, float)
        Point being annotated (data coordinates).
    xytext : tuple of (float, float), optional
        Position for the text. If None, places near xy.
    fontsize : float
        Font size for annotation text.
    uppercase : bool
        Whether to uppercase the text.
    box : bool
        Whether to draw a box around the text.
    arrow : bool
        Whether to draw an arrow from text to point.
    **kwargs
        Additional keyword arguments passed to ax.annotate.

    Returns
    -------
    matplotlib.text.Annotation

    Examples
    --------
    >>> from dubois.typography import annotate
    >>> annotate(ax, 'Emancipation', xy=(1865, 50),
    ...          xytext=(1855, 70))
    """
    if uppercase:
        text = text.upper()

    if xytext is None:
        xytext = (xy[0], xy[1] + (ax.get_ylim()[1] - ax.get_ylim()[0]) * 0.15)

    bbox_props = None
    if box:
        bbox_props = dict(
            boxstyle='round,pad=0.3',
            facecolor='white',
            edgecolor='#000000',
            linewidth=1.0,
            alpha=0.9,
        )

    arrowprops = None
    if arrow and xytext != xy:
        arrowprops = dict(
            arrowstyle='-|>',
            color='#000000',
            linewidth=1.2,
        )

    ann = ax.annotate(
        text, xy=xy, xytext=xytext,
        fontsize=fontsize, fontweight='bold',
        fontfamily='serif',
        ha='center', va='center',
        bbox=bbox_props,
        arrowprops=arrowprops,
        **kwargs,
    )
    return ann


def source_note(ax: matplotlib.axes.Axes,
                text: str,
                fontsize: float = 8) -> None:
    """
    Add a source/attribution note at the bottom of a chart.

    Du Bois' plates often included attribution text like
    "Done by Atlanta University" at the bottom.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes to add the note to.
    text : str
        Source or attribution text.
    fontsize : float
        Font size.

    Examples
    --------
    >>> from dubois.typography import source_note
    >>> source_note(ax, 'Done by Atlanta University, 1900')
    """
    ax.text(0.5, -0.08, text,
            transform=ax.transAxes,
            ha='center', va='top',
            fontsize=fontsize, style='italic',
            fontfamily='serif',
            color='#666666')


def format_label(text: str, uppercase: bool = True, wrap_width: int = 0) -> str:
    """
    Format a text label in Du Bois style.

    Parameters
    ----------
    text : str
        The text to format.
    uppercase : bool
        Whether to convert to uppercase (Du Bois convention).
    wrap_width : int
        Maximum characters per line. 0 for no wrapping.

    Returns
    -------
    str
        Formatted text string.

    Examples
    --------
    >>> format_label('proportion of freemen and slaves')
    'PROPORTION OF FREEMEN AND SLAVES'
    >>> format_label('a very long title that should wrap', wrap_width=20)
    'A VERY LONG TITLE\\nTHAT SHOULD WRAP'
    """
    if uppercase:
        text = text.upper()

    if wrap_width > 0:
        words = text.split()
        lines = []
        current_line = []
        current_len = 0

        for word in words:
            if current_len + len(word) + (1 if current_line else 0) > wrap_width:
                lines.append(' '.join(current_line))
                current_line = [word]
                current_len = len(word)
            else:
                current_line.append(word)
                current_len += len(word) + (1 if len(current_line) > 1 else 0)

        if current_line:
            lines.append(' '.join(current_line))

        text = '\n'.join(lines)

    return text


def plate_number(ax: matplotlib.axes.Axes,
                 number: int,
                 position: str = 'top-right',
                 fontsize: float = 10) -> None:
    """
    Add a plate number label in the style of Du Bois' original exhibition.

    The original plates were numbered (e.g., "Plate 11", "Plate 31").

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes to label.
    number : int
        Plate number.
    position : str
        Position: 'top-right', 'top-left', 'bottom-right', 'bottom-left'.
    fontsize : float
        Font size.

    Examples
    --------
    >>> from dubois.typography import plate_number
    >>> plate_number(ax, 11)
    """
    positions = {
        'top-right': (0.98, 0.98, 'right', 'top'),
        'top-left': (0.02, 0.98, 'left', 'top'),
        'bottom-right': (0.98, 0.02, 'right', 'bottom'),
        'bottom-left': (0.02, 0.02, 'left', 'bottom'),
    }

    if position not in positions:
        raise ValueError(f"Unknown position '{position}'. "
                         f"Choose from: {list(positions.keys())}")

    x, y, ha, va = positions[position]

    ax.text(x, y, f'PLATE {number}',
            transform=ax.transAxes,
            ha=ha, va=va,
            fontsize=fontsize,
            fontfamily='serif',
            fontweight='bold',
            color='#444444')
