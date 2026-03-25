"""
Du Bois Plate Gallery

Recreations of specific plates from W.E.B. Du Bois' 1900 Paris Exposition
using dubois-viz. Each function recreates one plate
as faithfully as possible with the available chart types.

These are interpretive recreations — the original plates were hand-painted
with gouache and ink. This gallery captures their spirit and data while
using modern tools.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

import matplotlib.pyplot as plt
import dubois
from dubois import typography, layouts
from dubois.charts import bar, area, butterfly, spiral, pictorial, wrapped


def plate_11_city_rural():
    """
    Plate 11: City and Rural Population. 1890.

    Original: A spiral showing the proportion of African Americans
    living in cities vs rural areas across states.
    """
    dubois.set_theme('classic')

    fig, ax = spiral.spiral(
        ['Georgia', 'Virginia', 'Mississippi', 'South Carolina',
         'Alabama', 'Louisiana', 'North Carolina', 'Tennessee',
         'Kentucky', 'Maryland', 'Texas', 'Arkansas'],
        [16, 18, 6, 8, 10, 22, 7, 15, 20, 38, 12, 5],
        label_a='City', label_b='Rural',
        color_a=dubois.colors.crimson,
        color_b=dubois.colors.DUBOIS_EXTENDED['gold'],
        title='City and Rural Population',
        subtitle='1890',
        ring_width=0.06,
        ring_gap=0.015,
    )
    typography.plate_number(ax, 11, position='top-left')
    fig.savefig(f'{OUTPUT_DIR}/gallery_plate11.png', dpi=250)
    print("  Plate 11: City and Rural Population")
    dubois.reset_theme()


def plate_25_occupations():
    """
    Plate 25: Occupations of Negroes and Whites in Georgia.

    Original: Horizontal stacked bars comparing occupations
    between racial groups.
    """
    dubois.set_theme('classic')

    fig, ax = butterfly.butterfly(
        ['Agriculture', 'Domestic & Personal Service',
         'Manufacturing & Mechanical', 'Trade & Transportation',
         'Professions'],
        [62, 28, 5, 4, 1],
        [22, 12, 20, 18, 4],
        left_label='Negroes',
        right_label='Whites',
        left_color=dubois.colors.crimson,
        right_color=dubois.colors.DUBOIS_EXTENDED['blue'],
        title='Occupations of Negroes and Whites in Georgia',
        label_format='{:.0f}%',
    )
    typography.plate_number(ax, 25, position='top-left')
    fig.savefig(f'{OUTPUT_DIR}/gallery_plate25.png', dpi=250)
    print("  Plate 25: Occupations of Negroes and Whites")
    dubois.reset_theme()


def plate_31_freemen_slaves():
    """
    Plate 31: Proportion of Freemen and Slaves Among American Negroes.

    Original: A stacked area chart showing how the proportion shifted
    from 1790 to 1870, with a dramatic change at emancipation.
    """
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
        subtitle='1790 - 1870',
        annotations={1865: 'Emancipation'},
    )
    typography.plate_number(ax, 31, position='top-left')
    typography.source_note(ax, 'Done by Atlanta University')
    fig.savefig(f'{OUTPUT_DIR}/gallery_plate31.png', dpi=250)
    print("  Plate 31: Proportion of Freemen and Slaves")
    dubois.reset_theme()


def plate_39_illiteracy():
    """
    Plate 39: Illiteracy.

    Original: Grid-style visualization of illiteracy rates,
    showing the decrease over time.
    """
    dubois.set_theme('classic')

    plate = layouts.DuBoisPlate(
        1, 3,
        title='Illiteracy of American Negroes Compared With That of Other Nations',
        theme='classic',
        plate_number=39,
        figsize=(16, 6),
    )

    # 1870
    ax1 = plate.get_axes(0, 0)
    pictorial.icon_grid(
        {'Illiterate': 80, 'Literate': 20},
        colors=[dubois.colors.crimson, dubois.colors.DUBOIS_EXTENDED['green']],
        total=100, ncols=10, cell_size=0.35, cell_gap=0.04,
        show_legend=False, ax=ax1,
    )
    ax1.set_title('1870', fontsize=12, fontweight='bold')

    # 1880
    ax2 = plate.get_axes(0, 1)
    pictorial.icon_grid(
        {'Illiterate': 70, 'Literate': 30},
        colors=[dubois.colors.crimson, dubois.colors.DUBOIS_EXTENDED['green']],
        total=100, ncols=10, cell_size=0.35, cell_gap=0.04,
        show_legend=False, ax=ax2,
    )
    ax2.set_title('1880', fontsize=12, fontweight='bold')

    # 1900
    ax3 = plate.get_axes(0, 2)
    pictorial.icon_grid(
        {'Illiterate': 44, 'Literate': 56},
        colors=[dubois.colors.crimson, dubois.colors.DUBOIS_EXTENDED['green']],
        total=100, ncols=10, cell_size=0.35, cell_gap=0.04,
        show_legend=True, ax=ax3,
    )
    ax3.set_title('1900', fontsize=12, fontweight='bold')

    plate.save(f'{OUTPUT_DIR}/gallery_plate39.png', dpi=250)
    print("  Plate 39: Illiteracy")
    plate.close()


def plate_47_progress():
    """
    Plate 47: A series showing Negro progress since emancipation.

    A multi-panel plate combining bar charts and comparison data
    to demonstrate economic and social advancement.
    """
    plate = layouts.DuBoisPlate(
        2, 2,
        title='The Rise of the Negroes from Slavery to Freedom in One Generation',
        subtitle='A study of Negro progress since emancipation',
        theme='classic',
        plate_number=47,
    )

    # Panel 1: Literacy over time
    ax1 = plate.get_axes(0, 0)
    years = [1860, 1870, 1880, 1890, 1900]
    literacy = [5, 20, 30, 43, 57]
    ax1.fill_between(years, literacy, color=dubois.colors.crimson, alpha=0.3)
    ax1.plot(years, literacy, color=dubois.colors.crimson, linewidth=2.5, marker='o')
    ax1.set_title('LITERACY RATE', fontsize=11, fontweight='bold')
    ax1.set_ylabel('%')
    ax1.set_ylim(0, 70)

    # Panel 2: Property ownership
    ax2 = plate.get_axes(0, 1)
    bar.bar(
        ['1870', '1880', '1890', '1900'],
        [0.5, 6, 12, 20],
        colors=[dubois.colors.DUBOIS_EXTENDED['gold']] * 4,
        label_format='${:.0f}M',
        ax=ax2,
    )
    ax2.set_title('PROPERTY OWNED', fontsize=11, fontweight='bold')

    # Panel 3: Education (full width)
    ax3 = plate.get_axes(1, 0)
    ax3.barh(['Common Schools', 'High Schools', 'Colleges'],
             [28000, 150, 34],
             color=[dubois.colors.crimson, dubois.colors.DUBOIS_EXTENDED['gold'],
                    dubois.colors.DUBOIS_EXTENDED['green']],
             edgecolor='black', linewidth=1.2)
    ax3.set_title('NEGRO SCHOOLS AND COLLEGES, 1900', fontsize=11, fontweight='bold')

    # Panel 4: Occupations
    ax4 = plate.get_axes(1, 1)
    pictorial.pictograph_row(
        {'Agriculture': 53, 'Domestic': 31, 'Manufacturing': 8,
         'Trade': 5, 'Professions': 3},
        ax=ax4,
    )
    ax4.set_title('OCCUPATIONS, 1900', fontsize=11, fontweight='bold')

    plate.save(f'{OUTPUT_DIR}/gallery_plate47.png', dpi=250)
    print("  Plate 47: Rise of the Negroes")
    plate.close()


def plate_54_population_comparison():
    """
    Plate 54: The Amalgamation of the White and Black
    Elements of the Population.

    Using concentric rings to show demographic breakdown.
    """
    dubois.set_theme('classic')

    fig, ax = spiral.concentric_rings(
        ['Georgia Negro Population',
         'Virginia Negro Population',
         'Mississippi Negro Population',
         'South Carolina Negro Population',
         'Alabama Negro Population',
         'North Carolina Negro Population',
         'Louisiana Negro Population'],
        [47, 38, 59, 60, 48, 33, 50],
        title='Negro Population as a Percentage of Total',
        subtitle='In the Former Slave States, 1890',
        value_format='{:.0f}%',
        ring_width=0.10,
        ring_gap=0.02,
    )
    typography.plate_number(ax, 54, position='top-left')
    fig.savefig(f'{OUTPUT_DIR}/gallery_plate54.png', dpi=250)
    print("  Plate 54: Population Comparison")
    dubois.reset_theme()


if __name__ == '__main__':
    print("Generating Du Bois Plate Gallery...\n")

    plate_11_city_rural()
    plate_25_occupations()
    plate_31_freemen_slaves()
    plate_39_illiteracy()
    plate_47_progress()
    plate_54_population_comparison()

    print(f"\nGallery complete! See {OUTPUT_DIR}/")
