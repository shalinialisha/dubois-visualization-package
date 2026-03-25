"""
Phase 3 Examples: Typography, Wrapped Bars, Pictorial Charts, Layouts

Demonstrates the new modules added in Phase 3 using data inspired by
W.E.B. Du Bois' 1900 Paris Exposition visualizations.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

import matplotlib.pyplot as plt
import dubois
from dubois import typography, layouts
from dubois.charts import wrapped, pictorial, bar, butterfly


def example_1_wrapped_bar():
    """Circular wrapped bar chart: Occupations."""
    dubois.set_theme('classic')

    fig, ax = wrapped.wrapped_bar(
        ['Agriculture', 'Domestic Service', 'Manufacturing',
         'Trade & Transport', 'Professions', 'Other'],
        [62, 28, 5, 4, 1, 0.5],
        title='Occupations of Georgia Negroes',
        subtitle='Done by Atlanta University, 1900',
        value_format='{:.0f}%',
    )
    fig.savefig(f'{OUTPUT_DIR}/example_wrapped.png', dpi=200)
    print("Saved example_wrapped.png")
    dubois.reset_theme()


def example_2_snake_bar():
    """Snake bar chart: City vs Rural by state."""
    dubois.set_theme('classic')

    fig, ax = wrapped.snake_bar(
        ['Georgia', 'Virginia', 'Mississippi', 'S. Carolina',
         'Alabama', 'Louisiana'],
        {
            'City': [16, 18, 6, 8, 10, 22],
            'Rural': [84, 82, 94, 92, 90, 78],
        },
        colors=[dubois.colors.crimson, dubois.colors.DUBOIS_EXTENDED['gold']],
        title='City and Rural Population',
        subtitle='Colored Population, 1890',
    )
    fig.savefig(f'{OUTPUT_DIR}/example_snake.png', dpi=200)
    print("Saved example_snake.png")
    dubois.reset_theme()


def example_3_icon_grid():
    """Icon grid (waffle) chart: Illiteracy rates."""
    dubois.set_theme('classic')

    fig, ax = pictorial.icon_grid(
        {'Illiterate': 44, 'Literate': 56},
        colors=[dubois.colors.crimson, dubois.colors.DUBOIS_EXTENDED['green']],
        title='Illiteracy Among American Negroes',
        subtitle='1900 Census Data',
    )
    fig.savefig(f'{OUTPUT_DIR}/example_icon_grid.png', dpi=200)
    print("Saved example_icon_grid.png")
    dubois.reset_theme()


def example_4_icon_grid_circles():
    """Circle icon grid: Population composition."""
    dubois.set_theme('classic')

    fig, ax = pictorial.icon_grid(
        {'Agriculture': 62, 'Domestic': 28, 'Manufacturing': 5, 'Other': 5},
        shape='circle',
        title='Occupations of Negroes',
        subtitle='Georgia, 1900',
    )
    fig.savefig(f'{OUTPUT_DIR}/example_icon_circles.png', dpi=200)
    print("Saved example_icon_circles.png")
    dubois.reset_theme()


def example_5_pictograph_row():
    """Pictograph row: Racial composition."""
    dubois.set_theme('classic')

    fig, ax = pictorial.pictograph_row(
        {'Black': 80, 'Mulatto': 15, 'Other': 5},
        colors=[dubois.colors.black,
                dubois.colors.DUBOIS_EXTENDED['brown'],
                dubois.colors.tan],
        title='Racial Composition',
        subtitle='Georgia, 1900',
    )
    fig.savefig(f'{OUTPUT_DIR}/example_pictograph.png', dpi=200)
    print("Saved example_pictograph.png")
    dubois.reset_theme()


def example_6_typography():
    """Typography utilities demonstration."""
    dubois.set_theme('classic')

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot([1870, 1880, 1890, 1900], [20, 35, 47, 57],
            color=dubois.colors.crimson, linewidth=3, marker='o')
    ax.fill_between([1870, 1880, 1890, 1900], [20, 35, 47, 57],
                    alpha=0.3, color=dubois.colors.crimson)

    typography.title_block(ax,
                           'Literacy Among American Negroes',
                           subtitle='Percentage Who Can Read and Write',
                           caption='Done by Atlanta University, 1900')
    typography.annotate(ax, 'Rapid Growth', xy=(1890, 47),
                        xytext=(1882, 52))
    typography.source_note(ax, 'Source: United States Census Bureau')
    typography.plate_number(ax, 31)

    ax.set_xlabel('Year')
    ax.set_ylabel('Literacy Rate (%)')

    fig.savefig(f'{OUTPUT_DIR}/example_typography.png', dpi=200)
    print("Saved example_typography.png")
    dubois.reset_theme()


def example_7_multi_panel():
    """Multi-panel plate layout."""
    plate = layouts.DuBoisPlate(
        2, 2,
        title='The Georgia Negro: A Social Study',
        subtitle='Prepared for the Paris Exposition of 1900',
        theme='classic',
        plate_number=42,
    )

    # Panel 1: Bar chart
    ax1 = plate.get_axes(0, 0)
    cats = ['Agriculture', 'Domestic', 'Manufacturing', 'Professions']
    vals = [62, 28, 5, 5]
    colors = dubois.get_categorical(4)
    ax1.barh(cats, vals, color=colors, edgecolor='black', linewidth=1.2)
    ax1.set_title('OCCUPATIONS', fontsize=11, fontweight='bold')
    ax1.invert_yaxis()

    # Panel 2: Butterfly chart
    ax2 = plate.get_axes(0, 1)
    butterfly.butterfly(
        ['Under 20', '20-40', '40-60', 'Over 60'],
        [35, 30, 22, 13],
        [32, 33, 23, 12],
        left_label='1890', right_label='1900',
        ax=ax2,
    )
    ax2.set_title('AGE DISTRIBUTION', fontsize=11, fontweight='bold')

    # Panel 3: Full-width pictograph row
    ax3 = plate.get_axes(1, 0, colspan=2)
    pictorial.pictograph_row(
        {'Illiterate': 44, 'Literate': 56},
        colors=[dubois.colors.crimson, dubois.colors.DUBOIS_EXTENDED['green']],
        ax=ax3,
    )
    ax3.set_title('ILLITERACY RATE, 1900', fontsize=11, fontweight='bold')

    plate.save(f'{OUTPUT_DIR}/example_plate.png', dpi=200)
    print("Saved example_plate.png")
    plate.close()


if __name__ == '__main__':
    print("Generating Phase 3 examples...\n")

    example_1_wrapped_bar()
    example_2_snake_bar()
    example_3_icon_grid()
    example_4_icon_grid_circles()
    example_5_pictograph_row()
    example_6_typography()
    example_7_multi_panel()

    print("\nAll Phase 3 examples generated!")
