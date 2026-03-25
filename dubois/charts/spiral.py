"""
Du Bois-Style Spiral Charts

Recreation of the iconic spiral chart from Plate 11 of Du Bois' 1900 Paris
Exposition display: "City and Rural Population 1890." This chart type wraps
proportional data around concentric rings, creating a visually striking
display that draws the viewer inward.

The original Plate 11 showed the proportion of African Americans living
in cities versus rural areas across different states, with data on
concentric rings from the outer edge inward.

Key Design Elements:
- Data displayed on bold concentric rings
- Contrasting colors for different segments
- Clear, large labels at each ring
- Strong visual center-pull effect
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Wedge
import numpy as np
from typing import List, Optional, Tuple, Union
from dubois import colors as dubois_colors


def spiral(categories: List[str],
           values_a: List[float],
           values_b: Optional[List[float]] = None,
           label_a: str = 'Group A',
           label_b: str = 'Group B',
           color_a: Optional[str] = None,
           color_b: Optional[str] = None,
           title: str = '',
           subtitle: str = '',
           max_value: Optional[float] = None,
           start_radius: float = 1.2,
           ring_width: float = 0.12,
           ring_gap: float = 0.04,
           figsize: Optional[Tuple[float, float]] = None,
           ax: Optional[plt.Axes] = None) -> Tuple[plt.Figure, plt.Axes]:
    """
    Create a Du Bois-style spiral chart (Plate 11 style).

    Each category is rendered as a ring. The ring is divided
    proportionally between two groups (e.g., city vs rural population).

    Parameters
    ----------
    categories : list of str
        Labels for each ring (displayed outside).
    values_a : list of float
        Values for the first group (rendered as proportion of ring).
    values_b : list of float, optional
        Values for the second group. If None, computed as max_value - values_a.
    label_a : str
        Label for first group.
    label_b : str
        Label for second group.
    color_a : str, optional
        Color for first group. Defaults to Du Bois crimson.
    color_b : str, optional
        Color for second group. Defaults to Du Bois gold.
    title : str
        Chart title.
    subtitle : str
        Subtitle.
    max_value : float, optional
        Maximum value (for computing proportions). If None, uses sum of a+b.
    start_radius : float
        Radius of outermost ring.
    ring_width : float
        Width of each ring.
    ring_gap : float
        Gap between rings.
    figsize : tuple, optional
        Figure size.
    ax : matplotlib.axes.Axes, optional
        Axes to draw on.

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
        figsize = (10, 10)

    if ax is None:
        fig, ax = plt.subplots(figsize=figsize, subplot_kw={'aspect': 'equal'})
    else:
        fig = ax.figure

    vals_a = np.array(values_a, dtype=float)

    if values_b is not None:
        vals_b = np.array(values_b, dtype=float)
    else:
        if max_value is not None:
            vals_b = max_value - vals_a
        else:
            vals_b = 100.0 - vals_a

    # Compute proportions
    fractions_a = vals_a / (vals_a + vals_b)

    # Auto-scale ring dimensions to fit all categories
    min_inner = 0.2
    available = start_radius - min_inner
    step = available / n
    eff_ring_width = min(ring_width, step * 0.72)
    eff_ring_gap = step - eff_ring_width

    # Build rings from outside in
    for i in range(n):
        radius = start_radius - i * (eff_ring_width + eff_ring_gap)
        if radius <= eff_ring_width:
            break

        frac = fractions_a[i]
        angle_a = frac * 360

        # Draw group A wedge (starting from top, going clockwise)
        wedge_a = Wedge(center=(0, 0), r=radius,
                        theta1=90 - angle_a, theta2=90,
                        width=eff_ring_width,
                        facecolor=color_a, edgecolor='#000000',
                        linewidth=1.0)
        ax.add_patch(wedge_a)

        # Draw group B wedge (the remainder)
        wedge_b = Wedge(center=(0, 0), r=radius,
                        theta1=90 - 360, theta2=90 - angle_a,
                        width=eff_ring_width,
                        facecolor=color_b, edgecolor='#000000',
                        linewidth=1.0)
        ax.add_patch(wedge_b)

        # Percentage label at the midpoint of segment A
        pct_text = f'{frac * 100:.0f}%'
        label_angle_deg = 90 - angle_a / 2
        label_r = radius - eff_ring_width / 2
        label_x = label_r * np.cos(np.radians(label_angle_deg))
        label_y = label_r * np.sin(np.radians(label_angle_deg))

        if angle_a > 20:
            ax.text(label_x, label_y, pct_text,
                    ha='center', va='center', fontsize=10,
                    fontweight='bold', color='white',
                    fontfamily='serif')

    # Category labels on the left side, with connector lines to each ring
    # Compute max label width to set proper margin
    rendered_rings = []
    for i in range(n):
        radius = start_radius - i * (eff_ring_width + eff_ring_gap)
        if radius <= eff_ring_width:
            break
        rendered_rings.append((i, radius))

    n_rendered = len(rendered_rings)

    # Space labels evenly across the full height of the rings
    label_spacing = max(eff_ring_width + eff_ring_gap, 0.16)
    total_label_height = (n_rendered - 1) * label_spacing
    label_top = total_label_height / 2

    # Estimate label margin from longest category name
    max_label_len = max(len(c) for c in categories[:n_rendered]) if n_rendered > 0 else 5
    label_margin = max(0.8, max_label_len * 0.08)
    label_x_base = -start_radius - label_margin

    for idx, (i, radius) in enumerate(rendered_rings):
        label_y = label_top - idx * label_spacing

        # Connect to the actual left edge of the ring (at 180 degrees)
        ring_left_x = -radius + eff_ring_width / 2
        ring_y = 0.0  # rings are centered at origin, left edge is at y=0

        ax.text(label_x_base - 0.05, label_y, categories[i],
                ha='right', va='center', fontsize=11,
                fontweight='bold', fontfamily='serif')
        # Draw connector line from label to the ring's left edge
        ax.plot([label_x_base, ring_left_x], [label_y, ring_y],
                color='#999999', linewidth=0.6, linestyle='-',
                clip_on=False)

    # Set limits with room for labels
    margin = 0.2
    ax.set_xlim(label_x_base - 0.1, start_radius + margin)
    ax.set_ylim(-start_radius - margin, start_radius + margin)
    ax.axis('off')

    # Title
    if title:
        ax.set_title(title.upper(), fontsize=16, fontweight='bold',
                     fontfamily='serif', pad=20)
    if subtitle:
        ax.text(0.5, 0.96, subtitle, transform=ax.transAxes,
                ha='center', va='bottom', fontsize=11,
                style='italic', fontfamily='serif')

    # Legend
    legend_elements = [
        mpatches.Patch(facecolor=color_a, edgecolor='black',
                       linewidth=1, label=label_a),
        mpatches.Patch(facecolor=color_b, edgecolor='black',
                       linewidth=1, label=label_b),
    ]
    ax.legend(handles=legend_elements, loc='lower right',
              frameon=True, edgecolor='black', fancybox=False,
              fontsize=11)

    plt.tight_layout()
    return fig, ax


