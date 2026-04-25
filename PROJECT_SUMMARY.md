# dubois-viz — Project Summary

A Python package for creating matplotlib visualizations inspired by W.E.B. Du Bois' groundbreaking
data portraits from the 1900 Paris Exposition. The package is **v1.0.0 — feature complete**,
covering colors, themes, typography, layouts, and seven specialized chart types.

## Repository Layout

```
dubois-visualization-package/
├── dubois/                    # Main package (~1,500 lines)
│   ├── __init__.py            # Public API exports
│   ├── colors.py              # Color palettes and conversion utilities
│   ├── themes.py              # Matplotlib themes and context manager
│   ├── typography.py          # Title blocks, annotations, source notes
│   ├── layouts.py             # DuBoisPlate multi-panel composition
│   └── charts/                # Specialized chart types
│       ├── bar.py             # bar / grouped_bar / stacked_bar
│       ├── area.py            # area / proportional_area
│       ├── butterfly.py       # butterfly / comparison
│       ├── spiral.py          # spiral / concentric_rings
│       ├── wrapped.py         # wrapped_bar / snake_bar
│       └── pictorial.py       # icon_grid / pictograph_row
├── examples/                  # Runnable example scripts
│   ├── basic_usage.py         # Colors, themes, palettes
│   ├── chart_examples.py      # Bar, area, butterfly, spiral
│   ├── phase3_examples.py     # Wrapped, pictorial, typography, layouts
│   ├── gallery.py             # Recreations of specific Du Bois plates
│   ├── try_your_data.py       # Plug-and-play template for your data
│   ├── test_with_real_data.py # Exercises every chart with TidyTuesday data
│   ├── test_random_data.py    # Exercises every chart with random data
│   └── data/                  # Du Bois CSV datasets (TidyTuesday 2021)
├── tests/                     # 95 pytest tests
│   ├── test_colors.py
│   ├── test_charts.py
│   └── test_phase3.py
├── pyproject.toml             # Modern Python packaging config
├── setup.py                   # Backwards-compat shim
├── MANIFEST.in                # sdist file inclusion
├── LICENSE                    # MIT License
├── CHANGELOG.md               # Version history
└── README.md                  # Full user documentation
```

## What's Included

### Colors (`dubois.colors`)

- **Primary palette**: crimson (`#DC143C`), gold (`#D4AF37`), black (`#000000`), tan (`#D2B48C`)
- **Extended palette**: 13 colors including pink, rose, green, navy, purple, brown, cream
- **Sequential palettes**: crimson, gold, green (8 shades each)
- **Categorical palettes**: classic 3-color, classic 4-color, extended 8-color
- **Diverging palette**: 7-color crimson → cream → green
- Helpers: `get_palette()`, `get_sequential()`, `get_categorical()`, `get_diverging()`,
  `hex_to_rgb()`, `rgb_to_hex()`, `show_palette()`

### Themes (`dubois.themes`)

- Three theme variants: **classic** (cream background), **modern** (white), **minimal** (no spines)
- Four context scales: `notebook` (default), `paper` (0.8×), `talk` (1.3×), `poster` (1.6×)
- Global usage via `set_theme()` / `reset_theme()` and a `DuBoisStyle` context manager

### Chart Types (`dubois.charts`)

| Module | Functions |
| --- | --- |
| `bar` | `bar`, `grouped_bar`, `stacked_bar` |
| `area` | `area`, `proportional_area` |
| `butterfly` | `butterfly`, `comparison` |
| `spiral` | `spiral`, `concentric_rings` |
| `wrapped` | `wrapped_bar`, `snake_bar` |
| `pictorial` | `icon_grid`, `pictograph_row` |

### Typography & Layouts

- `dubois.typography`: `title_block`, `annotate`, `source_note`, `format_label`, `plate_number`
- `dubois.layouts.DuBoisPlate`: multi-panel figure composition with title block and plate numbering

## Public API

```python
import dubois

# Themes
dubois.set_theme('classic', context='notebook')
dubois.reset_theme()

# Colors
dubois.colors.crimson
dubois.get_categorical(4)
dubois.get_sequential('crimson', n=5)
dubois.get_diverging(7)

# Charts
from dubois.charts import bar, area, butterfly, spiral, wrapped, pictorial

# Typography & layouts
from dubois import typography
from dubois.layouts import DuBoisPlate
```

## Installation

```bash
# From PyPI (once published)
pip install dubois-viz

# From source
git clone https://github.com/shalinialisha/dubois-viz.git
cd dubois-viz
pip install -e .
```

Requires Python ≥ 3.9, `matplotlib ≥ 3.5`, `numpy ≥ 1.20`.

## Running Tests and Examples

```bash
# Run the test suite (95 tests)
pytest tests/

# Generate example charts
python examples/basic_usage.py
python examples/chart_examples.py
python examples/phase3_examples.py
python examples/gallery.py

# Try it with your own data
python examples/try_your_data.py
```

## Design Principles

1. **Authenticity** — colors and styling derived from research of original 1900 plates.
2. **Simplicity** — opinionated defaults that work out of the box, with full matplotlib access underneath.
3. **Composability** — every helper returns standard `(fig, ax)` so charts integrate with normal matplotlib workflows.
4. **Accessibility** — clear API, docstrings on every public function, runnable examples.

## References

- *W.E.B. Du Bois's Data Portraits: Visualizing Black America* — Battle-Baptiste & Rusert (2018), Princeton Architectural Press
- [Library of Congress — 1900 Paris Exposition](https://www.loc.gov/collections/african-american-photographs-1900-paris-exposition/)
- [#DuBoisChallenge — Anthony Starks](https://github.com/ajstarks/dubois-data-portraits)
- TidyTuesday Du Bois Challenge (2021, 2024)

---

> **"The problem of the twentieth century is the problem of the color line."**
> — W.E.B. Du Bois, *The Souls of Black Folk* (1903)
