"""
Test dubois-viz with real W.E.B. Du Bois data from the 1900 Paris Exposition.

Datasets from TidyTuesday Du Bois Challenge (2021):
https://github.com/rfordatascience/tidytuesday/tree/master/data/2021/2021-02-16

This script exercises every chart type to confirm the package works
with authentic historical data.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import csv
import matplotlib.pyplot as plt
import dubois
from dubois.charts import bar, area, butterfly, spiral, wrapped, pictorial
from dubois import typography

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output', 'real_data')
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_csv(filename):
    """Load a CSV file and return headers + rows."""
    path = os.path.join(DATA_DIR, filename)
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return rows


# ──────────────────────────────────────────────────────────────
# 1. BAR CHART — City/Rural population distribution
# ──────────────────────────────────────────────────────────────
def test_bar_city_rural():
    dubois.set_theme('classic')
    rows = load_csv('city_rural.csv')
    categories = [r['Category'] for r in rows]
    values = [int(r['Population']) for r in rows]

    fig, ax = bar.bar(
        categories, values,
        title='City and Rural Population',
        subtitle='Among American Negroes in Georgia, 1890',
        label_format='{:,.0f}',
    )
    fig.savefig(f'{OUTPUT_DIR}/bar_city_rural.png', dpi=200)
    plt.close(fig)
    print("  [OK] Bar chart — City/Rural population")


# ──────────────────────────────────────────────────────────────
# 2. GROUPED BAR — Occupation by race
# ──────────────────────────────────────────────────────────────
def test_grouped_bar_occupation():
    dubois.set_theme('classic')
    rows = load_csv('occupation.csv')

    # Split into two groups
    negro_rows = [r for r in rows if r['Group'] == 'Negroes']
    white_rows = [r for r in rows if r['Group'] == 'Whites']

    categories = [r['Occupation'] for r in negro_rows]
    # Shorten long names for readability
    short_names = [c.split(',')[0] if ',' in c else c for c in categories]

    negro_vals = [float(r['Percentage']) for r in negro_rows]
    white_vals = [float(r['Percentage']) for r in white_rows]

    fig, ax = bar.grouped_bar(
        short_names,
        {'Negroes': negro_vals, 'Whites': white_vals},
        title='Occupations in Georgia',
        subtitle='Compared by Race, 1900',
        label_format='{:.0f}%',
    )
    fig.savefig(f'{OUTPUT_DIR}/grouped_bar_occupation.png', dpi=200)
    plt.close(fig)
    print("  [OK] Grouped bar — Occupation by race")


# ──────────────────────────────────────────────────────────────
# 3. STACKED BAR — Household income spending
# ──────────────────────────────────────────────────────────────
def test_stacked_bar_income():
    dubois.set_theme('classic')
    rows = load_csv('income.csv')

    categories = [r['Class'] for r in rows]
    spending_keys = ['Rent', 'Food', 'Clothes', 'Tax', 'Other']
    groups = {}
    for key in spending_keys:
        vals = []
        for r in rows:
            v = r.get(key, '0') or '0'
            vals.append(float(v))
        groups[key] = vals

    fig, ax = bar.stacked_bar(
        categories, groups,
        title='Income and Expenditure',
        subtitle='Of 150 Negro Families in Atlanta, GA, 1900',
        label_format='{:.0f}%',
        show_total=False,
    )
    fig.savefig(f'{OUTPUT_DIR}/stacked_bar_income.png', dpi=200)
    plt.close(fig)
    print("  [OK] Stacked bar — Income spending")


# ──────────────────────────────────────────────────────────────
# 4. AREA CHART — Freed slaves over time
# ──────────────────────────────────────────────────────────────
def test_area_freed_slaves():
    dubois.set_theme('classic')
    rows = load_csv('freed_slaves.csv')

    years = [int(r['Year']) for r in rows]
    slave_pct = [float(r['Slave']) for r in rows]
    free_pct = [float(r['Free']) for r in rows]

    fig, ax = area.area(
        years,
        {'Enslaved': slave_pct, 'Free': free_pct},
        title='Proportion of Freemen and Slaves',
        subtitle='Among American Negroes, 1790-1870',
        stacked=True,
        normalized=True,
    )
    fig.savefig(f'{OUTPUT_DIR}/area_freed_slaves.png', dpi=200)
    plt.close(fig)
    print("  [OK] Area chart — Freed slaves")


# ──────────────────────────────────────────────────────────────
# 5. BUTTERFLY CHART — Georgia population comparison
# ──────────────────────────────────────────────────────────────
def test_butterfly_georgia_pop():
    dubois.set_theme('classic')
    rows = load_csv('georgia_pop.csv')

    # Skip the first two rows where both are 0
    rows = [r for r in rows if float(r['Colored']) > 0 or float(r['White']) > 0]
    years = [r['Year'] for r in rows]
    colored = [float(r['Colored']) for r in rows]
    white = [float(r['White']) for r in rows]

    fig, ax = butterfly.butterfly(
        years, colored, white,
        left_label='Colored', right_label='White',
        title='Comparative Increase of\nWhite and Colored Population of Georgia',
        label_format='{:.0f}%',
    )
    fig.savefig(f'{OUTPUT_DIR}/butterfly_georgia_pop.png', dpi=200)
    plt.close(fig)
    print("  [OK] Butterfly chart — Georgia population")


# ──────────────────────────────────────────────────────────────
# 6. COMPARISON CHART — Conjugal condition
# ──────────────────────────────────────────────────────────────
def test_comparison_conjugal():
    dubois.set_theme('classic')
    rows = load_csv('conjugal.csv')

    german = [r for r in rows if r['Population'] == 'Germany']
    negro = [r for r in rows if r['Population'] == 'Negroes']
    age_groups = [r['Age'] for r in german]

    german_single = [float(r['Single']) for r in german]
    negro_single = [float(r['Single']) for r in negro]

    fig, ax = butterfly.comparison(
        age_groups, german_single, negro_single,
        left_label='Germany (Single %)', right_label='Negroes (Single %)',
        title='Conjugal Condition',
        subtitle='Percentage Single, by Age Group',
        label_format='{:.1f}%',
    )
    fig.savefig(f'{OUTPUT_DIR}/comparison_conjugal.png', dpi=200)
    plt.close(fig)
    print("  [OK] Comparison chart — Conjugal condition")


# ──────────────────────────────────────────────────────────────
# 7. SPIRAL CHART — Freed slaves proportions
# ──────────────────────────────────────────────────────────────
def test_spiral_freed_slaves():
    dubois.set_theme('classic')
    rows = load_csv('freed_slaves.csv')

    years = [str(r['Year']) for r in rows]
    free_pct = [float(r['Free']) for r in rows]
    slave_pct = [float(r['Slave']) for r in rows]

    fig, ax = spiral.spiral(
        years, free_pct, slave_pct,
        title='Proportion of Freemen and Slaves',
        color_a=dubois.colors.DUBOIS_PRIMARY['crimson'],
        color_b=dubois.colors.DUBOIS_EXTENDED['green'],
        label_a='Free',
        label_b='Enslaved',
    )
    fig.savefig(f'{OUTPUT_DIR}/spiral_freed_slaves.png', dpi=200)
    plt.close(fig)
    print("  [OK] Spiral chart — Freed slaves")


# ──────────────────────────────────────────────────────────────
# 8. CONCENTRIC RINGS — Furniture value growth
# ──────────────────────────────────────────────────────────────
def test_rings_furniture():
    dubois.set_theme('classic')
    rows = load_csv('furniture.csv')

    years = [str(r['Year']) for r in rows]
    values = [int(r['Houshold Value (Dollars)']) for r in rows]
    # Normalize to percentage of max for ring display
    max_val = max(values)
    pcts = [v / max_val * 100 for v in values]

    fig, ax = spiral.concentric_rings(
        years, pcts,
        title='Assessed Value of Household\nand Kitchen Furniture',
        subtitle='Owned by Georgia Negroes',
    )
    fig.savefig(f'{OUTPUT_DIR}/rings_furniture.png', dpi=200)
    plt.close(fig)
    print("  [OK] Concentric rings — Furniture value")


# ──────────────────────────────────────────────────────────────
# 9. WRAPPED BAR — Income spending breakdown
# ──────────────────────────────────────────────────────────────
def test_wrapped_bar_income():
    dubois.set_theme('classic')
    rows = load_csv('income.csv')

    categories = [r['Class'] for r in rows]
    rent_vals = []
    for r in rows:
        v = r.get('Rent', '0') or '0'
        rent_vals.append(float(v))

    fig, ax = wrapped.wrapped_bar(
        categories, rent_vals,
        title='Rent as Percentage of Income',
        subtitle='Among 150 Negro Families in Atlanta, GA',
        show_inline_labels=False,
    )
    fig.savefig(f'{OUTPUT_DIR}/wrapped_bar_income.png', dpi=200)
    plt.close(fig)
    print("  [OK] Wrapped bar — Income rent %")


# ──────────────────────────────────────────────────────────────
# 10. SNAKE BAR — Occupation percentages
# ──────────────────────────────────────────────────────────────
def test_snake_bar_occupation():
    dubois.set_theme('classic')
    rows = load_csv('occupation.csv')

    negro_rows = [r for r in rows if r['Group'] == 'Negroes']
    white_rows = [r for r in rows if r['Group'] == 'Whites']
    short_names = []
    for r in negro_rows:
        name = r['Occupation'].split(',')[0] if ',' in r['Occupation'] else r['Occupation']
        short_names.append(name)
    negro_vals = [float(r['Percentage']) for r in negro_rows]
    white_vals = [float(r['Percentage']) for r in white_rows]

    fig, ax = wrapped.snake_bar(
        short_names,
        {'Negroes': negro_vals, 'Whites': white_vals},
        title='Negro vs White Occupations in Georgia',
        subtitle='Percentage Distribution, 1900',
    )
    fig.savefig(f'{OUTPUT_DIR}/snake_bar_occupation.png', dpi=200)
    plt.close(fig)
    print("  [OK] Snake bar — Occupation %")


# ──────────────────────────────────────────────────────────────
# 11. ICON GRID — City/Rural population as pictorial
# ──────────────────────────────────────────────────────────────
def test_icon_grid_city_rural():
    dubois.set_theme('classic')
    rows = load_csv('city_rural.csv')

    total = sum(int(r['Population']) for r in rows)
    # Convert to percentages for icon grid
    data = {}
    for r in rows:
        pct = int(r['Population']) / total * 100
        data[r['Category']] = round(pct)

    fig, ax = pictorial.icon_grid(
        data,
        title='City and Rural Population',
        subtitle='Georgia Negroes, 1890',
        total=100,
    )
    fig.savefig(f'{OUTPUT_DIR}/icon_grid_city_rural.png', dpi=200)
    plt.close(fig)
    print("  [OK] Icon grid — City/Rural")


# ──────────────────────────────────────────────────────────────
# 12. PICTOGRAPH ROW — Occupation as pictograph
# ──────────────────────────────────────────────────────────────
def test_pictograph_occupation():
    dubois.set_theme('classic')
    rows = load_csv('occupation.csv')

    negro_rows = [r for r in rows if r['Group'] == 'Negroes']
    data = {}
    for r in negro_rows:
        name = r['Occupation'].split(',')[0] if ',' in r['Occupation'] else r['Occupation']
        data[name] = float(r['Percentage'])

    fig, ax = pictorial.pictograph_row(
        data,
        title='Occupations of Georgia Negroes',
        subtitle='1900',
    )
    fig.savefig(f'{OUTPUT_DIR}/pictograph_occupation.png', dpi=200)
    plt.close(fig)
    print("  [OK] Pictograph row — Occupation")


# ──────────────────────────────────────────────────────────────
# Run all tests
# ──────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print("Testing dubois-viz with real Du Bois 1900 Paris Exposition data\n")
    print(f"Data directory:   {DATA_DIR}")
    print(f"Output directory: {OUTPUT_DIR}\n")

    tests = [
        test_bar_city_rural,
        test_grouped_bar_occupation,
        test_stacked_bar_income,
        test_area_freed_slaves,
        test_butterfly_georgia_pop,
        test_comparison_conjugal,
        test_spiral_freed_slaves,
        test_rings_furniture,
        test_wrapped_bar_income,
        test_snake_bar_occupation,
        test_icon_grid_city_rural,
        test_pictograph_occupation,
    ]

    passed = 0
    failed = 0
    for test_fn in tests:
        try:
            test_fn()
            passed += 1
        except Exception as e:
            print(f"  [FAIL] {test_fn.__name__}: {e}")
            failed += 1

    print(f"\nResults: {passed} passed, {failed} failed out of {len(tests)}")
    print(f"Charts saved to {OUTPUT_DIR}/")

    dubois.reset_theme()
