"""
W.E.B. Du Bois Color Palettes

This module contains color palettes extracted from W.E.B. Du Bois' original 
data visualizations from the 1900 Paris Exposition. These colors were 
hand-painted using gouache and ink, and are characterized by their bold,
saturated primary colors and limited but powerful palette.

Historical Context:
-------------------
Du Bois likely used Osborne's artists' paints, manufactured in Philadelphia.
The palette relies heavily on saturated primary colors, creating a spare,
crisp, and elegant style that predated modernist movements by decades.

Color Palette Notes:
-------------------
- The dominant palette uses crimson/red, gold/yellow, black, and occasionally
  green, blue, or purple
- Colors are bold and saturated, not pastel
- Du Bois used color sparingly but powerfully
- The aesthetic is hand-drawn with visible brush strokes and texture

References:
-----------
- W.E.B. Du Bois's Data Portraits: Visualizing Black America (2018)
- Library of Congress: African American Photographs Assembled for 1900 Paris Exposition
- #DuBoisChallenge style guides (2021, 2024)
"""

from typing import Dict, List, Tuple
import matplotlib.colors as mcolors

# Core Du Bois Colors - extracted from original plates
# These hex codes are approximations based on digital scans of the original works

# Primary palette - most commonly used colors
DUBOIS_PRIMARY = {
    'crimson': '#DC143C',      # Vivid red/crimson - most dominant color
    'gold': '#D4AF37',         # Rich gold/yellow
    'black': '#000000',        # True black
    'tan': '#D2B48C',          # Light tan/beige
}

# Extended palette - additional colors from various plates
DUBOIS_EXTENDED = {
    'crimson': '#DC143C',
    'pink': '#FFC1CC',         # Soft pink
    'rose': '#E75480',         # Medium rose pink
    'gold': '#D4AF37',
    'yellow': '#FFD700',       # Brighter yellow
    'green': '#00A550',        # Vibrant green
    'navy': '#000080',         # Dark navy blue
    'blue': '#4682B4',         # Steel blue
    'purple': '#663399',       # Deep purple
    'brown': '#654321',        # Rich brown
    'tan': '#D2B48C',
    'cream': '#F5DEB3',        # Wheat/cream
    'black': '#000000',
    'gray': '#808080',         # Medium gray
}

# Sequential palettes for different data types
# These are useful for showing progression or intensity

# Red/Crimson sequential (from light to dark)
CRIMSON_SEQUENTIAL = [
    '#FFF0F0',  # Very light pink
    '#FFD0D0',  # Light pink
    '#FFA0A0',  # Medium pink
    '#FF7070',  # Salmon
    '#E75480',  # Rose
    '#DC143C',  # Crimson
    '#B01030',  # Dark crimson
    '#800020',  # Burgundy
]

# Gold/Yellow sequential (from light to dark)
GOLD_SEQUENTIAL = [
    '#FFF9E6',  # Very light cream
    '#FFF0B3',  # Light cream
    '#FFE680',  # Light gold
    '#FFD700',  # Gold
    '#D4AF37',  # Rich gold
    '#C5A028',  # Dark gold
    '#B8860B',  # Darker gold
    '#8B6914',  # Bronze
]

# Green sequential (from light to dark)
GREEN_SEQUENTIAL = [
    '#E6F5E6',  # Very light green
    '#C0E8C0',  # Light green
    '#99D699',  # Medium light green
    '#66C266',  # Medium green
    '#00A550',  # Du Bois green
    '#008040',  # Dark green
    '#006030',  # Darker green
    '#004020',  # Very dark green
]

# Categorical palettes for discrete categories
# These are designed to be maximally distinguishable

# Classic Du Bois palette (3-4 colors)
DUBOIS_CLASSIC_3 = ['#DC143C', '#D4AF37', '#000000']
DUBOIS_CLASSIC_4 = ['#DC143C', '#D4AF37', '#00A550', '#000000']

# Extended categorical palette (up to 8 colors)
DUBOIS_CATEGORICAL_8 = [
    '#DC143C',  # Crimson
    '#D4AF37',  # Gold
    '#00A550',  # Green
    '#4682B4',  # Blue
    '#E75480',  # Rose
    '#663399',  # Purple
    '#654321',  # Brown
    '#000000',  # Black
]

# Diverging palette (useful for showing deviation from center)
DUBOIS_DIVERGING = [
    '#DC143C',  # Crimson
    '#E75480',  # Rose
    '#FFC1CC',  # Pink
    '#F5DEB3',  # Cream (neutral)
    '#99D699',  # Light green
    '#66C266',  # Medium green
    '#00A550',  # Du Bois green
]

# Pan-African flag colors (used in 2024 Du Bois Challenge)
PAN_AFRICAN = {
    'red': '#DC143C',
    'black': '#000000',
    'green': '#00A550',
}


