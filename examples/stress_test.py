"""
Stress test — exercise every dubois chart with diverse third-party data shapes.

Goal: surface label overlap, clipping, illegible text, broken layouts that
arise when users plug in their own data (long labels, many categories,
tiny values, lopsided distributions).
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import dubois
from dubois.charts import bar, area, butterfly, spiral, wrapped, pictorial

OUT = os.path.join(os.path.dirname(__file__), 'output', 'stress_test')
os.makedirs(OUT, exist_ok=True)


def save(fig, name):
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, dpi=110, bbox_inches='tight')
    plt.close(fig)
    print(f'  wrote {name}.png')


# ---- BAR ----------------------------------------------------------------
print('BAR')

# 1. Long category labels
fig, _ = bar.bar(
    ['Software Engineers and Architects',
     'Product Managers / Program Managers',
     'Data Scientists & ML Researchers',
     'Customer Support Representatives',
     'Marketing & Communications Specialists'],
    [3450, 1280, 980, 760, 540],
    title='Headcount by Function',
    label_format='{:,.0f}'
)
save(fig, 'bar_long_labels')

# 2. Many categories (15)
months = [f'Month {i+1}' for i in range(15)]
fig, _ = bar.bar(months, [12, 8, 19, 23, 17, 31, 28, 35, 22, 18, 14, 9, 25, 30, 11],
                 title='15 month series')
save(fig, 'bar_15_categories')

# 3. Tiny decimal values
fig, _ = bar.bar(['A', 'B', 'C', 'D'], [0.012, 0.045, 0.008, 0.034],
                 title='Tiny values', label_format='{:.3f}')
save(fig, 'bar_tiny_values')

# 4. Extreme magnitude spread (one bar dwarfs others)
fig, _ = bar.bar(['X', 'Y', 'Z', 'W'], [10000, 50, 30, 10],
                 title='Extreme spread')
save(fig, 'bar_extreme_spread')

# 5. Vertical orientation w/ long labels
fig, _ = bar.bar(
    ['North America', 'South America', 'Europe', 'Asia Pacific',
     'Middle East and Africa', 'Antarctica'],
    [340, 180, 290, 510, 95, 2],
    orientation='vertical', title='Regions vertical')
save(fig, 'bar_vertical_long')

# 6. Single bar (degenerate)
fig, _ = bar.bar(['Only One'], [42], title='Single bar')
save(fig, 'bar_single')

# 7. Negative values
fig, _ = bar.bar(['Q1', 'Q2', 'Q3', 'Q4'], [120, -45, 80, -30],
                 title='Net change with negatives')
save(fig, 'bar_negatives')

# ---- GROUPED BAR --------------------------------------------------------
print('GROUPED BAR')

# Many groups, few categories
fig, _ = bar.grouped_bar(
    ['North', 'South', 'East', 'West'],
    {'2019': [12, 18, 15, 9],
     '2020': [10, 14, 20, 11],
     '2021': [15, 22, 25, 18],
     '2022': [22, 28, 30, 24],
     '2023': [30, 35, 40, 33]},
    title='5 groups across 4 cats')
save(fig, 'grouped_5_groups')

# Long category labels
fig, _ = bar.grouped_bar(
    ['Customer Acquisition Cost',
     'Average Revenue Per User',
     'Monthly Recurring Revenue',
     'Churn Rate (Annual)'],
    {'Plan A': [120, 80, 250, 5],
     'Plan B': [200, 120, 410, 3]},
    title='Long category names')
save(fig, 'grouped_long_labels')

# ---- STACKED BAR --------------------------------------------------------
print('STACKED BAR')

# Many small segments
fig, _ = bar.stacked_bar(
    ['2020', '2021', '2022'],
    {'Chrome': [62, 64, 65],
     'Safari': [18, 19, 20],
     'Firefox': [8, 7, 6],
     'Edge': [6, 7, 8],
     'Opera': [3, 2, 1],
     'Other': [3, 1, 0]},  # zero segment
    title='Browser share', show_total=True, label_format='{:.0f}%')
save(fig, 'stacked_many_segments')

# Tiny segments below the white-vs-black threshold (val>8)
fig, _ = bar.stacked_bar(
    ['Cohort A', 'Cohort B'],
    {'Major': [70, 80],
     'Minor': [25, 15],
     'Trace': [5, 5]},
    title='Mixed sizes')
save(fig, 'stacked_tiny_segments')

# ---- AREA ---------------------------------------------------------------
print('AREA')

# Many groups
years = list(range(1900, 1961, 10))
fig, _ = area.area(
    years,
    {'Agriculture': [60, 50, 40, 35, 30, 25, 20],
     'Manufacturing': [20, 25, 30, 32, 35, 33, 30],
     'Services': [12, 15, 18, 20, 22, 28, 35],
     'Government': [5, 7, 8, 10, 8, 9, 10],
     'Other': [3, 3, 4, 3, 5, 5, 5]},
    title='5 sectors over time')
save(fig, 'area_5_groups')

# Proportional with long group names
fig, _ = area.proportional_area(
    [2018, 2019, 2020, 2021, 2022, 2023],
    {'Direct Sales Channel': [40, 38, 35, 30, 28, 25],
     'Reseller Partner Network': [35, 33, 30, 28, 25, 23],
     'Online Self-Service Platform': [15, 18, 22, 25, 30, 35],
     'Marketplace Integrations': [10, 11, 13, 17, 17, 17]},
    title='Proportional revenue mix')
save(fig, 'area_proportional_long_names')

# Annotations at edges (test edge clipping)
fig, _ = area.area(
    [2010, 2012, 2014, 2016, 2018, 2020, 2022],
    {'Active Users': [10, 25, 40, 55, 70, 85, 100],
     'Inactive': [90, 75, 60, 45, 30, 15, 5]},
    title='Annotations at edges',
    annotations={2010: 'Launch', 2016: 'IPO', 2022: 'Acquisition'})
save(fig, 'area_annotations_edges')

# Tiny middle group (label visibility)
fig, _ = area.area(
    [1, 2, 3, 4, 5],
    {'Big': [80, 82, 78, 81, 79],
     'Small': [2, 3, 2, 4, 3],
     'Medium': [18, 15, 20, 15, 18]},
    title='Tiny group label')
save(fig, 'area_tiny_group')

# ---- BUTTERFLY ----------------------------------------------------------
print('BUTTERFLY')

# Asymmetric scale (one side much larger)
fig, _ = butterfly.butterfly(
    ['18-24', '25-34', '35-44', '45-54', '55-64', '65+'],
    [10, 25, 40, 35, 20, 8],
    [200, 320, 410, 380, 290, 150],
    left_label='Pilot Program', right_label='Full Rollout',
    title='Asymmetric magnitudes', symmetric=False)
save(fig, 'butterfly_asymmetric')

# Long category labels
fig, _ = butterfly.butterfly(
    ['Bachelor\u2019s degree or higher',
     'Some college, no degree',
     'High school graduate only',
     'Less than high school'],
    [45, 30, 18, 7],
    [38, 28, 22, 12],
    left_label='2010 Census', right_label='2020 Census',
    title='Education by census')
save(fig, 'butterfly_long_labels')

# Many categories
states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
          'HI', 'ID', 'IL', 'IN', 'IA']
fig, _ = butterfly.butterfly(
    states,
    [22, 15, 28, 19, 45, 32, 25, 18, 38, 35, 12, 14, 41, 24, 19],
    [25, 18, 30, 21, 50, 35, 28, 20, 40, 38, 15, 16, 44, 27, 21],
    left_label='2019', right_label='2024',
    title='15 states')
save(fig, 'butterfly_many_cats')

# Comparison (dot chart)
fig, _ = butterfly.comparison(
    ['Engineering', 'Sales', 'Marketing', 'Operations', 'Finance'],
    [85000, 72000, 65000, 58000, 92000],
    [110000, 95000, 80000, 70000, 125000],
    label_a='Junior', label_b='Senior',
    title='Salary comparison')
save(fig, 'butterfly_comparison')

# ---- SPIRAL -------------------------------------------------------------
print('SPIRAL')

# Many rings (12)
fig, _ = spiral.spiral(
    [f'Region {i+1}' for i in range(12)],
    [22, 35, 48, 18, 65, 40, 28, 55, 38, 72, 45, 30],
    title='12 rings')
save(fig, 'spiral_12_rings')

# Long category names
fig, _ = spiral.spiral(
    ['San Francisco Bay Area',
     'Greater New York Metro',
     'Chicago Metropolitan Area',
     'Los Angeles & Orange County',
     'Boston-Cambridge-Newton'],
    [62, 78, 45, 55, 70],
    label_a='Urban', label_b='Suburban',
    title='Long region names')
save(fig, 'spiral_long_names')

# Extreme proportions (very small group A on some rings)
fig, _ = spiral.spiral(
    ['A', 'B', 'C', 'D', 'E'],
    [2, 5, 50, 95, 98],  # both extremes
    title='Extreme proportions')
save(fig, 'spiral_extremes')

# Concentric rings
fig, _ = spiral.concentric_rings(
    ['Quarterly Revenue', 'Customer Retention', 'Product Quality',
     'Employee Satisfaction', 'Market Share'],
    [78, 92, 65, 88, 45],
    title='KPI dashboard')
save(fig, 'spiral_concentric')

# ---- WRAPPED ------------------------------------------------------------
print('WRAPPED')

# Many small categories
fig, _ = wrapped.wrapped_bar(
    [f'Cat{i+1}' for i in range(10)],
    [15, 18, 12, 10, 14, 8, 11, 9, 7, 6],
    title='10 categories')
save(fig, 'wrapped_10_cats')

# Few large vs many tiny
fig, _ = wrapped.wrapped_bar(
    ['Dominant', 'Secondary', 'Tiny1', 'Tiny2', 'Tiny3', 'Tiny4'],
    [60, 30, 3, 3, 2, 2],
    title='Lopsided distribution')
save(fig, 'wrapped_lopsided')

# Long category names
fig, _ = wrapped.wrapped_bar(
    ['Manufacturing & Logistics',
     'Retail & Consumer Goods',
     'Financial Services Industry',
     'Healthcare & Life Sciences'],
    [28, 22, 30, 20],
    title='Long industry names')
save(fig, 'wrapped_long_names')

# Snake bar
fig, _ = wrapped.snake_bar(
    ['North Carolina', 'South Carolina', 'Georgia', 'Mississippi',
     'Alabama', 'Tennessee'],
    {'Urban': [20, 15, 28, 8, 22, 30],
     'Suburban': [25, 22, 30, 18, 28, 35],
     'Rural': [55, 63, 42, 74, 50, 35]},
    title='State urbanization')
save(fig, 'wrapped_snake')

# ---- PICTORIAL ----------------------------------------------------------
print('PICTORIAL')

# Many groups in icon grid
fig, _ = pictorial.icon_grid(
    {'Apple': 28, 'Samsung': 22, 'Xiaomi': 13, 'OPPO': 9,
     'Vivo': 8, 'Huawei': 6, 'Realme': 4, 'Other': 10},
    title='Smartphone share')
save(fig, 'pictorial_grid_8groups')

# Tiny percentages
fig, _ = pictorial.icon_grid(
    {'Common': 97, 'Rare': 2, 'Ultra-rare': 1},
    title='Rounding and tiny groups')
save(fig, 'pictorial_grid_tiny')

# Pictograph row — many narrow segments (callout test)
fig, _ = pictorial.pictograph_row(
    {'Excellent': 8, 'Very Good': 12, 'Good': 22, 'Average': 30,
     'Below Average': 18, 'Poor': 7, 'Very Poor': 3},
    title='Likert scale 7-pt')
save(fig, 'pictorial_row_7segs')

# Pictograph row — long segment names
fig, _ = pictorial.pictograph_row(
    {'Strongly Disagree with Statement': 5,
     'Somewhat Disagree': 15,
     'Neither Agree Nor Disagree': 20,
     'Somewhat Agree': 35,
     'Strongly Agree with Statement': 25},
    title='Long segment names')
save(fig, 'pictorial_row_long_names')

# Pictograph row — single dominant segment
fig, _ = pictorial.pictograph_row(
    {'Yes': 92, 'No': 5, 'Unsure': 3},
    title='Dominant segment')
save(fig, 'pictorial_row_dominant')

print('\nAll done. Outputs in:', OUT)