def concentric_rings(categories: List[str],
                     values: List[float],
                     colors: Optional[List[str]] = None,
                     title: str = '',
                     subtitle: str = '',
                     max_value: Optional[float] = None,
                     show_values: bool = True,
                     value_format: str = '{:.0f}%',
                     start_radius: float = 1.2,
                     ring_width: float = 0.12,
                     ring_gap: float = 0.04,
                     background_color: str = '#E0E0E0',
                     figsize: Optional[Tuple[float, float]] = None,
                     ax: Optional[plt.Axes] = None) -> Tuple[plt.Figure, plt.Axes]:
    """
    Create concentric rings showing single values as proportions.

    Each ring represents a category, filled proportionally to its value.
    This is a simpler variant of the spiral chart useful for showing
    progress or completion across categories.

    Parameters
    ----------
    categories : list of str
        Labels for each ring.
    values : list of float
        Values for each ring (interpreted as percentages of max_value).
    colors : list of str, optional
        Colors for each ring.
    title : str
        Chart title.
    subtitle : str
        Subtitle.
    max_value : float, optional
        Maximum value for proportion calculation. Defaults to 100.
    show_values : bool
        Whether to show value labels.
    value_format : str
        Format string for value labels.
    start_radius : float
        Radius of outermost ring.
    ring_width : float
        Width of each ring.
    ring_gap : float
        Gap between rings.
    background_color : str
        Color for unfilled portion of rings.
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

    if max_value is None:
        max_value = 100.0

    if figsize is None:
        figsize = (10, 10)

    if ax is None:
        fig, ax = plt.subplots(figsize=figsize, subplot_kw={'aspect': 'equal'})
    else:
        fig = ax.figure

    # Auto-scale ring dimensions to fit all categories
    min_inner = 0.2
    available = start_radius - min_inner
    step = available / n
    eff_ring_width = min(ring_width, step * 0.72)
    eff_ring_gap = step - eff_ring_width

    for i in range(n):
        radius = start_radius - i * (eff_ring_width + eff_ring_gap)
        if radius <= eff_ring_width:
            break

        frac = min(values[i] / max_value, 1.0)
        angle = frac * 360

        # Background ring (full circle)
        bg_wedge = Wedge(center=(0, 0), r=radius,
                         theta1=0, theta2=360,
                         width=eff_ring_width,
                         facecolor=background_color, edgecolor='#000000',
                         linewidth=0.5)
        ax.add_patch(bg_wedge)

        # Filled portion (starting from top, going clockwise)
        if angle > 0:
            fill_wedge = Wedge(center=(0, 0), r=radius,
                               theta1=90 - angle, theta2=90,
                               width=eff_ring_width,
                               facecolor=colors[i], edgecolor='#000000',
                               linewidth=1.0)
            ax.add_patch(fill_wedge)

        # Value label at the end of the filled arc
        if show_values:
            label_angle_deg = 90 - angle - 8
            label_r = radius - eff_ring_width / 2
            lx = label_r * np.cos(np.radians(label_angle_deg))
            ly = label_r * np.sin(np.radians(label_angle_deg))
            ax.text(lx, ly, value_format.format(values[i]),
                    ha='center', va='center', fontsize=10,
                    fontweight='bold', fontfamily='serif')

    # Category labels on the left, with connector lines to each ring
    rendered_rings = []
    for i in range(n):
        radius = start_radius - i * (eff_ring_width + eff_ring_gap)
        if radius <= eff_ring_width:
            break
        rendered_rings.append((i, radius))

    n_rendered = len(rendered_rings)

    label_spacing = max(eff_ring_width + eff_ring_gap, 0.16)
    total_label_height = (n_rendered - 1) * label_spacing
    label_top = total_label_height / 2

    max_label_len = max(len(c) for c in categories[:n_rendered]) if n_rendered > 0 else 5
    label_margin = max(0.8, max_label_len * 0.08)
    label_x_base = -start_radius - label_margin

    for idx, (i, radius) in enumerate(rendered_rings):
        label_y = label_top - idx * label_spacing

        ring_left_x = -radius + eff_ring_width / 2
        ring_y = 0.0

        ax.text(label_x_base - 0.05, label_y, categories[i],
                ha='right', va='center', fontsize=11,
                fontweight='bold', fontfamily='serif')
        ax.plot([label_x_base, ring_left_x], [label_y, ring_y],
                color='#999999', linewidth=0.6, linestyle='-',
                clip_on=False)

    margin = 0.2
    ax.set_xlim(label_x_base - 0.1, start_radius + margin)
    ax.set_ylim(-start_radius - margin, start_radius + margin)
    ax.axis('off')

    if title:
        ax.set_title(title.upper(), fontsize=16, fontweight='bold',
                     fontfamily='serif', pad=20)
    if subtitle:
        ax.text(0.5, 0.96, subtitle, transform=ax.transAxes,
                ha='center', va='bottom', fontsize=11,
                style='italic', fontfamily='serif')

    plt.tight_layout()
    return fig, ax
