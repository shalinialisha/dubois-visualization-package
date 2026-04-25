"""
Du Bois-Style Area Charts

Stacked area charts inspired by W.E.B. Du Bois' visualizations of
population proportions over time. Du Bois used filled areas with bold
colors to show how proportions changed across decades, most notably
in his "Proportion of Freemen and Slaves Among American Negroes" chart.

Key Design Elements:
- Bold fill colors with black outlines
- Clear year/period labels along the axis
- Annotations for key historical events
- Proportional (0-100%) or absolute scale
- Minimal axis chrome
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import List, Optional, Tuple, Union
from dubois import colors as dubois_colors


def area(x: List[Union[int, float, str]],
         groups: dict,
         colors: Optional[List[str]] = None,
         title: str = '',
         subtitle: str = '',
         stacked: bool = True,
         normalized: bool = False,
         show_labels: bool = True,
         annotations: Optional[dict] = None,
         figsize: Optional[Tuple[float, float]] = None,
         ax: Optional[plt.Axes] = None,
         **kwargs) -> Tuple[plt.Figure, plt.Axes]:
    """
    Create a Du Bois-style stacked area chart.

    Parameters
    ----------
    x : list
        X-axis values (typically years or time periods).
    groups : dict
        Dictionary mapping group names to lists of values.
        Example: {'Free': [10, 20, 30], 'Enslaved': [90, 80, 70]}
    colors : list of str, optional
        Fill colors for each group.
    title : str
        Chart title.
    subtitle : str
        Subtitle.
    stacked : bool
        Whether to stack areas (True) or overlay them (False).
    normalized : bool
        Whether to normalize to 100% (proportional). Only applies when stacked=True.
    show_labels : bool
        Whether to show group labels in the filled areas.
    annotations : dict, optional
        Dictionary mapping x-values to annotation text.
        Example: {1865: 'Emancipation'}
    figsize : tuple, optional
        Figure size.
    ax : matplotlib.axes.Axes, optional
        Axes to draw on.
    **kwargs
        Additional keyword arguments passed to fill_between.

    Returns
    -------
    tuple of (Figure, Axes)
    """
    group_names = list(groups.keys())
    n_groups = len(group_names)
    x_arr = np.arange(len(x))

    if colors is None:
        colors = dubois_colors.get_categorical(n_groups)

    if figsize is None:
        figsize = (12, 7)

    created_fig = ax is None
    if created_fig:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.figure

    edge_color = kwargs.pop('edgecolor', '#000000')
    line_width = kwargs.pop('linewidth', 1.5)
    alpha = kwargs.pop('alpha', 0.9)

    values_matrix = np.array([groups[name] for name in group_names], dtype=float)

    if stacked:
        if normalized:
            totals = values_matrix.sum(axis=0)
            totals[totals == 0] = 1
            values_matrix = values_matrix / totals * 100

        cumulative = np.zeros(len(x))

        for i, (name, vals) in enumerate(zip(group_names, values_matrix)):
            ax.fill_between(x_arr, cumulative, cumulative + vals,
                            color=colors[i], edgecolor=edge_color,
                            linewidth=line_width, alpha=alpha,
                            label=name, **kwargs)

            if show_labels:
                # Find the best position for the label: where the band is
                # tallest, but well inside the chart (not at edges)
                midpoints = cumulative + vals / 2
                heights = vals.copy()
                n_pts = len(heights)
                # Strongly penalize edges so labels stay interior
                for j in range(n_pts):
                    edge_dist = min(j, n_pts - 1 - j)
                    if edge_dist == 0:
                        heights[j] *= 0.1
                    elif edge_dist == 1:
                        heights[j] *= 0.4
                    elif edge_dist == 2:
                        heights[j] *= 0.7

                best_idx = np.argmax(heights)
                mid_y = midpoints[best_idx]
                orig_height = vals[best_idx]
                total_at_idx = values_matrix.sum(axis=0)[best_idx]
                if orig_height > (total_at_idx * 0.04):
                    ax.text(best_idx, mid_y, name.upper(),
                            ha='center', va='center',
                            fontweight='bold', fontsize=12,
                            color='white', fontfamily='serif')

            cumulative += vals
    else:
        for i, (name, vals) in enumerate(zip(group_names, values_matrix)):
            ax.fill_between(x_arr, 0, vals,
                            color=colors[i], edgecolor=edge_color,
                            linewidth=line_width, alpha=alpha * 0.7,
                            label=name, **kwargs)

    ax.set_xticks(x_arr)
    ax.set_xticklabels([str(v) for v in x], fontsize=11, fontfamily='serif')

    # Add a small right margin so annotations near the edge aren't clipped
    x_pad = (x_arr[-1] - x_arr[0]) * 0.03
    ax.set_xlim(x_arr[0] - x_pad, x_arr[-1] + x_pad)

    if normalized:
        ax.set_ylim(0, 100)
    else:
        ax.set_ylim(0, None)

    if annotations:
        for x_val, text in annotations.items():
            # Find the closest x position
            if x_val in x:
                idx = list(x).index(x_val)
            else:
                # Interpolate between x values for proper placement
                idx_float = np.interp(x_val, x, x_arr)
                idx = idx_float

            # Place annotation at the midpoint of the chart height
            if stacked:
                # Use integer index for cumulative lookup
                int_idx = min(int(round(float(idx))), len(cumulative) - 1)
                y_mid = cumulative[int_idx] / 2
            else:
                int_idx = min(int(round(float(idx))), len(x) - 1)
                y_mid = max(v[int_idx] for v in values_matrix) / 2

            ax.annotate(text.upper(),
                        xy=(idx, y_mid),
                        fontsize=11, fontweight='bold',
                        fontfamily='serif',
                        ha='center', va='center',
                        bbox=dict(boxstyle='round,pad=0.3',
                                  facecolor='white', edgecolor='black',
                                  alpha=0.9))

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
    ax.set_yticklabels([])

    if not show_labels:
        ax.legend(frameon=True, edgecolor='black', fancybox=False, fontsize=11)

    if created_fig:
        plt.tight_layout()
    return fig, ax


def proportional_area(x: List[Union[int, float, str]],
                      groups: dict,
                      colors: Optional[List[str]] = None,
                      title: str = '',
                      subtitle: str = '',
                      annotations: Optional[dict] = None,
                      figsize: Optional[Tuple[float, float]] = None,
                      ax: Optional[plt.Axes] = None,
                      **kwargs) -> Tuple[plt.Figure, plt.Axes]:
    """
    Convenience wrapper for a normalized (100%) stacked area chart.

    This is the style Du Bois most commonly used for showing population
    proportions across time periods.

    Parameters
    ----------
    x : list
        X-axis values (typically years).
    groups : dict
        Dictionary mapping group names to lists of values.
    colors : list of str, optional
        Fill colors.
    title : str
        Chart title.
    subtitle : str
        Subtitle.
    annotations : dict, optional
        Annotations at specific x positions.
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
    return area(x, groups, colors=colors, title=title, subtitle=subtitle,
                stacked=True, normalized=True, show_labels=True,
                annotations=annotations, figsize=figsize, ax=ax, **kwargs)