def get_palette(name: str = 'primary') -> Dict[str, str]:
    """
    Get a Du Bois color palette by name.
    
    Parameters
    ----------
    name : str
        Name of the palette. Options:
        - 'primary': Core Du Bois colors (default)
        - 'extended': Full extended palette
        - 'pan_african': Pan-African flag colors
    
    Returns
    -------
    Dict[str, str]
        Dictionary mapping color names to hex codes
    
    Examples
    --------
    >>> palette = get_palette('primary')
    >>> print(palette['crimson'])
    '#DC143C'
    """
    palettes = {
        'primary': DUBOIS_PRIMARY,
        'extended': DUBOIS_EXTENDED,
        'pan_african': PAN_AFRICAN,
    }
    
    if name not in palettes:
        raise ValueError(f"Unknown palette '{name}'. Choose from: {list(palettes.keys())}")
    
    return palettes[name]


def get_sequential(color: str = 'crimson', n: int = None) -> List[str]:
    """
    Get a sequential color palette.
    
    Parameters
    ----------
    color : str
        Base color for the sequence. Options: 'crimson', 'gold', 'green'
    n : int, optional
        Number of colors to return. If None, returns full palette.
    
    Returns
    -------
    List[str]
        List of hex color codes from light to dark
    
    Examples
    --------
    >>> colors = get_sequential('crimson', n=5)
    >>> len(colors)
    5
    """
    sequences = {
        'crimson': CRIMSON_SEQUENTIAL,
        'gold': GOLD_SEQUENTIAL,
        'green': GREEN_SEQUENTIAL,
    }
    
    if color not in sequences:
        raise ValueError(f"Unknown sequence '{color}'. Choose from: {list(sequences.keys())}")
    
    seq = sequences[color]
    
    if n is None:
        return seq
    elif n <= 0:
        raise ValueError("n must be positive")
    elif n == 1:
        return [seq[len(seq) // 2]]
    elif n <= len(seq):
        # Return evenly spaced colors from the sequence
        indices = [int(i * (len(seq) - 1) / (n - 1)) for i in range(n)]
        return [seq[i] for i in indices]
    else:
        # If more colors requested than available, interpolate
        return _interpolate_colors(seq, n)


def get_categorical(n: int = 4) -> List[str]:
    """
    Get a categorical color palette with n distinct colors.
    
    Parameters
    ----------
    n : int
        Number of colors needed (1-8)
    
    Returns
    -------
    List[str]
        List of hex color codes optimized for categorical data
    
    Examples
    --------
    >>> colors = get_categorical(4)
    >>> len(colors)
    4
    """
    if n <= 0:
        raise ValueError("n must be positive")
    elif n <= 3:
        return DUBOIS_CLASSIC_3[:n]
    elif n <= 4:
        return DUBOIS_CLASSIC_4[:n]
    elif n <= 8:
        return DUBOIS_CATEGORICAL_8[:n]
    else:
        # For more than 8 categories, cycle through the palette
        full_cycles = n // 8
        remainder = n % 8
        result = DUBOIS_CATEGORICAL_8 * full_cycles + DUBOIS_CATEGORICAL_8[:remainder]
        return result


def get_diverging(n: int = 7) -> List[str]:
    """
    Get a diverging color palette.
    
    Useful for data that diverges from a central value (e.g., -100 to +100).
    
    Parameters
    ----------
    n : int
        Number of colors needed (must be odd for symmetric diverging scale)
    
    Returns
    -------
    List[str]
        List of hex color codes from one extreme through neutral to opposite extreme
    
    Examples
    --------
    >>> colors = get_diverging(7)
    >>> len(colors)
    7
    """
    if n <= 0:
        raise ValueError("n must be positive")
    elif n % 2 == 0:
        import warnings
        warnings.warn(f"Diverging palettes work best with odd numbers. Adding 1 to n={n}")
        n += 1

    if n == 1:
        return [DUBOIS_DIVERGING[len(DUBOIS_DIVERGING) // 2]]
    elif n <= len(DUBOIS_DIVERGING):
        indices = [int(i * (len(DUBOIS_DIVERGING) - 1) / (n - 1)) for i in range(n)]
        return [DUBOIS_DIVERGING[i] for i in indices]
    else:
        return _interpolate_colors(DUBOIS_DIVERGING, n)


def hex_to_rgb(hex_color: str) -> Tuple[float, float, float]:
    """
    Convert hex color to RGB tuple (0-1 range for matplotlib).
    
    Parameters
    ----------
    hex_color : str
        Hex color code (e.g., '#DC143C')
    
    Returns
    -------
    Tuple[float, float, float]
        RGB values in 0-1 range
    
    Examples
    --------
    >>> rgb = hex_to_rgb('#DC143C')
    >>> print(f"R: {rgb[0]:.3f}, G: {rgb[1]:.3f}, B: {rgb[2]:.3f}")
    R: 0.863, G: 0.078, B: 0.235
    """
    return mcolors.hex2color(hex_color)


def rgb_to_hex(r: float, g: float, b: float) -> str:
    """
    Convert RGB values (0-1 range) to hex color.
    
    Parameters
    ----------
    r, g, b : float
        RGB values in 0-1 range
    
    Returns
    -------
    str
        Hex color code
    
    Examples
    --------
    >>> hex_color = rgb_to_hex(0.863, 0.078, 0.235)
    >>> print(hex_color)
    '#dc143c'
    """
    return mcolors.rgb2hex((r, g, b))


def _interpolate_colors(colors: List[str], n: int) -> List[str]:
    """
    Interpolate between colors to create a palette of n colors.
    
    Parameters
    ----------
    colors : List[str]
        List of hex color codes to interpolate between
    n : int
        Number of colors to generate
    
    Returns
    -------
    List[str]
        List of interpolated hex color codes
    """
    if n == 1:
        return [colors[len(colors) // 2]]
    
    # Convert to RGB for interpolation
    rgb_colors = [hex_to_rgb(c) for c in colors]
    
    # Create interpolated colors
    result = []
    for i in range(n):
        # Map i to position in original color list
        pos = i * (len(rgb_colors) - 1) / (n - 1)
        idx = int(pos)
        frac = pos - idx
        
        if idx >= len(rgb_colors) - 1:
            result.append(colors[-1])
        else:
            # Linear interpolation between two colors
            r1, g1, b1 = rgb_colors[idx]
            r2, g2, b2 = rgb_colors[idx + 1]
            
            r = r1 + (r2 - r1) * frac
            g = g1 + (g2 - g1) * frac
            b = b1 + (b2 - b1) * frac
            
            result.append(rgb_to_hex(r, g, b))
    
    return result


def show_palette(palette_name: str = 'primary', save_path: str = None):
    """
    Display a color palette visually.
    
    Parameters
    ----------
    palette_name : str
        Name of palette to display
    save_path : str, optional
        Path to save the figure. If None, displays interactively.
    
    Examples
    --------
    >>> show_palette('primary')
    >>> show_palette('extended', save_path='palettes/extended.png')
    """
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    
    # Get the palette
    if palette_name in ['primary', 'extended', 'pan_african']:
        palette = get_palette(palette_name)
        colors = list(palette.values())
        names = list(palette.keys())
        title = f"Du Bois {palette_name.title()} Palette"
    elif palette_name == 'categorical':
        colors = get_categorical(8)
        names = [f'Color {i+1}' for i in range(len(colors))]
        title = "Du Bois Categorical Palette"
    elif palette_name in ['crimson', 'gold', 'green']:
        colors = get_sequential(palette_name)
        names = [f'{i+1}' for i in range(len(colors))]
        title = f"Du Bois {palette_name.title()} Sequential Palette"
    elif palette_name == 'diverging':
        colors = get_diverging(7)
        names = [f'{i+1}' for i in range(len(colors))]
        title = "Du Bois Diverging Palette"
    else:
        raise ValueError(f"Unknown palette: {palette_name}")
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 2))
    ax.set_xlim(0, len(colors))
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    # Draw color swatches
    for i, (color, name) in enumerate(zip(colors, names)):
        rect = mpatches.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor='black', linewidth=0.5)
        ax.add_patch(rect)
        
        # Add color name below
        ax.text(i + 0.5, -0.15, name, ha='center', va='top', fontsize=8, rotation=45)
        
        # Add hex code above
        ax.text(i + 0.5, 1.05, color.upper(), ha='center', va='bottom', fontsize=7, family='monospace')
    
    plt.title(title, fontsize=14, pad=30)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Palette saved to {save_path}")
    else:
        plt.show()


# Export main colors as module-level variables for easy access
crimson = DUBOIS_PRIMARY['crimson']
gold = DUBOIS_PRIMARY['gold']
black = DUBOIS_PRIMARY['black']
tan = DUBOIS_PRIMARY['tan']

__all__ = [
    # Dictionaries
    'DUBOIS_PRIMARY',
    'DUBOIS_EXTENDED',
    'PAN_AFRICAN',
    # Lists
    'CRIMSON_SEQUENTIAL',
    'GOLD_SEQUENTIAL',
    'GREEN_SEQUENTIAL',
    'DUBOIS_CLASSIC_3',
    'DUBOIS_CLASSIC_4',
    'DUBOIS_CATEGORICAL_8',
    'DUBOIS_DIVERGING',
    # Functions
    'get_palette',
    'get_sequential',
    'get_categorical',
    'get_diverging',
    'hex_to_rgb',
    'rgb_to_hex',
    'show_palette',
    # Quick access
    'crimson',
    'gold',
    'black',
    'tan',
]
