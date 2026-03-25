# Changelog

All notable changes to dubois-viz.

## [1.0.0] - 2026-03-24

### Changed
- Renamed package to `dubois-viz` (install via `pip install dubois-viz`, import as `import dubois`)
- Bumped to v1.0.0 stable release
- Added `MANIFEST.in` for proper sdist distribution
- Updated all URLs to `dubois-viz`

## [0.2.0] - 2026-02-26

### Added

#### Phase 2: Core Chart Types
- `dubois.charts.bar` — `bar()`, `grouped_bar()`, `stacked_bar()` for horizontal/vertical bar charts with Du Bois styling
- `dubois.charts.area` — `area()`, `proportional_area()` for stacked and normalized area charts
- `dubois.charts.butterfly` — `butterfly()` for back-to-back mirror charts, `comparison()` for dot comparison charts
- `dubois.charts.spiral` — `spiral()` for Plate 11-style spiral charts, `concentric_rings()` for ring progress charts

#### Phase 3: Signature Visualizations & Utilities
- `dubois.charts.wrapped` — `wrapped_bar()` for circular bar charts, `snake_bar()` for horizontal stacked row charts
- `dubois.charts.pictorial` — `icon_grid()` for waffle/icon grid charts, `pictograph_row()` for proportional strip charts
- `dubois.typography` — `title_block()`, `annotate()`, `source_note()`, `format_label()`, `plate_number()` for Du Bois-style text formatting
- `dubois.layouts` — `DuBoisPlate` class and `plate_layout()` for multi-panel plate composition

#### Phase 4: Polish & Distribution
- `pyproject.toml` with full PyPI metadata, classifiers, and optional dependencies
- `CHANGELOG.md`
- `LICENSE`
- Gallery examples recreating specific Du Bois plates
- 95 tests across 3 test files

### Changed
- Bumped version to 0.2.0
- Updated `dubois/__init__.py` to export `charts`, `typography`, and `layouts` modules
- Updated `dubois/charts/__init__.py` to include `wrapped` and `pictorial`
- Expanded README with documentation for all chart types, typography, and layouts
- Replaced minimal `setup.py` with comprehensive `pyproject.toml`

### Removed
- Stale `SOURCES.txt`, `requires.txt`, `setup.sh` from Phase 1 scaffolding

## [0.1.0] - 2026-02-26

### Added

#### Phase 1: Color Extraction & Theme
- `dubois.colors` — 7 color palettes (primary, extended, 3 sequential, categorical, diverging) extracted from Du Bois' original plates
- `dubois.colors.get_palette()`, `get_sequential()`, `get_categorical()`, `get_diverging()` — palette access functions
- `dubois.colors.hex_to_rgb()`, `rgb_to_hex()` — color conversion utilities
- `dubois.colors.show_palette()` — palette visualization
- `dubois.themes` — 3 matplotlib themes (classic, modern, minimal) with 4 context scales
- `dubois.themes.set_theme()`, `reset_theme()`, `DuBoisStyle` context manager
- 19 tests in `tests/test_colors.py`
- 6 examples in `examples/basic_usage.py`
- Complete README with installation, usage, and design principles
