# dubois-visualizations

**Bring your data to life with the bold, hand-painted style of W.E.B. Du Bois' 1900 Paris Exposition charts.**

## Historical Context

In 1900, W.E.B. Du Bois and his team at Atlanta University created 63 innovative hand-painted data visualizations for the "Exposition Universelle" in Paris. The visualizations were revolutionary in their use of creative chart types (spirals, wrapped bars, butterfly charts), compelling visual narratives, and modernist design principles decades before the modernist movement. To me they represent the power of marginalized peoples when we are able to contribute to humanity. These charts were made 35 years post-emancipation and are an additon to Du Bois' incredible achivements. 

This package helps you create matplotlib visualizations that capture the spirit and aesthetic of Du Bois' original works.

![Five sectors of the U.S. economy from 1900 to 1960, in deep crimson, gold, green, blue, and pink](docs/images/gallery/area_5_groups.png)

Plug in your own numbers — sales, survey results, demographics, anything — and get back charts that look like Du Bois' originals: deep crimson, mustard gold, forest green, jet black. Every chart in this README was made from ordinary modern data, not the historical figures Du Bois used.

> ⚠️ **This is still a work in progress.** Everything works and you can use it today, but a few charts still get a little messy with very long labels or unusual data shapes. The [open issues](https://github.com/shalinialisha/dubois-visualization-package/issues) list shows what's known and what's coming.

---

## What you can make

### Bar charts — for ranking things

A horizontal bar chart of company headcount by team:

![Headcount by function — five teams ranked by size](docs/images/gallery/bar_long_labels.png)

A stacked bar showing how browser market share has shifted year over year:

![Browser market share over three years, stacked](docs/images/gallery/stacked_many_segments.png)

### Area charts — for change over time

How five sectors of the U.S. economy shifted from 1900 to 1960:

![Five sectors of the economy across six decades](docs/images/gallery/area_5_groups.png)

A proportional view (always summing to 100%) of where revenue comes from across six years:

![Revenue mix as percentages over time](docs/images/gallery/area_proportional_long_names.png)

### Butterfly charts — for comparing two sides

Education levels in the 2010 vs. 2020 U.S. Census, mirrored across a center line:

![Education levels compared between two censuses](docs/images/gallery/butterfly_long_labels.png)

Junior vs. senior salary across departments, shown as paired dots connected by a line:

![Junior vs senior salary by department](docs/images/gallery/butterfly_comparison.png)

### Spiral and ring charts — Du Bois' signature style

Urban vs. suburban share across five U.S. metro areas, on concentric rings:

![Urban vs suburban share across five metros, on concentric rings](docs/images/gallery/spiral_long_names.png)

A dashboard of five business KPIs, each ring filled to its current value:

![Five business KPIs as concentric filled rings](docs/images/gallery/spiral_concentric.png)

### Wrapped charts — for compact proportional layouts

Four industries laid out as a single bar that spirals inward:

![Four industries on a wrapped spiral bar](docs/images/gallery/wrapped_long_names.png)

Six U.S. states broken down by urban / suburban / rural population, one row each:

![Six states as urban-suburban-rural rows](docs/images/gallery/wrapped_snake.png)

### Pictograph charts — for proportions you can count

Smartphone market share as a 10×10 grid of squares — every cell is one percent:

![Smartphone market share as a 100-cell grid](docs/images/gallery/pictorial_grid_8groups.png)

A 7-point survey scale (Excellent → Very Poor) shown as a single proportional strip:

![Likert scale results as one proportional strip](docs/images/gallery/pictorial_row_7segs.png)

---

## Installation

```bash
pip install dubois-viz
```

Or install from source:

```bash
git clone https://github.com/shalinialisha/dubois-viz.git
cd dubois-viz
pip install -e .
```

**Requirements:** Python 3.9+, `matplotlib >= 3.5`, `numpy >= 1.20`.

To run the test suite or build the docs, install the optional extras:

```bash
pip install -e ".[dev]"   # pytest, pytest-cov, black, ruff
pytest tests/             # 95 tests
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

### Chart Types

Specialized chart types that recreate Du Bois' signature visualization styles:

#### Bar Charts

```python
from dubois.charts import bar

# Simple horizontal bar chart
fig, ax = bar.bar(
    ['Agriculture', 'Domestic', 'Manufacturing', 'Professions'],
    [62, 28, 5, 5],
    title='Occupations of Georgia Negroes',
    label_format='{:.0f}%',
)

# Grouped bar chart (compare across time periods)
fig, ax = bar.grouped_bar(
    ['Agriculture', 'Manufacturing', 'Professions'],
    {'1890': [62, 5, 3], '1900': [55, 8, 5]},
    title='Occupations Over Time',
)

# Stacked bar chart
fig, ax = bar.stacked_bar(
    ['Georgia', 'Virginia', 'Mississippi'],
    {'City': [16, 18, 6], 'Rural': [84, 82, 94]},
    title='City and Rural Population',
)
```

#### Area Charts

```python
from dubois.charts import area

# Proportional area chart (Du Bois' "Freemen and Slaves" style)
fig, ax = area.proportional_area(
    [1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870],
    {'Slaves': [92, 89, 86, 87, 86, 87, 88, 89, 0],
     'Free': [8, 11, 14, 13, 14, 13, 12, 11, 100]},
    title='Proportion of Freemen and Slaves',
    annotations={1865: 'Emancipation'},
)
```

#### Butterfly (Mirror) Charts

```python
from dubois.charts import butterfly

# Back-to-back comparison chart
fig, ax = butterfly.butterfly(
    ['Under 10', '10-20', '20-30', '30-40', '40-50', '50+'],
    [18, 20, 17, 14, 12, 19],
    [16, 18, 19, 15, 13, 19],
    left_label='Negroes', right_label='Whites',
    title='Comparative Age Distribution',
)

# Dot comparison chart
fig, ax = butterfly.comparison(
    ['Literacy', 'Land Ownership', 'Business'],
    [30, 12, 2],
    [57, 21, 5],
    label_a='1880', label_b='1900',
    title='Negro Progress Since Emancipation',
)
```

#### Spiral Charts (Plate 11 Style)

```python
from dubois.charts import spiral

# Iconic Du Bois spiral chart
fig, ax = spiral.spiral(
    ['Georgia', 'Virginia', 'Mississippi', 'S. Carolina',
     'Alabama', 'Louisiana', 'N. Carolina', 'Tennessee'],
    [16, 18, 6, 8, 10, 22, 7, 15],
    label_a='City', label_b='Rural',
    title='City and Rural Population 1890',
)

# Concentric rings (progress indicators)
fig, ax = spiral.concentric_rings(
    ['Literacy', 'School Enrollment', 'Land Ownership', 'Business'],
    [57, 54, 21, 5],
    title='Negro Progress Indicators, 1900',
)
```

#### Wrapped (Snake) Bar Charts

```python
from dubois.charts import wrapped

# Circular wrapped bar chart
fig, ax = wrapped.wrapped_bar(
    ['Agriculture', 'Domestic', 'Manufacturing', 'Trade', 'Professions'],
    [62, 28, 5, 4, 1],
    title='Occupations of Georgia Negroes',
)

# Snake bar (horizontal stacked rows)
fig, ax = wrapped.snake_bar(
    ['Georgia', 'Virginia', 'Mississippi'],
    {'City': [16, 18, 6], 'Rural': [84, 82, 94]},
    title='City and Rural Population',
)
```

#### Pictorial (Icon Grid) Charts

```python
from dubois.charts import pictorial

# Waffle-style icon grid (each cell = 1%)
fig, ax = pictorial.icon_grid(
    {'Illiterate': 44, 'Literate': 56},
    title='Illiteracy Among American Negroes, 1900',
)

# Single-row proportional strip
fig, ax = pictorial.pictograph_row(
    {'Black': 80, 'Mulatto': 15, 'Other': 5},
    title='Racial Composition',
)
```

### Typography Utilities

```python
from dubois import typography

# Hierarchical title block
typography.title_block(ax,
    'City and Rural Population',
    subtitle='Among American Negroes in the Former Slave States',
    caption='Done by Atlanta University, 1900')

# Du Bois-style annotation with arrow and box
typography.annotate(ax, 'Emancipation', xy=(1865, 50))

# Source attribution
typography.source_note(ax, 'Source: United States Census Bureau')

# Plate number label
typography.plate_number(ax, 11)
```

### Multi-Panel Layouts

```python
from dubois.layouts import DuBoisPlate

# Create a multi-panel plate
plate = DuBoisPlate(2, 2,
    title='The Georgia Negro: A Social Study',
    subtitle='Prepared for the Paris Exposition of 1900',
    plate_number=42)

ax1 = plate.get_axes(0, 0)  # Top-left panel
ax2 = plate.get_axes(0, 1)  # Top-right panel
ax3 = plate.get_axes(1, 0, colspan=2)  # Full-width bottom

# Draw on each axes, then save
plate.save('my_plate.png')
plate.close()
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

See the `examples/` directory for complete working examples. Each script writes its
output PNGs into `examples/output/` (created on first run, ignored by git).

**Walkthroughs** — read these to learn the API:

- `examples/basic_usage.py` — Color palettes, themes, and simple matplotlib charts
- `examples/chart_examples.py` — Bar, area, butterfly, and spiral charts
- `examples/phase3_examples.py` — Wrapped bars, pictorial charts, typography, multi-panel layouts
- `examples/gallery.py` — Recreations of specific Du Bois plates (11, 25, 27, 31, …)

**Try-it scripts** — exercise every chart type end-to-end:

- `examples/try_your_data.py` — Plug in your own data and regenerate every chart
- `examples/test_with_real_data.py` — Runs every chart against the TidyTuesday Du Bois CSVs in `examples/data/`
- `examples/test_random_data.py` — Runs every chart against randomly generated data

Chart examples include recreations inspired by:
- Plate 11: City and Rural Population (spiral chart)
- Plate 25: Comparative Age Distribution (butterfly chart)
- Plate 31: Proportion of Freemen and Slaves (proportional area chart)
- Plate 27: Occupations of Georgia Negroes (bar, wrapped bar)
- Pictorial grids showing illiteracy and population composition

```bash
# Generate the walkthrough examples
python examples/basic_usage.py
python examples/chart_examples.py
python examples/phase3_examples.py
python examples/gallery.py

# Or exercise every chart type at once
python examples/test_with_real_data.py
```

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
@software{dubois-viz,
  title = {dubois-viz: Data Visualization in the Style of W.E.B. Du Bois},
  author = {Shalini Thinakaran},
  year = {2026},
  url = {https://github.com/shalinialisha/dubois-viz}
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
