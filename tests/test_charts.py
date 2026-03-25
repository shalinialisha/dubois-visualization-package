"""
Tests for Du Bois chart types.
"""

import pytest
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for testing
import matplotlib.pyplot as plt

from dubois.charts import bar, area, butterfly, spiral


class TestBarChart:
    """Tests for bar chart module."""

    def setup_method(self):
        plt.close('all')

    def test_basic_bar(self):
        fig, ax = bar.bar(
            ['A', 'B', 'C'],
            [10, 20, 30],
        )
        assert fig is not None
        assert ax is not None
        plt.close(fig)

    def test_bar_with_title(self):
        fig, ax = bar.bar(
            ['Agriculture', 'Domestic', 'Manufacturing'],
            [62, 28, 5],
            title='Occupations',
            subtitle='Georgia, 1900',
        )
        assert ax.get_title() == 'OCCUPATIONS'
        plt.close(fig)

    def test_bar_vertical(self):
        fig, ax = bar.bar(
            ['A', 'B', 'C'],
            [10, 20, 30],
            orientation='vertical',
        )
        assert fig is not None
        plt.close(fig)

    def test_bar_custom_colors(self):
        fig, ax = bar.bar(
            ['A', 'B'],
            [10, 20],
            colors=['#DC143C', '#D4AF37'],
        )
        assert fig is not None
        plt.close(fig)

    def test_bar_no_value_labels(self):
        fig, ax = bar.bar(
            ['A', 'B'],
            [10, 20],
            value_labels=False,
        )
        assert fig is not None
        plt.close(fig)

    def test_bar_on_existing_axes(self):
        fig, ax = plt.subplots()
        fig2, ax2 = bar.bar(
            ['A', 'B'],
            [10, 20],
            ax=ax,
        )
        assert ax2 is ax
        plt.close(fig)

    def test_grouped_bar(self):
        fig, ax = bar.grouped_bar(
            ['Agriculture', 'Manufacturing', 'Professions'],
            {'1890': [62, 5, 3], '1900': [55, 8, 5]},
        )
        assert fig is not None
        plt.close(fig)

    def test_grouped_bar_vertical(self):
        fig, ax = bar.grouped_bar(
            ['A', 'B', 'C'],
            {'X': [10, 20, 30], 'Y': [15, 25, 35]},
            orientation='vertical',
        )
        assert fig is not None
        plt.close(fig)

    def test_stacked_bar(self):
        fig, ax = bar.stacked_bar(
            ['State A', 'State B', 'State C'],
            {'Free': [20, 30, 40], 'Enslaved': [80, 70, 60]},
        )
        assert fig is not None
        plt.close(fig)

    def test_stacked_bar_with_total(self):
        fig, ax = bar.stacked_bar(
            ['A', 'B'],
            {'X': [30, 40], 'Y': [70, 60]},
            show_total=True,
        )
        assert fig is not None
        plt.close(fig)

    def test_stacked_bar_vertical(self):
        fig, ax = bar.stacked_bar(
            ['A', 'B'],
            {'X': [30, 40], 'Y': [70, 60]},
            orientation='vertical',
        )
        assert fig is not None
        plt.close(fig)


class TestAreaChart:
    """Tests for area chart module."""

    def setup_method(self):
        plt.close('all')

    def test_basic_area(self):
        fig, ax = area.area(
            [1800, 1850, 1900],
            {'Free': [10, 30, 100], 'Enslaved': [90, 70, 0]},
        )
        assert fig is not None
        plt.close(fig)

    def test_area_normalized(self):
        fig, ax = area.area(
            [1800, 1850, 1900],
            {'Free': [10, 30, 100], 'Enslaved': [90, 70, 0]},
            normalized=True,
        )
        assert fig is not None
        plt.close(fig)

    def test_area_not_stacked(self):
        fig, ax = area.area(
            [1800, 1850, 1900],
            {'A': [10, 30, 50], 'B': [20, 40, 60]},
            stacked=False,
        )
        assert fig is not None
        plt.close(fig)

    def test_area_with_annotations(self):
        fig, ax = area.area(
            [1800, 1850, 1900],
            {'Free': [10, 30, 100], 'Enslaved': [90, 70, 0]},
            annotations={1850: 'Key Event'},
        )
        assert fig is not None
        plt.close(fig)

    def test_area_with_title(self):
        fig, ax = area.area(
            [1800, 1850, 1900],
            {'Free': [10, 30, 100]},
            title='Test Title',
            subtitle='Subtitle here',
        )
        assert ax.get_title() == 'TEST TITLE'
        plt.close(fig)

    def test_proportional_area(self):
        fig, ax = area.proportional_area(
            [1800, 1850, 1900],
            {'Free': [10, 30, 100], 'Enslaved': [90, 70, 0]},
            title='Proportion of Freemen',
        )
        assert fig is not None
        plt.close(fig)


