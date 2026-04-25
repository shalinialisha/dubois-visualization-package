"""
Du Bois-Style Pictorial (Icon Grid) Charts

Grid-based pictograph visualizations where each icon/symbol represents
a unit of data. Du Bois used grid layouts to represent population counts
and proportions, filling squares in a grid with different colors to show
the ratio between groups.

Key Design Elements:
- Regular grid of squares or circles
- Each cell represents a fixed unit (e.g., 1% or 1,000 people)
- Color-coded by category
- Clean black borders on each cell
- Reading order: left-to-right, top-to-bottom
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from typing import List, Optional, Tuple, Dict
from dubois import colors as dubois_colors


def icon_grid(groups: Dict[str, float],
              colors: Optional[List[str]] = None,
              total: int = 100,
              ncols: int = 10,
              shape: str = 'square',
              title: str = '',
              subtitle: str = '',
              cell_size: float = 0.4,
              cell_gap: float = 0.05,
              show_legend: bool = True,
              figsize: Optional[Tuple[float, float]] = None,
              ax: Optional[plt.Axes] = None) -> Tuple[plt.Figure, plt.Axes]:
    """
    Create a Du Bois-style icon grid (waffle-style) chart.

    Each cell in the grid represents one unit. Cells are filled
    with colors proportional to each group's share.

    Parameters
    ----------
    groups : dict
        Dictionary mapping group names to values.
        Example: {'Illiterate': 44, 'Literate': 56}
    colors : list of str, optional
        Colors for each group.
    total : int
        Total number of cells in the grid (usually 100 for percentages).
    ncols : int
        Number of columns in the grid.
    shape : str
        Cell shape: 'square' or 'circle'.
    title : str
        Chart title.
    subtitle : str
        Subtitle.
    cell_size : float
        Size of each cell.
    cell_gap : float
        Gap between cells.
    show_legend : bool
        Whether to display a legend.
    figsize : tuple, optional
        Figure size.
    ax : matplotlib.axes.Axes, optional
        Axes to draw on.

    Returns
    -------
    tuple of (Figure, Axes)

    Examples
    --------
    >>> from dubois.charts import pictorial
    >>> fig, ax = pictorial.icon_grid(
    ...     {'Illiterate': 44, 'Literate': 56},
    ...     title='Illiteracy Among American Negroes, 1900'
    ... )
    """
    group_names = list(groups.keys())
    group_values = list(groups.values())
    n_groups = len(group_names)

    if colors is None:
        colors = dubois_colors.get_categorical(n_groups)

    # Compute cell counts per group (round to total)
    value_sum = sum(group_values)
    cell_counts = []
    running = 0
    for i, val in enumerate(group_values):
        if i == n_groups - 1:
            cell_counts.append(total - running)
        else:
            count = round(val / value_sum * total)
            cell_counts.append(count)
            running += count

    # Build color array for each cell
    cell_colors = []
    for i, count in enumerate(cell_counts):
        cell_colors.extend([colors[i]] * count)

    nrows = int(np.ceil(total / ncols))

    if figsize is None:
        w = ncols * (cell_size + cell_gap) + 1
        h = nrows * (cell_size + cell_gap) + 2
        figsize = (w, h)

    created_fig = ax is None
    if created_fig:
        fig, ax = plt.subplots(figsize=figsize, subplot_kw={'aspect': 'equal'})
    else:
        fig = ax.figure
        ax.set_aspect('equal')

    # Draw grid cells (top-to-bottom, left-to-right)
    for idx in range(total):
        col = idx % ncols
        row = idx // ncols

        x = col * (cell_size + cell_gap)
        y = (nrows - 1 - row) * (cell_size + cell_gap)  # top-to-bottom

        color = cell_colors[idx] if idx < len(cell_colors) else '#EEEEEE'

        if shape == 'circle':
            circle = plt.Circle(
                (x + cell_size / 2, y + cell_size / 2),
                cell_size / 2 * 0.9,
                facecolor=color, edgecolor='#000000',
                linewidth=0.8)
            ax.add_patch(circle)
        else:
            rect = mpatches.FancyBboxPatch(
                (x, y), cell_size, cell_size,
                boxstyle="square,pad=0",
                facecolor=color, edgecolor='#000000',
                linewidth=0.8)
            ax.add_patch(rect)

    # Set limits
    ax.set_xlim(-cell_gap, ncols * (cell_size + cell_gap))
    ax.set_ylim(-cell_gap, nrows * (cell_size + cell_gap) + cell_gap)
    ax.axis('off')

    if title:
        ax.set_title(title.upper(), fontsize=16, fontweight='bold',
                     fontfamily='serif', pad=20)
    if subtitle:
        ax.text(0.5, 1.02, subtitle, transform=ax.transAxes,
                ha='center', va='bottom', fontsize=11,
                style='italic', fontfamily='serif')

    if show_legend:
        legend_elements = [
            mpatches.Patch(facecolor=colors[i], edgecolor='black',
                           linewidth=1,
                           label=f'{group_names[i]} ({group_values[i]:.0f})')
            for i in range(n_groups)
        ]
        ax.legend(handles=legend_elements, loc='lower center',
                  bbox_to_anchor=(0.5, -0.08),
                  frameon=True, edgecolor='black', fancybox=False,
                  fontsize=10, ncol=n_groups)

    if created_fig:
        plt.tight_layout()
    return fig, ax


def pictograph_row(groups: Dict[str, float],
                   colors: Optional[List[str]] = None,
                   total: int = 100,
                   title: str = '',
                   subtitle: str = '',
                   bar_height: float = 0.6,
                   show_labels: bool = True,
                   figsize: Optional[Tuple[float, float]] = None,
                   ax: Optional[plt.Axes] = None) -> Tuple[plt.Figure, plt.Axes]:
    """
    Create a single-row proportional block chart.

    A horizontal bar divided into colored blocks, each representing
    one unit. This is a compact pictograph showing proportional
    composition in a single strip.

    Parameters
    ----------
    groups : dict
        Dictionary mapping group names to values.
    colors : list of str, optional
        Colors for each group.
    total : int
        Total number of units in the strip.
    title : str
        Chart title.
    subtitle : str
        Subtitle.
    bar_height : float
        Height of the strip.
    show_labels : bool
        Whether to show group labels in the strip.
    figsize : tuple, optional
        Figure size.
    ax : matplotlib.axes.Axes, optional
        Axes to draw on.

    Returns
    -------
    tuple of (Figure, Axes)

    Examples
    --------
    >>> from dubois.charts import pictorial
    >>> fig, ax = pictorial.pictograph_row(
    ...     {'Black': 89, 'Mulatto': 11},
    ...     title='Conjugal Condition, 1890'
    ... )
    """
    group_names = list(groups.keys())
    group_values = list(groups.values())
    n_groups = len(group_names)

    if colors is None:
        colors = dubois_colors.get_categorical(n_groups)

    value_sum = sum(group_values)

    if figsize is None:
        figsize = (14, 3)

    created_fig = ax is None
    if created_fig:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.figure

    x_start = 0
    segment_info = []  # Track segments for smart labeling
    for i, (name, val) in enumerate(zip(group_names, group_values)):
        width = (val / value_sum) * total

        rect = mpatches.FancyBboxPatch(
            (x_start, 0), width, bar_height,
            boxstyle="square,pad=0",
            facecolor=colors[i], edgecolor='#000000',
            linewidth=1.5)
        ax.add_patch(rect)

        segment_info.append({
            'name': name, 'val': val, 'x': x_start, 'width': width,
            'color': colors[i],
        })
        x_start += width

    # Smart label placement: inline for wide segments, callout for narrow
    if show_labels:
        # Estimate character width as fraction of total bar
        char_width_est = total / 80  # ~80 chars fit across the full bar

        # First pass: classify each segment as inline or callout
        placements = []
        for seg in segment_info:
            name_len = len(seg['name']) + 5  # +5 for percentage text
            needed_width = name_len * char_width_est
            width = seg['width']
            if width >= needed_width and width > 5:
                placements.append('inline')
            else:
                placements.append('callout')

        # Assign callout tiers — stagger to avoid overlap
        # Tier 1 = close, Tier 2 = farther out (if consecutive callouts)
        callout_tier = []
        tier_above = 1
        tier_below = 1
        side = 1  # 1=above, -1=below
        for i, p in enumerate(placements):
            if p == 'callout':
                callout_tier.append((side, tier_above if side == 1 else tier_below))
                # If the next segment is also a callout on the same side,
                # bump to next tier
                if side == 1:
                    tier_above += 1
                else:
                    tier_below += 1
                side *= -1
            else:
                callout_tier.append(None)
                tier_above = 1
                tier_below = 1

        for idx, seg in enumerate(segment_info):
            width = seg['width']
            cx = seg['x'] + width / 2

            if placements[idx] == 'inline':
                fsize = min(11, max(8, int(width / 6)))
                ax.text(cx, bar_height / 2,
                        f'{seg["name"].upper()}\n{seg["val"]:.0f}%',
                        ha='center', va='center',
                        fontsize=fsize, fontweight='bold',
                        color='white', fontfamily='serif')
            else:
                cside, tier = callout_tier[idx]
                step = 0.25 * tier
                y_offset = bar_height + 0.1 + step if cside == 1 else -0.1 - step
                va = 'bottom' if cside == 1 else 'top'

                line_y_start = bar_height if cside == 1 else 0
                ax.plot([cx, cx], [line_y_start, y_offset],
                        color='#333333', linewidth=0.8, zorder=3)

                ax.text(cx, y_offset,
                        f'{seg["name"].upper()} ({seg["val"]:.0f}%)',
                        ha='center', va=va,
                        fontsize=9, fontweight='bold',
                        color='#000000', fontfamily='serif')

    # Expand y limits to make room for callout labels
    ax.set_xlim(-0.5, total + 0.5)
    max_tiers = max((t[1] for t in callout_tier if t is not None), default=0)
    y_margin = 0.5 + 0.25 * max_tiers
    ax.set_ylim(-y_margin, bar_height + y_margin)
    ax.axis('off')

    if title:
        ax.set_title(title.upper(), fontsize=16, fontweight='bold',
                     fontfamily='serif', pad=20)
    if subtitle:
        ax.text(0.5, 1.05, subtitle, transform=ax.transAxes,
                ha='center', va='bottom', fontsize=11,
                style='italic', fontfamily='serif')

    if created_fig:
        plt.tight_layout()
    return fig, ax
