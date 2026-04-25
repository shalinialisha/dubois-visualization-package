"""
Du Bois-Style Butterfly (Mirror) Charts

Back-to-back comparison charts where two datasets are mirrored along a
central axis. Du Bois used this format to compare data between groups
or across time periods, creating a visually symmetric and compelling
display of comparative statistics.

Also known as: population pyramids, tornado charts, mirror charts.

Key Design Elements:
- Central category labels
- Bars extending left and right from center
- Bold contrasting colors for the two sides
- Value labels on bar ends
- Symmetric axis scaling
- No axis lines or ticks
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import List, Optional, Tuple
from dubois import colors as dubois_colors


def butterfly(categories: List[str],
              left_values: List[float],
              right_values: List[float],
              left_label: str = 'Left',
              right_label: str = 'Right',
              left_color: Optional[str] = None,
              right_color: Optional[str] = None,
              title: str = '',
              subtitle: str = '',
              value_labels: bool = True,
              label_format: str = '{:.0f}',
              symmetric: bool = True,
              bar_height: float = 0.7,
              figsize: Optional[Tuple[float, float]] = None,
              ax: Optional[plt.Axes] = None,
              **kwargs) -> Tuple[plt.Figure, plt.Axes]:
    """
    Create a Du Bois-style butterfly (mirror/back-to-back) chart.

    Parameters
    ----------
    categories : list of str
        Category labels displayed in the center.
    left_values : list of float
        Values for the left side of the chart.
    right_values : list of float
        Values for the right side of the chart.
    left_label : str
        Label for the left dataset.
    right_label : str
        Label for the right dataset.
    left_color : str, optional
        Color for left bars. Defaults to Du Bois crimson.
    right_color : str, optional
        Color for right bars. Defaults to Du Bois gold.
    title : str
        Chart title.
    subtitle : str
        Subtitle.
    value_labels : bool
        Whether to display value labels.
    label_format : str
        Format string for value labels.
    symmetric : bool
        Whether to use same scale for both sides.
    bar_height : float
        Height of bars (0-1).
    figsize : tuple, optional
        Figure size.
    ax : matplotlib.axes.Axes, optional
        Axes to draw on.
    **kwargs
        Additional keyword arguments passed to barh.

    Returns
    -------
    tuple of (Figure, Axes)
    """
    n = len(categories)

    if left_color is None:
        left_color = dubois_colors.crimson
    if right_color is None:
        right_color = dubois_colors.DUBOIS_EXTENDED['gold']

    if figsize is None:
        figsize = (12, max(5, n * 1.0))

    created_fig = ax is None
    if created_fig:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.figure

    edge_color = kwargs.pop('edgecolor', '#000000')
    line_width = kwargs.pop('linewidth', 1.5)

    y_pos = np.arange(n)
    left_arr = np.array(left_values, dtype=float)
    right_arr = np.array(right_values, dtype=float)

    # Draw left bars (negative direction)
    bars_left = ax.barh(y_pos, -left_arr, height=bar_height,
                        color=left_color, edgecolor=edge_color,
                        linewidth=line_width, label=left_label, **kwargs)

    # Draw right bars (positive direction)
    bars_right = ax.barh(y_pos, right_arr, height=bar_height,
                         color=right_color, edgecolor=edge_color,
                         linewidth=line_width, label=right_label, **kwargs)

    # Set axis limits
    left_max = max(left_arr) if len(left_arr) else 1
    right_max = max(right_arr) if len(right_arr) else 1
    if symmetric:
        max_val = max(left_max, right_max)
        margin = max_val * 0.25
        ax.set_xlim(-max_val - margin, max_val + margin)
    else:
        margin_l = left_max * 0.25
        margin_r = right_max * 0.25
        max_val = max(left_max, right_max)
        ax.set_xlim(-left_max - margin_l, right_max + margin_r)

    # Value labels
    if value_labels:
        for bar_rect, val in zip(bars_left, left_arr):
            ax.text(bar_rect.get_x() - max_val * 0.02,
                    bar_rect.get_y() + bar_rect.get_height() / 2,
                    label_format.format(val),
                    ha='right', va='center', fontweight='bold',
                    color='#000000', fontsize=11, fontfamily='serif')

        for bar_rect, val in zip(bars_right, right_arr):
            ax.text(bar_rect.get_width() + max_val * 0.02,
                    bar_rect.get_y() + bar_rect.get_height() / 2,
                    label_format.format(val),
                    ha='left', va='center', fontweight='bold',
                    color='#000000', fontsize=11, fontfamily='serif')

    # Category labels in center
    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories, ha='center', fontsize=12,
                       fontweight='bold', fontfamily='serif')
    ax.tick_params(axis='y', length=0, pad=45)
    ax.invert_yaxis()

    # Reserve room above the topmost bar for the side labels — explicit ylim
    # so this works in single-figure and multi-panel layouts identically.
    ax.set_ylim(n - 0.5, -1.4)

    # Draw center line
    ax.axvline(x=0, color='#000000', linewidth=1.5)

    # Side labels above the topmost bar — anchor each to its own side's
    # midpoint so an asymmetric chart still places them over the data.
    if symmetric:
        left_label_x = -max_val * 0.5
        right_label_x = max_val * 0.5
    else:
        left_label_x = -left_max * 0.5
        right_label_x = right_max * 0.5
    ax.text(left_label_x, -0.9, left_label.upper(),
            ha='center', va='center', fontsize=13,
            fontweight='bold', color=left_color, fontfamily='serif')
    ax.text(right_label_x, -0.9, right_label.upper(),
            ha='center', va='center', fontsize=13,
            fontweight='bold', color=right_color, fontfamily='serif')

    if title:
        ax.set_title(title.upper(), fontsize=16, fontweight='bold',
                     fontfamily='serif', pad=30)
    if subtitle:
        ax.text(0.5, 1.02, subtitle, transform=ax.transAxes,
                ha='center', va='bottom', fontsize=11,
                style='italic', fontfamily='serif')

    # Du Bois style: remove all chart chrome
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(axis='x', length=0)
    ax.set_xticklabels([])

    if created_fig:
        plt.tight_layout()
    return fig, ax


def comparison(categories: List[str],
               dataset_a: List[float],
               dataset_b: List[float],
               label_a: str = 'Group A',
               label_b: str = 'Group B',
               color_a: Optional[str] = None,
               color_b: Optional[str] = None,
               title: str = '',
               subtitle: str = '',
               value_labels: bool = True,
               label_format: str = '{:.0f}',
               figsize: Optional[Tuple[float, float]] = None,
               ax: Optional[plt.Axes] = None,
               **kwargs) -> Tuple[plt.Figure, plt.Axes]:
    """
    Create a Du Bois-style side-by-side dot comparison chart.

    An alternative to the butterfly chart that uses connected dots
    to show differences between two groups.

    Parameters
    ----------
    categories : list of str
        Category labels.
    dataset_a : list of float
        Values for first dataset.
    dataset_b : list of float
        Values for second dataset.
    label_a : str
        Label for first dataset.
    label_b : str
        Label for second dataset.
    color_a : str, optional
        Color for first dataset markers.
    color_b : str, optional
        Color for second dataset markers.
    title : str
        Chart title.
    subtitle : str
        Subtitle.
    figsize : tuple, optional
        Figure size.
    ax : matplotlib.axes.Axes, optional
        Axes to draw on.
    **kwargs
        Additional keyword arguments.

    Returns
    -------
    tuple of (Figure, Axes)
    """
    n = len(categories)

    if color_a is None:
        color_a = dubois_colors.crimson
    if color_b is None:
        color_b = dubois_colors.DUBOIS_EXTENDED['gold']

    if figsize is None:
        figsize = (10, max(5, n * 1.0 + 1))

    created_fig = ax is None
    if created_fig:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.figure

    y_pos = np.arange(n)

    # Draw connecting lines
    for i in range(n):
        ax.plot([dataset_a[i], dataset_b[i]], [y_pos[i], y_pos[i]],
                color='#CCCCCC', linewidth=3, zorder=1)

    # Draw dots
    ax.scatter(dataset_a, y_pos, color=color_a, s=150,
               edgecolors='#000000', linewidths=1.5,
               zorder=2, label=label_a)
    ax.scatter(dataset_b, y_pos, color=color_b, s=150,
               edgecolors='#000000', linewidths=1.5,
               zorder=2, label=label_b)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories, fontsize=12, fontweight='bold',
                       fontfamily='serif')
    ax.invert_yaxis()

    # Add x padding so dots and value labels aren't clipped
    all_vals = list(dataset_a) + list(dataset_b)
    x_min, x_max = min(all_vals), max(all_vals)
    span = (x_max - x_min) if x_max > x_min else max(abs(x_max), 1)
    x_pad = span * 0.20
    ax.set_xlim(x_min - x_pad, x_max + x_pad)

    if value_labels:
        offset = span * 0.02
        for i in range(n):
            a, b = dataset_a[i], dataset_b[i]
            # Anchor each value on the outside of its dot so they don't
            # collide with the connecting line or each other.
            if a <= b:
                ax.text(a - offset, y_pos[i], label_format.format(a),
                        ha='right', va='center', fontweight='bold',
                        fontsize=10, fontfamily='serif', color=color_a)
                ax.text(b + offset, y_pos[i], label_format.format(b),
                        ha='left', va='center', fontweight='bold',
                        fontsize=10, fontfamily='serif', color=color_b)
            else:
                ax.text(a + offset, y_pos[i], label_format.format(a),
                        ha='left', va='center', fontweight='bold',
                        fontsize=10, fontfamily='serif', color=color_a)
                ax.text(b - offset, y_pos[i], label_format.format(b),
                        ha='right', va='center', fontweight='bold',
                        fontsize=10, fontfamily='serif', color=color_b)

    if title:
        ax.set_title(title.upper(), fontsize=16, fontweight='bold',
                     fontfamily='serif', pad=20)
    if subtitle:
        ax.text(0.5, 1.02, subtitle, transform=ax.transAxes,
                ha='center', va='bottom', fontsize=11,
                style='italic', fontfamily='serif')

    ax.legend(frameon=True, edgecolor='black', fancybox=False,
              loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=11)

    # Du Bois style: minimal chrome
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(axis='both', length=0)
    ax.set_xticklabels([])

    if created_fig:
        plt.tight_layout()
    return fig, ax
