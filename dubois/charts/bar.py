"""
Du Bois-Style Bar Charts

Enhanced horizontal and vertical bar charts inspired by W.E.B. Du Bois'
original data visualizations. Du Bois frequently used bold horizontal bars
with clear labels and black outlines to present comparative data about
African American life and progress.

Key Design Elements:
- Horizontal orientation (Du Bois' preferred layout)
- Black edge colors on all bars
- Value labels displayed on or beside bars
- Bold, saturated fill colors from the Du Bois palette
- Clean serif typography
- No axis lines, ticks, or gridlines — data speaks for itself
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import to_rgb
import numpy as np
from typing import List, Optional, Union, Tuple
from dubois import colors as dubois_colors


def _is_dark(color) -> bool:
    """Whether a fill is dark enough that white text reads better than black."""
    r, g, b = to_rgb(color)
    return (0.299 * r + 0.587 * g + 0.114 * b) < 0.55


def bar(categories: List[str],
        values: List[float],
        colors: Optional[List[str]] = None,
        title: str = '',
        subtitle: str = '',
        value_labels: bool = True,
        label_format: str = '{:.0f}',
        orientation: str = 'horizontal',
        bar_height: float = 0.7,
        figsize: Optional[Tuple[float, float]] = None,
        ax: Optional[plt.Axes] = None,
        **kwargs) -> Tuple[plt.Figure, plt.Axes]:
    """
    Create a Du Bois-style bar chart.

    Parameters
    ----------
    categories : list of str
        Category labels for each bar.
    values : list of float
        Numeric values for each bar.
    colors : list of str, optional
        Bar colors. Defaults to Du Bois categorical palette.
    title : str
        Chart title (displayed in uppercase, Du Bois style).
    subtitle : str
        Subtitle displayed below the title.
    value_labels : bool
        Whether to display value labels on bars.
    label_format : str
        Format string for value labels (e.g., '{:.1f}%').
    orientation : str
        'horizontal' (default, Du Bois preferred) or 'vertical'.
    bar_height : float
        Height/width of bars (0-1 range, default 0.7).
    figsize : tuple, optional
        Figure size (width, height). Auto-calculated if None.
    ax : matplotlib.axes.Axes, optional
        Axes to draw on. Creates new figure if None.
    **kwargs
        Additional keyword arguments passed to plt.barh/plt.bar.

    Returns
    -------
    tuple of (Figure, Axes)
    """
    n = len(categories)
    if colors is None:
        colors = dubois_colors.get_categorical(n)

    if figsize is None:
        if orientation == 'horizontal':
            figsize = (10, max(4, n * 0.9))
        else:
            figsize = (max(6, n * 1.2), 6)

    created_fig = ax is None
    if created_fig:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.figure

    edge_color = kwargs.pop('edgecolor', '#000000')
    line_width = kwargs.pop('linewidth', 1.5)

    if orientation == 'horizontal':
        y_pos = np.arange(n)
        bars = ax.barh(y_pos, values, height=bar_height,
                       color=colors, edgecolor=edge_color,
                       linewidth=line_width, **kwargs)
        ax.set_yticks(y_pos)
        ax.set_yticklabels(categories, fontsize=12, fontweight='bold',
                           fontfamily='serif')
        ax.invert_yaxis()

        if value_labels:
            max_abs = max((abs(v) for v in values), default=1) or 1
            for bar_rect, val, fill in zip(bars, values, colors):
                inside = abs(val) > max_abs * 0.25
                if inside:
                    if val >= 0:
                        x, ha = val - max_abs * 0.02, 'right'
                    else:
                        x, ha = val + max_abs * 0.02, 'left'
                    color = 'white' if _is_dark(fill) else '#000000'
                else:
                    if val >= 0:
                        x, ha = val + max_abs * 0.02, 'left'
                    else:
                        x, ha = val - max_abs * 0.02, 'right'
                    color = '#000000'
                ax.text(x,
                        bar_rect.get_y() + bar_rect.get_height() / 2,
                        label_format.format(val),
                        ha=ha, va='center', fontweight='bold',
                        color=color, fontsize=12, fontfamily='serif')
    else:
        x_pos = np.arange(n)
        bars = ax.bar(x_pos, values, width=bar_height,
                      color=colors, edgecolor=edge_color,
                      linewidth=line_width, **kwargs)
        ax.set_xticks(x_pos)
        ax.set_xticklabels(categories, rotation=45, ha='right',
                           fontsize=11, fontweight='bold', fontfamily='serif')

        if value_labels:
            max_abs = max((abs(v) for v in values), default=1) or 1
            for bar_rect, val in zip(bars, values):
                if val >= 0:
                    y, va = val + max_abs * 0.02, 'bottom'
                else:
                    y, va = val - max_abs * 0.02, 'top'
                ax.text(bar_rect.get_x() + bar_rect.get_width() / 2,
                        y,
                        label_format.format(val),
                        ha='center', va=va, fontweight='bold',
                        color='#000000', fontsize=12, fontfamily='serif')

    if title:
        ax.set_title(title.upper(), fontsize=16, fontweight='bold',
                     fontfamily='serif', pad=20)
    if subtitle:
        ax.text(0.5, 1.02, subtitle, transform=ax.transAxes,
                ha='center', va='bottom', fontsize=11,
                style='italic', fontfamily='serif')

    # Du Bois style: remove all chart chrome
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(axis='both', length=0)
    if orientation == 'horizontal':
        ax.set_xticklabels([])
    else:
        ax.set_yticklabels([])

    if created_fig:
        plt.tight_layout()
    return fig, ax


def grouped_bar(categories: List[str],
                groups: dict,
                colors: Optional[List[str]] = None,
                title: str = '',
                subtitle: str = '',
                value_labels: bool = True,
                label_format: str = '{:.0f}',
                orientation: str = 'horizontal',
                bar_height: float = 0.8,
                figsize: Optional[Tuple[float, float]] = None,
                ax: Optional[plt.Axes] = None,
                **kwargs) -> Tuple[plt.Figure, plt.Axes]:
    """
    Create a Du Bois-style grouped bar chart.

    Parameters
    ----------
    categories : list of str
        Category labels.
    groups : dict
        Dictionary mapping group names to lists of values.
        Example: {'1890': [40, 30, 20], '1900': [50, 35, 15]}
    colors : list of str, optional
        Colors for each group.
    title : str
        Chart title.
    subtitle : str
        Subtitle.
    value_labels : bool
        Whether to display value labels.
    label_format : str
        Format string for value labels.
    orientation : str
        'horizontal' or 'vertical'.
    bar_height : float
        Total height allocated per category group.
    figsize : tuple, optional
        Figure size.
    ax : matplotlib.axes.Axes, optional
        Axes to draw on.
    **kwargs
        Additional keyword arguments passed to bar drawing.

    Returns
    -------
    tuple of (Figure, Axes)
    """
    group_names = list(groups.keys())
    n_groups = len(group_names)
    n_cats = len(categories)

    if colors is None:
        colors = dubois_colors.get_categorical(n_groups)

    if figsize is None:
        if orientation == 'horizontal':
            figsize = (10, max(4, n_cats * n_groups * 0.5))
        else:
            figsize = (max(6, n_cats * 1.5), 6)

    created_fig = ax is None
    if created_fig:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.figure

    edge_color = kwargs.pop('edgecolor', '#000000')
    line_width = kwargs.pop('linewidth', 1.5)

    single_height = bar_height / n_groups
    y_pos = np.arange(n_cats)

    all_values = [v for vals in groups.values() for v in vals]
    max_val = max(all_values) if all_values else 1

    for i, (group_name, vals) in enumerate(groups.items()):
        offset = (i - n_groups / 2 + 0.5) * single_height

        if orientation == 'horizontal':
            bars = ax.barh(y_pos + offset, vals, height=single_height * 0.9,
                           color=colors[i], edgecolor=edge_color,
                           linewidth=line_width, label=group_name, **kwargs)
            if value_labels:
                for bar_rect, val in zip(bars, vals):
                    width = bar_rect.get_width()
                    if width > max_val * 0.25:
                        ax.text(width - max_val * 0.02,
                                bar_rect.get_y() + bar_rect.get_height() / 2,
                                label_format.format(val),
                                ha='right', va='center', fontweight='bold',
                                color='white', fontsize=10, fontfamily='serif')
                    else:
                        ax.text(width + max_val * 0.02,
                                bar_rect.get_y() + bar_rect.get_height() / 2,
                                label_format.format(val),
                                ha='left', va='center', fontweight='bold',
                                color='#000000', fontsize=10, fontfamily='serif')
        else:
            bars = ax.bar(y_pos + offset, vals, width=single_height * 0.9,
                          color=colors[i], edgecolor=edge_color,
                          linewidth=line_width, label=group_name, **kwargs)
            if value_labels:
                for bar_rect, val in zip(bars, vals):
                    height = bar_rect.get_height()
                    ax.text(bar_rect.get_x() + bar_rect.get_width() / 2,
                            height + max_val * 0.02,
                            label_format.format(val),
                            ha='center', va='bottom', fontweight='bold',
                            color='#000000', fontsize=10, fontfamily='serif')

    if orientation == 'horizontal':
        ax.set_yticks(y_pos)
        ax.set_yticklabels(categories, fontsize=12, fontweight='bold',
                           fontfamily='serif')
        ax.invert_yaxis()
    else:
        ax.set_xticks(y_pos)
        ax.set_xticklabels(categories, rotation=45, ha='right',
                           fontsize=11, fontweight='bold', fontfamily='serif')

    if title:
        ax.set_title(title.upper(), fontsize=16, fontweight='bold',
                     fontfamily='serif', pad=20)
    if subtitle:
        ax.text(0.5, 1.02, subtitle, transform=ax.transAxes,
                ha='center', va='bottom', fontsize=11,
                style='italic', fontfamily='serif')

    ax.legend(frameon=True, edgecolor='black', fancybox=False, fontsize=11,
              loc='upper left', bbox_to_anchor=(1.02, 1))
    # Du Bois style: remove all chart chrome
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(axis='both', length=0)
    if orientation == 'horizontal':
        ax.set_xticklabels([])
    else:
        ax.set_yticklabels([])

    if created_fig:
        plt.tight_layout()
    return fig, ax


def stacked_bar(categories: List[str],
                groups: dict,
                colors: Optional[List[str]] = None,
                title: str = '',
                subtitle: str = '',
                value_labels: bool = True,
                label_format: str = '{:.0f}',
                show_total: bool = False,
                orientation: str = 'horizontal',
                bar_height: float = 0.7,
                figsize: Optional[Tuple[float, float]] = None,
                ax: Optional[plt.Axes] = None,
                **kwargs) -> Tuple[plt.Figure, plt.Axes]:
    """
    Create a Du Bois-style stacked bar chart.

    Parameters
    ----------
    categories : list of str
        Category labels.
    groups : dict
        Dictionary mapping segment names to lists of values.
        Example: {'Free': [10, 20], 'Enslaved': [90, 80]}
    colors : list of str, optional
        Colors for each segment.
    title : str
        Chart title.
    subtitle : str
        Subtitle.
    value_labels : bool
        Whether to display value labels in segments.
    label_format : str
        Format string for value labels.
    show_total : bool
        Whether to show total at end of bar.
    orientation : str
        'horizontal' or 'vertical'.
    bar_height : float
        Height/width of bars.
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
    group_names = list(groups.keys())
    n_groups = len(group_names)
    n_cats = len(categories)

    if colors is None:
        colors = dubois_colors.get_categorical(n_groups)

    if figsize is None:
        if orientation == 'horizontal':
            figsize = (10, max(4, n_cats * 0.9))
        else:
            figsize = (max(6, n_cats * 1.2), 6)

    created_fig = ax is None
    if created_fig:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.figure

    edge_color = kwargs.pop('edgecolor', '#000000')
    line_width = kwargs.pop('linewidth', 1.5)

    y_pos = np.arange(n_cats)
    cumulative = np.zeros(n_cats)

    # Width threshold: don't try to label segments smaller than ~4% of the
    # widest stack — they'll just collide with neighbors. Legend identifies them.
    stack_totals = np.sum(
        np.array([list(v) for v in groups.values()], dtype=float), axis=0)
    total_max = float(np.max(stack_totals)) if len(stack_totals) else 1.0
    label_threshold = total_max * 0.04

    for i, (group_name, vals) in enumerate(groups.items()):
        vals = np.array(vals, dtype=float)
        text_color = 'white' if _is_dark(colors[i]) else '#000000'

        if orientation == 'horizontal':
            bars = ax.barh(y_pos, vals, left=cumulative, height=bar_height,
                           color=colors[i], edgecolor=edge_color,
                           linewidth=line_width, label=group_name, **kwargs)
            if value_labels:
                for bar_rect, val in zip(bars, vals):
                    if val > label_threshold:
                        cx = bar_rect.get_x() + bar_rect.get_width() / 2
                        cy = bar_rect.get_y() + bar_rect.get_height() / 2
                        ax.text(cx, cy, label_format.format(val),
                                ha='center', va='center', fontweight='bold',
                                color=text_color,
                                fontsize=11, fontfamily='serif')
        else:
            bars = ax.bar(y_pos, vals, bottom=cumulative, width=bar_height,
                          color=colors[i], edgecolor=edge_color,
                          linewidth=line_width, label=group_name, **kwargs)
            if value_labels:
                for bar_rect, val in zip(bars, vals):
                    if val > label_threshold:
                        cx = bar_rect.get_x() + bar_rect.get_width() / 2
                        cy = bar_rect.get_y() + bar_rect.get_height() / 2
                        ax.text(cx, cy, label_format.format(val),
                                ha='center', va='center', fontweight='bold',
                                color=text_color,
                                fontsize=11, fontfamily='serif')

        cumulative += vals

    if show_total:
        for j, total in enumerate(cumulative):
            if orientation == 'horizontal':
                ax.text(total + max(cumulative) * 0.02, y_pos[j],
                        label_format.format(total),
                        ha='left', va='center', fontweight='bold',
                        fontsize=11, fontfamily='serif')
            else:
                ax.text(y_pos[j], total + max(cumulative) * 0.02,
                        label_format.format(total),
                        ha='center', va='bottom', fontweight='bold',
                        fontsize=11, fontfamily='serif')

    if orientation == 'horizontal':
        ax.set_yticks(y_pos)
        ax.set_yticklabels(categories, fontsize=12, fontweight='bold',
                           fontfamily='serif')
        ax.invert_yaxis()
    else:
        ax.set_xticks(y_pos)
        ax.set_xticklabels(categories, rotation=45, ha='right',
                           fontsize=11, fontweight='bold', fontfamily='serif')

    if title:
        ax.set_title(title.upper(), fontsize=16, fontweight='bold',
                     fontfamily='serif', pad=20)
    if subtitle:
        ax.text(0.5, 1.02, subtitle, transform=ax.transAxes,
                ha='center', va='bottom', fontsize=11,
                style='italic', fontfamily='serif')

    ax.legend(frameon=True, edgecolor='black', fancybox=False, fontsize=11,
              loc='upper left', bbox_to_anchor=(1.02, 1))
    # Du Bois style: remove all chart chrome
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(axis='both', length=0)
    if orientation == 'horizontal':
        ax.set_xticklabels([])
    else:
        ax.set_yticklabels([])

    if created_fig:
        plt.tight_layout()
    return fig, ax
