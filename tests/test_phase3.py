"""
Tests for Phase 3: Typography, Wrapped bars, Pictorial charts, Layouts.
"""

import pytest
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from dubois import typography, layouts
from dubois.charts import wrapped, pictorial


class TestTypography:
    """Tests for typography utilities."""

    def setup_method(self):
        plt.close('all')

    def test_title_block(self):
        fig, ax = plt.subplots()
        typography.title_block(ax, 'Main Title', subtitle='A subtitle',
                               caption='Done by Atlanta University')
        plt.close(fig)

    def test_title_block_title_only(self):
        fig, ax = plt.subplots()
        typography.title_block(ax, 'Just a Title')
        plt.close(fig)

    def test_annotate(self):
        fig, ax = plt.subplots()
        ax.plot([0, 1, 2], [0, 1, 0])
        ann = typography.annotate(ax, 'Peak', xy=(1, 1), xytext=(1.5, 0.8))
        assert ann is not None
        plt.close(fig)

    def test_annotate_no_box_no_arrow(self):
        fig, ax = plt.subplots()
        ax.plot([0, 1], [0, 1])
        ann = typography.annotate(ax, 'Point', xy=(0.5, 0.5),
                                  box=False, arrow=False)
        assert ann is not None
        plt.close(fig)

    def test_annotate_lowercase(self):
        fig, ax = plt.subplots()
        ax.plot([0, 1], [0, 1])
        ann = typography.annotate(ax, 'lower', xy=(0.5, 0.5), uppercase=False)
        assert ann is not None
        plt.close(fig)

    def test_source_note(self):
        fig, ax = plt.subplots()
        typography.source_note(ax, 'Done by Atlanta University, 1900')
        plt.close(fig)

    def test_format_label_uppercase(self):
        result = typography.format_label('hello world')
        assert result == 'HELLO WORLD'

    def test_format_label_no_uppercase(self):
        result = typography.format_label('Hello World', uppercase=False)
        assert result == 'Hello World'

    def test_format_label_wrap(self):
        result = typography.format_label('a very long title text', wrap_width=12)
        assert '\n' in result

    def test_plate_number(self):
        fig, ax = plt.subplots()
        typography.plate_number(ax, 11)
        plt.close(fig)

    def test_plate_number_positions(self):
        for pos in ['top-right', 'top-left', 'bottom-right', 'bottom-left']:
            fig, ax = plt.subplots()
            typography.plate_number(ax, 1, position=pos)
            plt.close(fig)

    def test_plate_number_invalid_position(self):
        fig, ax = plt.subplots()
        with pytest.raises(ValueError):
            typography.plate_number(ax, 1, position='middle')
        plt.close(fig)


class TestWrappedBar:
    """Tests for wrapped/snake bar charts."""

    def setup_method(self):
        plt.close('all')

    def test_wrapped_bar(self):
        fig, ax = wrapped.wrapped_bar(
            ['Agriculture', 'Domestic', 'Manufacturing', 'Trade'],
            [62, 28, 5, 4],
        )
        assert fig is not None
        plt.close(fig)

    def test_wrapped_bar_with_title(self):
        fig, ax = wrapped.wrapped_bar(
            ['A', 'B', 'C'],
            [50, 30, 20],
            title='Test Chart',
        )
        assert ax.get_title() == 'TEST CHART'
        plt.close(fig)

    def test_wrapped_bar_counterclockwise(self):
        fig, ax = wrapped.wrapped_bar(
            ['A', 'B', 'C'],
            [40, 30, 20],
            direction='counterclockwise',
        )
        assert fig is not None
        plt.close(fig)

    def test_wrapped_bar_no_values(self):
        fig, ax = wrapped.wrapped_bar(
            ['A', 'B'],
            [60, 40],
            show_values=False,
        )
        assert fig is not None
        plt.close(fig)

    def test_snake_bar(self):
        fig, ax = wrapped.snake_bar(
            ['Georgia', 'Virginia', 'Mississippi'],
            {'City': [16, 18, 6], 'Rural': [84, 82, 94]},
        )
        assert fig is not None
        plt.close(fig)

    def test_snake_bar_with_title(self):
        fig, ax = wrapped.snake_bar(
            ['A', 'B'],
            {'X': [30, 40], 'Y': [70, 60]},
            title='Population',
        )
        assert ax.get_title() == 'POPULATION'
        plt.close(fig)


