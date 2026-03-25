"""
Test dubois-viz with randomly generated data.

Proves the package works with any dataset, not just Du Bois-specific data.
Uses a mix of realistic random data: tech industry stats, world energy,
and fictional survey results.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random
import matplotlib.pyplot as plt
import dubois
from dubois.charts import bar, area, butterfly, spiral, wrapped, pictorial

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output', 'random_data')
os.makedirs(OUTPUT_DIR, exist_ok=True)

random.seed(42)


# ── 1. BAR — Programming language popularity ────────────────
def test_bar():
    dubois.set_theme('classic')
    langs = ['Python', 'JavaScript', 'Java', 'C++', 'Go', 'Rust', 'TypeScript']
    popularity = [random.randint(5, 70) for _ in langs]
    popularity.sort(reverse=True)

    fig, ax = bar.bar(
        langs, popularity,
        title='Programming Language Popularity',
        subtitle='Developer Survey 2025 (random data)',
        label_format='{:.0f}%',
    )
    fig.savefig(f'{OUTPUT_DIR}/bar_languages.png', dpi=200)
    plt.close(fig)
    print("  [OK] Bar chart")


# ── 2. GROUPED BAR — Revenue by quarter ─────────────────────
def test_grouped_bar():
    dubois.set_theme('classic')
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    fig, ax = bar.grouped_bar(
        quarters,
        {
            'Product A': [random.randint(100, 500) for _ in quarters],
            'Product B': [random.randint(80, 400) for _ in quarters],
            'Product C': [random.randint(50, 300) for _ in quarters],
        },
        title='Quarterly Revenue by Product',
        subtitle='FY2025 (random data)',
        label_format='${:.0f}K',
    )
    fig.savefig(f'{OUTPUT_DIR}/grouped_bar_revenue.png', dpi=200)
    plt.close(fig)
    print("  [OK] Grouped bar chart")


# ── 3. STACKED BAR — Energy sources by country ──────────────
def test_stacked_bar():
    dubois.set_theme('classic')
    countries = ['USA', 'China', 'Germany', 'Brazil', 'India']
    sources = ['Fossil Fuels', 'Nuclear', 'Solar/Wind', 'Hydro']

    groups = {}
    for src in sources:
        groups[src] = [random.randint(5, 50) for _ in countries]

    fig, ax = bar.stacked_bar(
        countries, groups,
        title='Energy Mix by Country',
        subtitle='Percentage of Total Generation (random data)',
        label_format='{:.0f}%',
    )
    fig.savefig(f'{OUTPUT_DIR}/stacked_bar_energy.png', dpi=200)
    plt.close(fig)
    print("  [OK] Stacked bar chart")


# ── 4. AREA — Website traffic over 12 months ────────────────
def test_area():
    dubois.set_theme('classic')
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Simulate growing traffic with seasonal dips
    base = 1000
    organic = []
    paid = []
    for i in range(12):
        organic.append(base + i * 200 + random.randint(-100, 100))
        paid.append(500 + i * 80 + random.randint(-50, 50))

    fig, ax = area.area(
        months,
        {'Organic': organic, 'Paid': paid},
        title='Website Traffic Sources',
        subtitle='Monthly Visitors, 2025 (random data)',
        stacked=True,
    )
    fig.savefig(f'{OUTPUT_DIR}/area_traffic.png', dpi=200)
    plt.close(fig)
    print("  [OK] Area chart")


# ── 5. BUTTERFLY — Men vs Women survey responses ────────────
def test_butterfly():
    dubois.set_theme('classic')
    topics = ['Career', 'Family', 'Health', 'Education',
              'Finance', 'Leisure', 'Community']
    men = [random.randint(10, 90) for _ in topics]
    women = [random.randint(10, 90) for _ in topics]

    fig, ax = butterfly.butterfly(
        topics, men, women,
        left_label='Men', right_label='Women',
        title='Life Priorities Survey',
        label_format='{:.0f}%',
    )
    fig.savefig(f'{OUTPUT_DIR}/butterfly_survey.png', dpi=200)
    plt.close(fig)
    print("  [OK] Butterfly chart")


# ── 6. COMPARISON — Urban vs Rural internet access ──────────
def test_comparison():
    dubois.set_theme('classic')
    age_groups = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
    urban = [random.randint(70, 99) for _ in age_groups]
    rural = [random.randint(30, 85) for _ in age_groups]

    fig, ax = butterfly.comparison(
        age_groups, urban, rural,
        left_label='Urban', right_label='Rural',
        title='Internet Access by Age',
        subtitle='Urban vs Rural (random data)',
        label_format='{:.0f}%',
    )
    fig.savefig(f'{OUTPUT_DIR}/comparison_internet.png', dpi=200)
    plt.close(fig)
    print("  [OK] Comparison chart")


# ── 7. SPIRAL — Market share ────────────────────────────────
def test_spiral():
    dubois.set_theme('classic')
    companies = ['AlphaCorp', 'BetaTech', 'Gamma Inc', 'Delta Ltd',
                 'Epsilon Co', 'Zeta Group']
    shares = [random.randint(5, 35) for _ in companies]

    fig, ax = spiral.spiral(
        companies, shares,
        title='Market Share Distribution',
        label_a='Share',
        label_b='Remaining',
    )
    fig.savefig(f'{OUTPUT_DIR}/spiral_market.png', dpi=200)
    plt.close(fig)
    print("  [OK] Spiral chart")


# ── 8. CONCENTRIC RINGS — Completion rates ──────────────────
def test_rings():
    dubois.set_theme('classic')
    courses = ['Math 101', 'Physics', 'Chemistry', 'Biology',
               'History', 'English']
    completion = [random.randint(40, 98) for _ in courses]

    fig, ax = spiral.concentric_rings(
        courses, completion,
        title='Course Completion Rates',
        subtitle='University Department Overview (random data)',
    )
    fig.savefig(f'{OUTPUT_DIR}/rings_courses.png', dpi=200)
    plt.close(fig)
    print("  [OK] Concentric rings")


# ── 9. WRAPPED BAR — Budget allocation ──────────────────────
def test_wrapped_bar():
    dubois.set_theme('classic')
    depts = ['Engineering', 'Marketing', 'Sales', 'Operations',
             'HR', 'Legal', 'R&D']
    budgets = [random.randint(5, 35) for _ in depts]

    fig, ax = wrapped.wrapped_bar(
        depts, budgets,
        title='Annual Budget Allocation',
        subtitle='By Department (random data)',
        show_inline_labels=False,
    )
    fig.savefig(f'{OUTPUT_DIR}/wrapped_budget.png', dpi=200)
    plt.close(fig)
    print("  [OK] Wrapped bar")


# ── 10. SNAKE BAR — Skills by team ──────────────────────────
def test_snake_bar():
    dubois.set_theme('classic')
    teams = ['Frontend', 'Backend', 'DevOps', 'Data', 'Mobile']

    fig, ax = wrapped.snake_bar(
        teams,
        {
            'Junior': [random.randint(10, 40) for _ in teams],
            'Mid': [random.randint(20, 50) for _ in teams],
            'Senior': [random.randint(10, 30) for _ in teams],
        },
        title='Team Seniority Distribution',
        subtitle='Engineering Department (random data)',
    )
    fig.savefig(f'{OUTPUT_DIR}/snake_teams.png', dpi=200)
    plt.close(fig)
    print("  [OK] Snake bar")


# ── 11. ICON GRID — Market segments ─────────────────────────
def test_icon_grid():
    dubois.set_theme('classic')
    fig, ax = pictorial.icon_grid(
        {
            'Enterprise': 35,
            'Mid-Market': 28,
            'SMB': 22,
            'Consumer': 15,
        },
        title='Customer Segments',
        subtitle='By Revenue Contribution (random data)',
        total=100,
    )
    fig.savefig(f'{OUTPUT_DIR}/icon_grid_segments.png', dpi=200)
    plt.close(fig)
    print("  [OK] Icon grid")


# ── 12. PICTOGRAPH ROW — Browser market share ───────────────
def test_pictograph():
    dubois.set_theme('classic')
    fig, ax = pictorial.pictograph_row(
        {
            'Chrome': 62,
            'Safari': 20,
            'Firefox': 8,
            'Edge': 5,
            'Other': 5,
        },
        title='Browser Market Share',
        subtitle='Global Desktop Users (random data)',
    )
    fig.savefig(f'{OUTPUT_DIR}/pictograph_browsers.png', dpi=200)
    plt.close(fig)
    print("  [OK] Pictograph row")


# ── Run all ──────────────────────────────────────────────────
if __name__ == '__main__':
    print("Testing dubois-viz with random non-historical data\n")
    print(f"Output: {OUTPUT_DIR}\n")

    tests = [
        test_bar, test_grouped_bar, test_stacked_bar, test_area,
        test_butterfly, test_comparison, test_spiral, test_rings,
        test_wrapped_bar, test_snake_bar, test_icon_grid, test_pictograph,
    ]

    passed = 0
    failed = 0
    for fn in tests:
        try:
            fn()
            passed += 1
        except Exception as e:
            print(f"  [FAIL] {fn.__name__}: {e}")
            import traceback
            traceback.print_exc()
            failed += 1

    print(f"\nResults: {passed} passed, {failed} failed out of {len(tests)}")
    print(f"Charts saved to {OUTPUT_DIR}/")
    dubois.reset_theme()
