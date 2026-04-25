"""
Du Bois-Style Wrapped (Snake) Bar Charts

Bars that wrap around a spiral path, inspired by Du Bois' original plates
where proportional data was laid out along curved paths. The wrapped bar
is a single continuous bar that spirals inward, with colored segments
representing different categories flowing seamlessly into each other.

Du Bois used this style to show proportional data in a compact circular
layout, making efficient use of space while creating a memorable visual.

Key Design Elements:
- One continuous bar spiraling inward
- Bold color fills with black outlines
- Labels placed beside each segment
- Proportional segment lengths along the spiral
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Polygon
import numpy as np
from typing import List, Optional, Tuple, Dict
from dubois import colors as dubois_colors


def _spiral_radius(theta, start_theta, total_theta, r_outer, r_inner):
    """Compute the spiral centerline radius at a given angle."""
    progress = (theta - start_theta) / total_theta
    return r_outer - progress * (r_outer - r_inner)


def _draw_spiral_segment(ax, theta_start, theta_end, start_theta, total_theta,
                         r_outer, r_inner, bar_width, color, n_points=80):
    """Draw one colored segment along the spiral as a filled polygon."""
    thetas = np.linspace(theta_start, theta_end, max(n_points, 4))

    # Outer edge of the bar
    r_center = np.array([
        _spiral_radius(t, start_theta, total_theta, r_outer, r_inner)
        for t in thetas
    ])
    r_out = r_center + bar_width / 2
    r_in = r_center - bar_width / 2

    # Convert to cartesian (angles in radians, measured from top, clockwise)
    # Map: 0° = top, positive = clockwise
    # In matplotlib polar: 90° = top, decreasing = clockwise
    angles_rad = np.radians(90 - thetas)

    x_out = r_out * np.cos(angles_rad)
    y_out = r_out * np.sin(angles_rad)
    x_in = r_in * np.cos(angles_rad)
    y_in = r_in * np.sin(angles_rad)

    # Build polygon: outer edge forward, inner edge backward
    verts_x = np.concatenate([x_out, x_in[::-1]])
    verts_y = np.concatenate([y_out, y_in[::-1]])
    verts = list(zip(verts_x, verts_y))

    poly = Polygon(verts, closed=True,
                   facecolor=color, edgecolor='#000000',
                   linewidth=1.2, zorder=2)
    ax.add_patch(poly)


def wrapped_bar(categories: List[str],
                values: List[float],
                colors: Optional[List[str]] = None,
                title: str = '',
                subtitle: str = '',
                n_wraps: float = 1.5,
                bar_width: float = 0.18,
                r_outer: float = 1.0,
                r_inner: float = 0.25,
                show_values: bool = True,
                show_inline_labels: bool = True,
                value_format: str = '{:.0f}',
                direction: str = 'clockwise',
                figsize: Optional[Tuple[float, float]] = None,
                ax: Optional[plt.Axes] = None) -> Tuple[plt.Figure, plt.Axes]:
    """
    Create a Du Bois-style wrapped bar chart.

    A single continuous bar spirals inward from the outer edge, with
    colored segments representing each category's proportion.

    Parameters
    ----------
    categories : list of str
        Category labels.
    values : list of float
        Values for each category (determines segment length).
    colors : list of str, optional
        Fill colors for each segment.
    title : str
        Chart title.
    subtitle : str
        Subtitle.
    n_wraps : float
        Number of times the bar wraps around (default 1.5).
    bar_width : float
        Thickness of the bar.
    r_outer : float
        Outer radius of the spiral.
    r_inner : float
        Inner radius of the spiral.
    show_values : bool
        Whether to show value labels inside segments.
    show_inline_labels : bool
        Whether to show category name labels along the spiral.
        Set to False to rely on the legend only.
    value_format : str
        Format string for value labels.
    direction : str
        'clockwise' or 'counterclockwise'.
    figsize : tuple, optional
        Figure size.
    ax : matplotlib.axes.Axes, optional
        Axes to draw on.

    Returns
    -------
    tuple of (Figure, Axes)
    """
    n = len(categories)

    if colors is None:
        colors = dubois_colors.get_categorical(n)

    if figsize is None:
        figsize = (10, 10)

    created_fig = ax is None
    if created_fig:
        fig, ax = plt.subplots(figsize=figsize, subplot_kw={'aspect': 'equal'})
    else:
        fig = ax.figure
        ax.set_aspect('equal')

    total = sum(values)
    total_theta = 360.0 * n_wraps
    start_theta = 0.0

    # Draw each segment along the continuous spiral
    current_theta = start_theta
    for i, (cat, val, color) in enumerate(zip(categories, values, colors)):
        seg_theta = (val / total) * total_theta
        if direction == 'counterclockwise':
            seg_theta = -seg_theta

        _draw_spiral_segment(
            ax, current_theta, current_theta + seg_theta,
            start_theta, abs(total_theta),
            r_outer, r_inner, bar_width, color
        )

        # Label at the midpoint of this segment
        mid_theta = current_theta + seg_theta / 2
        mid_r = _spiral_radius(
            mid_theta, start_theta, abs(total_theta), r_outer, r_inner
        )

        label_angle_rad = np.radians(90 - mid_theta)

        # Rotate text to follow the curve
        text_angle = -mid_theta
        ha = 'left'
        if 90 < (mid_theta % 360) < 270:
            text_angle += 180
            ha = 'right'

        # Only place curved labels for segments large enough to read.
        # Restrict to the outer band of the spiral — long text on inner
        # wraps can cross outer rings, which is unreadable.
        abs_seg = abs(seg_theta)
        on_outer_band = mid_r > (r_outer + r_inner) / 2
        if show_inline_labels and abs_seg > 25 and on_outer_band:
            # Place label outside the bar
            label_r = mid_r + bar_width / 2 + 0.08
            lx = label_r * np.cos(label_angle_rad)
            ly = label_r * np.sin(label_angle_rad)

            ax.text(lx, ly, cat.upper(),
                    ha=ha, va='center',
                    fontsize=10, fontweight='bold',
                    fontfamily='serif',
                    rotation=text_angle,
                    rotation_mode='anchor')

        # Value label inside the bar
        if show_values and show_inline_labels and abs_seg > 15:
            vx = mid_r * np.cos(label_angle_rad)
            vy = mid_r * np.sin(label_angle_rad)

            val_angle = -mid_theta
            if 90 < (mid_theta % 360) < 270:
                val_angle += 180

            ax.text(vx, vy, value_format.format(val),
                    ha='center', va='center',
                    fontsize=10, fontweight='bold',
                    color='white',
                    rotation=val_angle,
                    rotation_mode='anchor')

        current_theta += seg_theta

    # Legend with ALL categories (including small ones that didn't get curved labels)
    legend_elements = [
        mpatches.Patch(facecolor=colors[i], edgecolor='black',
                       linewidth=1,
                       label=f'{categories[i]} ({value_format.format(values[i])})')
        for i in range(n)
    ]
    ax.legend(handles=legend_elements, loc='lower right',
              frameon=True, edgecolor='black', fancybox=False,
              fontsize=10)

    # Set limits
    extent = r_outer + bar_width + 0.3
    ax.set_xlim(-extent, extent)
    ax.set_ylim(-extent, extent)
    ax.axis('off')

    if title:
        ax.set_title(title.upper(), fontsize=16, fontweight='bold',
                     fontfamily='serif', pad=20)
    if subtitle:
        ax.text(0.5, 0.94, subtitle, transform=ax.transAxes,
                ha='center', va='bottom', fontsize=11,
                style='italic', fontfamily='serif')

    if created_fig:
        plt.tight_layout()
    return fig, ax


def snake_bar(categories: List[str],
              segments: Dict[str, List[float]],
              colors: Optional[List[str]] = None,
              title: str = '',
              subtitle: str = '',
              bar_height: float = 0.6,
              row_gap: float = 0.3,
              figsize: Optional[Tuple[float, float]] = None,
              ax: Optional[plt.Axes] = None) -> Tuple[plt.Figure, plt.Axes]:
    """
    Create a snake-style horizontal stacked bar chart.

    Each category gets a row. Within each row, colored segments
    represent different groups, laid out left-to-right.

    Parameters
    ----------
    categories : list of str
        Category labels (one per row).
    segments : dict
        Dictionary mapping segment names to lists of values.
        Example: {'City': [16, 18, 6], 'Rural': [84, 82, 94]}
    colors : list of str, optional
        Colors for each segment group.
    title : str
        Chart title.
    subtitle : str
        Subtitle.
    bar_height : float
        Height of each bar row.
    row_gap : float
        Gap between rows.
    figsize : tuple, optional
        Figure size.
    ax : matplotlib.axes.Axes, optional
        Axes to draw on.

    Returns
    -------
    tuple of (Figure, Axes)
    """
    seg_names = list(segments.keys())
    n_segs = len(seg_names)
    n_cats = len(categories)

    if colors is None:
        colors = dubois_colors.get_categorical(n_segs)

    if figsize is None:
        figsize = (12, max(4, n_cats * (bar_height + row_gap) + 1.5))

    created_fig = ax is None
    if created_fig:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.figure

    max_total = 0
    for i in range(n_cats):
        total = sum(segments[name][i] for name in seg_names)
        max_total = max(max_total, total)

    # Estimate left margin from longest category name
    max_cat_len = max(len(c) for c in categories) if categories else 5
    left_margin = max(3, max_cat_len * 0.8)

    for i, cat in enumerate(categories):
        y = (n_cats - 1 - i) * (bar_height + row_gap)
        x_start = 0

        for j, (seg_name, vals) in enumerate(segments.items()):
            val = vals[i]
            width = (val / max_total) * 100

            rect = mpatches.FancyBboxPatch(
                (x_start, y), width, bar_height,
                boxstyle="square,pad=0",
                facecolor=colors[j], edgecolor='#000000',
                linewidth=1.5)
            ax.add_patch(rect)

            # Segment value label (show percentage for wider segments,
            # abbreviation for narrower ones)
            if width > 8:
                ax.text(x_start + width / 2, y + bar_height / 2,
                        f'{val:.0f}%',
                        ha='center', va='center',
                        fontsize=11, fontweight='bold',
                        color='white', fontfamily='serif')
            elif width > 3:
                ax.text(x_start + width / 2, y + bar_height / 2,
                        f'{val:.0f}',
                        ha='center', va='center',
                        fontsize=9, fontweight='bold',
                        color='white', fontfamily='serif')

            x_start += width

        # Category label on the left (positioned relative to computed margin)
        ax.text(-1.5, y + bar_height / 2, cat,
                ha='right', va='center',
                fontsize=12, fontweight='bold', fontfamily='serif')

    ax.set_xlim(-left_margin - 0.5, 105)
    ax.set_ylim(-row_gap, n_cats * (bar_height + row_gap))
    ax.axis('off')

    # Legend
    legend_elements = [
        mpatches.Patch(facecolor=colors[j], edgecolor='black',
                       linewidth=1, label=name)
        for j, name in enumerate(seg_names)
    ]
    ax.legend(handles=legend_elements,
              loc='upper left', bbox_to_anchor=(1.02, 1),
              frameon=True, edgecolor='black', fancybox=False,
              fontsize=11)

    if title:
        ax.set_title(title.upper(), fontsize=16, fontweight='bold',
                     fontfamily='serif', pad=20)
    if subtitle:
        ax.text(0.5, 1.02, subtitle, transform=ax.transAxes,
                ha='center', va='bottom', fontsize=11,
                style='italic', fontfamily='serif')

    if created_fig:
        plt.tight_layout()
    return fig, ax