class TestPictorial:
    """Tests for pictorial/icon grid charts."""

    def setup_method(self):
        plt.close('all')

    def test_icon_grid(self):
        fig, ax = pictorial.icon_grid(
            {'Illiterate': 44, 'Literate': 56},
        )
        assert fig is not None
        plt.close(fig)

    def test_icon_grid_with_title(self):
        fig, ax = pictorial.icon_grid(
            {'A': 30, 'B': 70},
            title='Illiteracy Rate',
        )
        assert ax.get_title() == 'ILLITERACY RATE'
        plt.close(fig)

    def test_icon_grid_circles(self):
        fig, ax = pictorial.icon_grid(
            {'A': 50, 'B': 50},
            shape='circle',
        )
        assert fig is not None
        plt.close(fig)

    def test_icon_grid_custom_total(self):
        fig, ax = pictorial.icon_grid(
            {'A': 25, 'B': 75},
            total=50,
            ncols=10,
        )
        assert fig is not None
        plt.close(fig)

    def test_icon_grid_three_groups(self):
        fig, ax = pictorial.icon_grid(
            {'Agriculture': 62, 'Domestic': 28, 'Other': 10},
        )
        assert fig is not None
        plt.close(fig)

    def test_icon_grid_no_legend(self):
        fig, ax = pictorial.icon_grid(
            {'A': 40, 'B': 60},
            show_legend=False,
        )
        assert fig is not None
        plt.close(fig)

    def test_pictograph_row(self):
        fig, ax = pictorial.pictograph_row(
            {'Black': 89, 'Mulatto': 11},
        )
        assert fig is not None
        plt.close(fig)

    def test_pictograph_row_with_title(self):
        fig, ax = pictorial.pictograph_row(
            {'A': 60, 'B': 40},
            title='Composition',
        )
        assert ax.get_title() == 'COMPOSITION'
        plt.close(fig)

    def test_pictograph_row_three_groups(self):
        fig, ax = pictorial.pictograph_row(
            {'A': 50, 'B': 30, 'C': 20},
        )
        assert fig is not None
        plt.close(fig)


class TestLayouts:
    """Tests for multi-panel layout system."""

    def setup_method(self):
        plt.close('all')

    def test_dubois_plate_basic(self):
        plate = layouts.DuBoisPlate(1, 2, title='Test Plate')
        ax1 = plate.get_axes(0, 0)
        ax2 = plate.get_axes(0, 1)
        assert ax1 is not None
        assert ax2 is not None
        plate.close()

    def test_dubois_plate_with_number(self):
        plate = layouts.DuBoisPlate(1, 1, title='Test',
                                     plate_number=11)
        ax = plate.get_axes(0, 0)
        assert ax is not None
        plate.close()

    def test_dubois_plate_spanning(self):
        plate = layouts.DuBoisPlate(2, 2, title='Grid')
        ax_full = plate.get_axes(1, 0, rowspan=1, colspan=2)
        assert ax_full is not None
        plate.close()

    def test_dubois_plate_panel_title(self):
        plate = layouts.DuBoisPlate(1, 2)
        plate.add_panel_title(0, 0, 'Panel A')
        plate.close()

    def test_dubois_plate_figure_property(self):
        plate = layouts.DuBoisPlate(1, 1)
        assert plate.figure is not None
        plate.close()

    def test_plate_layout_function(self):
        fig, axes = layouts.plate_layout(
            [{'position': (0, 0), 'title': 'Chart A'},
             {'position': (0, 1), 'title': 'Chart B'}],
            title='Test Layout',
        )
        assert fig is not None
        assert len(axes) == 2
        plt.close(fig)

    def test_plate_layout_spanning(self):
        fig, axes = layouts.plate_layout(
            [{'position': (0, 0), 'title': 'Top Left'},
             {'position': (0, 1), 'title': 'Top Right'},
             {'position': (1, 0, 1, 2), 'title': 'Bottom Full'}],
            title='Complex Layout',
        )
        assert len(axes) == 3
        plt.close(fig)


class TestPhase3Imports:
    """Test that all new modules are importable."""

    def test_import_typography(self):
        from dubois import typography
        assert hasattr(typography, 'title_block')
        assert hasattr(typography, 'annotate')
        assert hasattr(typography, 'source_note')
        assert hasattr(typography, 'format_label')
        assert hasattr(typography, 'plate_number')

    def test_import_layouts(self):
        from dubois import layouts
        assert hasattr(layouts, 'DuBoisPlate')
        assert hasattr(layouts, 'plate_layout')

    def test_import_wrapped(self):
        from dubois.charts.wrapped import wrapped_bar, snake_bar
        assert callable(wrapped_bar)
        assert callable(snake_bar)

    def test_import_pictorial(self):
        from dubois.charts.pictorial import icon_grid, pictograph_row
        assert callable(icon_grid)
        assert callable(pictograph_row)

    def test_charts_init_has_new_modules(self):
        from dubois import charts
        assert hasattr(charts, 'wrapped')
        assert hasattr(charts, 'pictorial')
