# dubois-visualization-package
Python package that allows you to use W. E. B Dubois' revolutionary data visualizations 

## Historical Context

In 1900, W.E.B. Du Bois and his team at Atlanta University created 63 innovative hand-painted data visualizations for the "Exposition Universelle" in Paris. These charts challenged racist assumptions and powerfully demonstrated African American progress in the 35 years since emancipation. The visualizations were revolutionary in their use of:
    
- Bold, saturated colors from a limited palette
- Creative chart types (spirals, wrapped bars, butterfly charts)
- Compelling visual narratives
- Hand-crafted aesthetic with visible brushstrokes
- Modernist design principles decades before the modernist movement

This package helps you create matplotlib visualizations that capture the spirit and aesthetic of Du Bois' original works.

## Installation

```bash
pip install dubois-visualization-package
```

Or install from source:

```bash
git clone https://github.com/shalinialisha/dubois-visualization-package.git
cd dubois-visualization-package
pip install -e .
```

## Quick Start

```python
import dubois
import matplotlib.pyplot as plt
import numpy as np

# Apply the classic Du Bois theme
dubois.set_theme('classic')

# Use Du Bois colors
colors = dubois.get_categorical(4)

# Create a simple bar chart
categories = ['Agriculture', 'Manufacturing', 'Trade', 'Professions']
values = [45, 25, 20, 10]

plt.figure(figsize=(8, 6))
plt.barh(categories, values, color=colors, edgecolor='black', linewidth=1.5)
plt.xlabel('Percentage')
plt.title('Occupations of Georgia Negroes, 1900')
plt.tight_layout()
plt.show()
```

## Features

### Color Palettes

The package includes authentic color palettes extracted from Du Bois' original visualizations:

```python
# Primary palette (most commonly used colors)
primary = dubois.get_palette('primary')
# {'crimson': '#DC143C', 'gold': '#D4AF37', 'black': '#000000', 'tan': '#D2B48C'}

# Extended palette
extended = dubois.get_palette('extended')

# Sequential palettes for continuous data
crimson_seq = dubois.get_sequential('crimson', n=5)
gold_seq = dubois.get_sequential('gold', n=7)
green_seq = dubois.get_sequential('green', n=5)

# Categorical palettes for discrete categories
categorical = dubois.get_categorical(4)

# Diverging palette
diverging = dubois.get_diverging(7)

# Quick access to core colors
from dubois.colors import crimson, gold, black, tan
```

### Themes

Multiple theme variants inspired by Du Bois' aesthetic:

```python
# Classic theme (cream background, traditional)
dubois.set_theme('classic')

# Modern theme (white background, cleaner)
dubois.set_theme('modern')

# Minimal theme (no spines or ticks)
dubois.set_theme('minimal')

# Context scaling
dubois.set_theme('classic', context='notebook')  # Default
dubois.set_theme('modern', context='talk')       # For presentations
dubois.set_theme('classic', context='paper')     # For publications
dubois.set_theme('modern', context='poster')     # For posters

# Reset to original matplotlib settings
dubois.reset_theme()
```

### Context Manager

Use Du Bois styling temporarily:

```python
import dubois
import matplotlib.pyplot as plt

# Temporarily apply Du Bois style
with dubois.themes.DuBoisStyle('modern', 'talk'):
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.title("Temporary Du Bois Style")
    plt.show()

# Back to normal matplotlib style here
```

## Color Palette Visualization

View available palettes:

```python
from dubois.colors import show_palette

# Display different palettes
show_palette('primary')
show_palette('extended')
show_palette('categorical')
show_palette('crimson')  # Sequential
show_palette('diverging')

# Save to file
show_palette('primary', save_path='dubois_primary.png')
```

## Design Principles

When creating Du Bois-inspired visualizations:

1. **Color**: Use the limited but powerful color palette. Crimson/red is dominant, followed by gold and black. Use color sparingly but boldly.

2. **Typography**: Use serif fonts (Georgia, Times) for body text. Keep text minimal and purposeful.

3. **Simplicity**: Remove unnecessary elements (top/right spines, excessive gridlines). Let the data speak.

4. **Boldness**: Use thick lines, strong colors, and clear shapes. Du Bois' charts were meant to be seen from a distance.

5. **Hand-crafted feel**: Embrace slight irregularities. The original charts were hand-painted.

6. **Narrative**: Every chart tells a story. Use titles and annotations to guide the viewer.

## Examples

See the `examples/` directory for recreations of specific Du Bois plates:

- Plate 11: City and Rural Population (spiral chart)
- Plate 27: Occupations (butterfly chart)
- Plate 51: Proportion of Freemen and Slaves (stacked area)

## References

### Primary Sources

- **W.E.B. Du Bois's Data Portraits: Visualizing Black America** (2018)  
  Edited by Whitney Battle-Baptiste and Britt Rusert  
  ISBN: 978-1-61689-706-2

- **Library of Congress Collection**  
  "African American Photographs Assembled for 1900 Paris Exposition"  
  https://www.loc.gov/collections/african-american-photographs-1900-paris-exposition/

### Recreations and Challenges

- **#DuBoisChallenge** - Annual community challenge to recreate Du Bois visualizations  
  https://github.com/ajstarks/dubois-data-portraits

- **TidyTuesday Du Bois Challenge** (2021, 2024)  
  Community recreations in R, Python, and other tools

### Articles

- Nightingale: "Exploring the Craft and Design of W.E.B. Du Bois' Data Visualizations"
- Smithsonian Magazine: "W.E.B. Du Bois' Visionary Infographics"
- Flourish: "Masters series: The data visualization legacy of W.E.B. Du Bois"

## Citation

If you use this package in academic work, please cite:

```bibtex
@software{dubois-visualization-package,
  title = {dubois-visualization-package: Data Visualization in the Style of W.E.B. Du Bois},
  author = {Shalini Thinakaran},
  year = {2026},
  url = {https://github.com/shalinialisha/dubois-visualization-package}
}
```

And please cite the original Du Bois work:

```bibtex
@book{battle2018web,
  title={W.E.B. Du Bois's Data Portraits: Visualizing Black America},
  author={Battle-Baptiste, Whitney and Rusert, Britt},
  year={2018},
  publisher={Princeton Architectural Press},
  isbn={978-1-61689-706-2}
}
```

## Acknowledgments

This package was inspired by:
- W.E.B. Du Bois and his team at Atlanta University
- Anthony Starks' decksh recreations
- All the data visualization practitioners keeping Du Bois' legacy alive

---

**"The problem of the twentieth century is the problem of the color line."**  
— W.E.B. Du Bois, *The Souls of Black Folk* (1903)