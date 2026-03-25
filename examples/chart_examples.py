"""
Du Bois Chart Type Examples

Demonstrates each specialized chart type using data inspired by
W.E.B. Du Bois' 1900 Paris Exposition visualizations.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

import dubois
from dubois.charts import bar, area, butterfly, spiral


def example_1_dubois_bar():
    """Horizontal bar chart: Occupations of Georgia Negroes, 1900."""
    dubois.set_theme('classic')

    fig, ax = bar.bar(
        ['Agriculture', 'Domestic and Personal Service',
         'Manufacturing and Mechanical', 'Trade and Transportation',
         'Professions'],
        [62, 28, 5, 4, 1],
        title='Occupations of Georgia Negroes',
        subtitle='Done by Atlanta University, 1900',
        label_format='{:.0f}%',
    )
    fig.savefig(f'{OUTPUT_DIR}/example_bar.png', dpi=200)
    print("Saved example_bar.png")
    dubois.reset_theme()


def example_2_grouped_bar():
    """Grouped bar chart: Comparing occupations across decades."""
    dubois.set_theme('classic')

    fig, ax = bar.grouped_bar(
        ['Agriculture', 'Manufacturing', 'Domestic Service', 'Professions'],
        {
            '1890': [57, 6, 31, 1],
            '1900': [53, 8, 33, 2],
        },
        title='Occupations Over Time',
        subtitle='Shift in Negro Employment, Georgia',
        label_format='{:.0f}%',
    )
    fig.savefig(f'{OUTPUT_DIR}/example_grouped_bar.png', dpi=200)
    print("Saved example_grouped_bar.png")
    dubois.reset_theme()


def example_3_stacked_bar():
    """Stacked bar chart: Population distribution by state."""
    dubois.set_theme('classic')

    fig, ax = bar.stacked_bar(
        ['Georgia', 'Virginia', 'Mississippi', 'Alabama',
         'S. Carolina', 'N. Carolina'],
        {
            'City': [16, 18, 6, 10, 8, 7],
            'Rural': [84, 82, 94, 90, 92, 93],
        },
        colors=[dubois.colors.crimson, dubois.colors.DUBOIS_EXTENDED['gold']],
        title='City and Rural Population by State',
        subtitle='Colored Population of the United States, 1890',
        label_format='{:.0f}%',
    )
    fig.savefig(f'{OUTPUT_DIR}/example_stacked_bar.png', dpi=200)
    print("Saved example_stacked_bar.png")
    dubois.reset_theme()


def example_4_area():
    """Area chart: Proportion of Freemen and Slaves."""
    dubois.set_theme('classic')

    years = [1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870]
    fig, ax = area.proportional_area(
        years,
        {
            'Slaves': [92, 89, 86, 87, 86, 87, 88, 89, 0],
            'Free': [8, 11, 14, 13, 14, 13, 12, 11, 100],
        },
        colors=[dubois.colors.crimson, dubois.colors.DUBOIS_EXTENDED['green']],
        title='Proportion of Freemen and Slaves\nAmong American Negroes',
        annotations={1865: 'Emancipation'},
    )
    fig.savefig(f'{OUTPUT_DIR}/example_area.png', dpi=200)
    print("Saved example_area.png")
    dubois.reset_theme()


def example_5_butterfly():
    """Butterfly chart: Age distribution comparison."""
    dubois.set_theme('classic')

    fig, ax = butterfly.butterfly(
        ['Under 10', '10-20', '20-30', '30-40',
         '40-50', '50-60', '60-70', 'Over 70'],
        [18, 20, 17, 14, 12, 9, 6, 4],
        [16, 18, 19, 15, 13, 10, 6, 3],
        left_label='Negroes',
        right_label='Whites',
        title='Comparative Age Distribution',
        subtitle='United States, 1890',
        label_format='{:.0f}%',
    )
    fig.savefig(f'{OUTPUT_DIR}/example_butterfly.png', dpi=200)
    print("Saved example_butterfly.png")
    dubois.reset_theme()


def example_6_comparison():
    """Dot comparison chart: Progress indicators."""
    dubois.set_theme('classic')

    fig, ax = butterfly.comparison(
        ['Literacy Rate', 'Land Ownership', 'Business Owners',
         'School Enrollment', 'College Graduates'],
        [30, 12, 2, 34, 0.3],
        [57, 21, 5, 54, 1.2],
        label_a='1880',
        label_b='1900',
        title='Negro Progress Since Emancipation',
    )
    fig.savefig(f'{OUTPUT_DIR}/example_comparison.png', dpi=200)
    print("Saved example_comparison.png")
    dubois.reset_theme()


def example_7_spiral():
    """Spiral chart: City and Rural Population (Plate 11 style)."""
    dubois.set_theme('classic')

    fig, ax = spiral.spiral(
        ['Georgia', 'Virginia', 'Mississippi', 'S. Carolina',
         'Alabama', 'Louisiana', 'N. Carolina', 'Tennessee',
         'Kentucky', 'Maryland'],
        [16, 18, 6, 8, 10, 22, 7, 15, 20, 38],
        label_a='City',
        label_b='Rural',
        color_a=dubois.colors.crimson,
        color_b=dubois.colors.DUBOIS_EXTENDED['gold'],
        title='City and Rural Population',
        subtitle='Colored Population of the United States, 1890',
    )
    fig.savefig(f'{OUTPUT_DIR}/example_spiral.png', dpi=200)
    print("Saved example_spiral.png")
    dubois.reset_theme()


def example_8_concentric_rings():
    """Concentric rings: Progress indicators as proportions."""
    dubois.set_theme('classic')

    fig, ax = spiral.concentric_rings(
        ['Literacy', 'School Enrollment', 'Land Ownership',
         'Home Ownership', 'Business Proprietors'],
        [57, 54, 21, 19, 5],
        title='Negro Progress Indicators',
        subtitle='Percentage Achieved by 1900',
    )
    fig.savefig(f'{OUTPUT_DIR}/example_rings.png', dpi=200)
    print("Saved example_rings.png")
    dubois.reset_theme()


if __name__ == '__main__':
    print("Generating Du Bois chart examples...\n")

    example_1_dubois_bar()
    example_2_grouped_bar()
    example_3_stacked_bar()
    example_4_area()
    example_5_butterfly()
    example_6_comparison()
    example_7_spiral()
    example_8_concentric_rings()

    print("\nAll examples generated!")