class TestButterflyChart:
    """Tests for butterfly chart module."""

    def setup_method(self):
        plt.close('all')

    def test_basic_butterfly(self):
        fig, ax = butterfly.butterfly(
            ['Under 15', '15-40', '40-70', 'Over 70'],
            [30, 35, 25, 10],
            [28, 38, 24, 10],
        )
        assert fig is not None
        plt.close(fig)

    def test_butterfly_with_labels(self):
        fig, ax = butterfly.butterfly(
            ['A', 'B', 'C'],
            [10, 20, 30],
            [15, 25, 35],
            left_label='1890',
            right_label='1900',
            title='Age Distribution',
        )
        assert ax.get_title() == 'AGE DISTRIBUTION'
        plt.close(fig)

    def test_butterfly_asymmetric(self):
        fig, ax = butterfly.butterfly(
            ['A', 'B'],
            [10, 20],
            [50, 60],
            symmetric=False,
        )
        assert fig is not None
        plt.close(fig)

    def test_butterfly_no_value_labels(self):
        fig, ax = butterfly.butterfly(
            ['A', 'B'],
            [10, 20],
            [15, 25],
            value_labels=False,
        )
        assert fig is not None
        plt.close(fig)

    def test_butterfly_custom_colors(self):
        fig, ax = butterfly.butterfly(
            ['A', 'B'],
            [10, 20],
            [15, 25],
            left_color='#00A550',
            right_color='#663399',
        )
        assert fig is not None
        plt.close(fig)

    def test_comparison_chart(self):
        fig, ax = butterfly.comparison(
            ['Literacy', 'Land', 'Business'],
            [30, 15, 5],
            [56, 22, 8],
            label_a='1890',
            label_b='1900',
        )
        assert fig is not None
        plt.close(fig)

    def test_comparison_with_title(self):
        fig, ax = butterfly.comparison(
            ['A', 'B', 'C'],
            [10, 20, 30],
            [15, 25, 35],
            title='Progress Over Time',
        )
        assert ax.get_title() == 'PROGRESS OVER TIME'
        plt.close(fig)


class TestSpiralChart:
    """Tests for spiral chart module."""

    def setup_method(self):
        plt.close('all')

    def test_basic_spiral(self):
        fig, ax = spiral.spiral(
            ['Georgia', 'Virginia', 'Mississippi'],
            [20, 18, 9],
        )
        assert fig is not None
        plt.close(fig)

    def test_spiral_with_both_values(self):
        fig, ax = spiral.spiral(
            ['State A', 'State B'],
            [30, 40],
            [70, 60],
            label_a='City',
            label_b='Rural',
        )
        assert fig is not None
        plt.close(fig)

    def test_spiral_with_title(self):
        fig, ax = spiral.spiral(
            ['A', 'B', 'C'],
            [20, 30, 40],
            title='Population Distribution',
        )
        assert ax.get_title() == 'POPULATION DISTRIBUTION'
        plt.close(fig)

    def test_spiral_custom_colors(self):
        fig, ax = spiral.spiral(
            ['A', 'B'],
            [25, 35],
            color_a='#00A550',
            color_b='#000000',
        )
        assert fig is not None
        plt.close(fig)

    def test_spiral_many_rings(self):
        cats = [f'State {i}' for i in range(10)]
        vals = [10 + i * 5 for i in range(10)]
        fig, ax = spiral.spiral(cats, vals)
        assert fig is not None
        plt.close(fig)

    def test_concentric_rings(self):
        fig, ax = spiral.concentric_rings(
            ['Literacy', 'Land Ownership', 'Business', 'Education'],
            [56, 19, 5, 33],
        )
        assert fig is not None
        plt.close(fig)

    def test_concentric_rings_with_title(self):
        fig, ax = spiral.concentric_rings(
            ['A', 'B', 'C'],
            [50, 75, 25],
            title='Progress Indicators',
        )
        assert ax.get_title() == 'PROGRESS INDICATORS'
        plt.close(fig)

    def test_concentric_rings_custom_max(self):
        fig, ax = spiral.concentric_rings(
            ['A', 'B'],
            [500, 800],
            max_value=1000,
        )
        assert fig is not None
        plt.close(fig)


class TestChartsImport:
    """Test that all chart modules are importable."""

    def test_import_charts(self):
        from dubois import charts
        assert hasattr(charts, 'bar')
        assert hasattr(charts, 'area')
        assert hasattr(charts, 'butterfly')
        assert hasattr(charts, 'spiral')

    def test_import_bar_functions(self):
        from dubois.charts.bar import bar, grouped_bar, stacked_bar
        assert callable(bar)
        assert callable(grouped_bar)
        assert callable(stacked_bar)

    def test_import_area_functions(self):
        from dubois.charts.area import area, proportional_area
        assert callable(area)
        assert callable(proportional_area)

    def test_import_butterfly_functions(self):
        from dubois.charts.butterfly import butterfly, comparison
        assert callable(butterfly)
        assert callable(comparison)

    def test_import_spiral_functions(self):
        from dubois.charts.spiral import spiral, concentric_rings
        assert callable(spiral)
        assert callable(concentric_rings)
