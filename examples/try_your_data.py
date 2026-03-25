"""
Try dubois-viz with your own data!

This script shows how to plug in your own data to every chart type.
Edit the data below and run: python examples/try_your_data.py

Each chart saves a PNG to examples/output/ so you can inspect the results.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import dubois
from dubois.charts import bar, area, butterfly, spiral, wrapped, pictorial

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ─── CHANGE THIS DATA TO YOUR OWN ────────────────────────────────────────────

# Bar chart data
BAR_CATEGORIES = ['Engineering', 'Design', 'Marketing', 'Sales', 'Operations']
BAR_VALUES = [35, 20, 18, 15, 12]

# Grouped bar data (compare two groups across categories)
GROUPED_CATEGORIES = ['Q1', 'Q2', 'Q3', 'Q4']
GROUPED_DATA = {
    '2024': [120, 150, 180, 200],
    '2025': [140, 160, 210, 240],
}

# Stacked bar data (parts of a whole per category)
STACKED_CATEGORIES = ['North', 'South', 'East', 'West']
STACKED_DATA = {
    'Online': [45, 38, 52, 41],
    'In-Store': [55, 62, 48, 59],
}

# Area chart data (trends over time)
AREA_YEARS = [2018, 2019, 2020, 2021, 2022, 2023, 2024]
AREA_DATA = {
    'Renewable': [15, 18, 22, 28, 35, 42, 50],
    'Fossil': [85, 82, 78, 72, 65, 58, 50],
}

# Butterfly chart data (compare two groups side-by-side)
BUTTERFLY_CATEGORIES = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
BUTTERFLY_LEFT = [12, 22, 20, 18, 15, 13]   # e.g. Male
BUTTERFLY_RIGHT = [14, 24, 19, 17, 14, 12]  # e.g. Female

# Spiral chart data (proportional data across categories)
SPIRAL_CATEGORIES = [
    'California', 'Texas', 'Florida', 'New York',
    'Pennsylvania', 'Illinois', 'Ohio', 'Georgia',
]
SPIRAL_VALUES = [28, 22, 19, 35, 24, 31, 18, 25]  # e.g. urban %

# Concentric rings data (progress/completion per category)
RINGS_CATEGORIES = ['Literacy', 'Home Ownership', 'College Degree', 'Business Ownership']
RINGS_VALUES = [88, 65, 33, 12]

# Wrapped bar data (proportional composition)
WRAPPED_CATEGORIES = ['Housing', 'Food', 'Transport', 'Healthcare', 'Education', 'Other']
WRAPPED_VALUES = [33, 22, 15, 12, 10, 8]

# Snake bar data (stacked rows)
SNAKE_CATEGORIES = ['USA', 'UK', 'Germany', 'Japan', 'Brazil']
SNAKE_DATA = {
    'Urban': [83, 84, 77, 92, 87],
    'Rural': [17, 16, 23, 8, 13],
}

# Icon grid data (waffle chart)
GRID_DATA = {'Employed': 62, 'Unemployed': 5, 'Not in Labor Force': 33}

# Pictograph row data (single proportional strip)
STRIP_DATA = {'Agree': 58, 'Neutral': 24, 'Disagree': 18}


# ─── GENERATE ALL CHARTS ─────────────────────────────────────────────────────

def main():
    dubois.set_theme('classic')
    print("Generating charts with your data...\n")

    # 1. Bar chart
    fig, ax = bar.bar(
        BAR_CATEGORIES, BAR_VALUES,
        title='Team Headcount by Department',
        label_format='{:.0f}',
    )
    fig.savefig(f'{OUTPUT_DIR}/test_bar.png', dpi=200, bbox_inches='tight')
    plt.close(fig)
    print("  [OK] Bar chart -> test_bar.png")

    # 2. Grouped bar
    fig, ax = bar.grouped_bar(
        GROUPED_CATEGORIES, GROUPED_DATA,
        title='Revenue by Quarter',
    )
    fig.savefig(f'{OUTPUT_DIR}/test_grouped_bar.png', dpi=200, bbox_inches='tight')
    plt.close(fig)
    print("  [OK] Grouped bar -> test_grouped_bar.png")

    # 3. Stacked bar
    fig, ax = bar.stacked_bar(
        STACKED_CATEGORIES, STACKED_DATA,
        title='Sales Channel by Region',
    )
    fig.savefig(f'{OUTPUT_DIR}/test_stacked_bar.png', dpi=200, bbox_inches='tight')
    plt.close(fig)
    print("  [OK] Stacked bar -> test_stacked_bar.png")

    # 4. Area chart
    fig, ax = area.proportional_area(
        AREA_YEARS, AREA_DATA,
        title='Energy Mix Over Time',
        subtitle='Percentage of total generation',
    )
    fig.savefig(f'{OUTPUT_DIR}/test_area.png', dpi=200, bbox_inches='tight')
    plt.close(fig)
    print("  [OK] Area chart -> test_area.png")

    # 5. Butterfly chart
    fig, ax = butterfly.butterfly(
        BUTTERFLY_CATEGORIES,
        BUTTERFLY_LEFT, BUTTERFLY_RIGHT,
        left_label='Male', right_label='Female',
        title='Population by Age Group',
        label_format='{:.0f}%',
    )
    fig.savefig(f'{OUTPUT_DIR}/test_butterfly.png', dpi=200, bbox_inches='tight')
    plt.close(fig)
    print("  [OK] Butterfly chart -> test_butterfly.png")

    # 6. Spiral chart
    fig, ax = spiral.spiral(
        SPIRAL_CATEGORIES, SPIRAL_VALUES,
        label_a='Urban', label_b='Rural',
        title='Urban Population by State',
    )
    fig.savefig(f'{OUTPUT_DIR}/test_spiral.png', dpi=200, bbox_inches='tight')
    plt.close(fig)
    print("  [OK] Spiral chart -> test_spiral.png")

    # 7. Concentric rings
    fig, ax = spiral.concentric_rings(
        RINGS_CATEGORIES, RINGS_VALUES,
        title='Progress Indicators',
    )
    fig.savefig(f'{OUTPUT_DIR}/test_rings.png', dpi=200, bbox_inches='tight')
    plt.close(fig)
    print("  [OK] Concentric rings -> test_rings.png")

    # 8. Wrapped bar
    fig, ax = wrapped.wrapped_bar(
        WRAPPED_CATEGORIES, WRAPPED_VALUES,
        title='Household Spending Breakdown',
    )
    fig.savefig(f'{OUTPUT_DIR}/test_wrapped.png', dpi=200, bbox_inches='tight')
    plt.close(fig)
    print("  [OK] Wrapped bar -> test_wrapped.png")

    # 9. Snake bar
    fig, ax = wrapped.snake_bar(
        SNAKE_CATEGORIES, SNAKE_DATA,
        title='Urban vs Rural Population',
    )
    fig.savefig(f'{OUTPUT_DIR}/test_snake.png', dpi=200, bbox_inches='tight')
    plt.close(fig)
    print("  [OK] Snake bar -> test_snake.png")

    # 10. Icon grid
    fig, ax = pictorial.icon_grid(
        GRID_DATA,
        title='Labor Force Participation',
    )
    fig.savefig(f'{OUTPUT_DIR}/test_icon_grid.png', dpi=200, bbox_inches='tight')
    plt.close(fig)
    print("  [OK] Icon grid -> test_icon_grid.png")

    # 11. Pictograph row
    fig, ax = pictorial.pictograph_row(
        STRIP_DATA,
        title='Survey Results',
    )
    fig.savefig(f'{OUTPUT_DIR}/test_pictograph.png', dpi=200, bbox_inches='tight')
    plt.close(fig)
    print("  [OK] Pictograph row -> test_pictograph.png")

    dubois.reset_theme()
    print(f"\nAll charts saved to {OUTPUT_DIR}/")
    print("Edit the data at the top of this file and re-run to test with your own data!")


if __name__ == '__main__':
    main()
