"""
Example: Using dubois-viz to create Du Bois-inspired visualizations

This script demonstrates the basic features of the dubois-viz package.
"""

import sys
import os

# Add parent directory to path for local development
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import dubois
import matplotlib.pyplot as plt
import numpy as np

def example_1_simple_bars():
    """Example 1: Simple bar chart with Du Bois styling"""
    print("Example 1: Simple Bar Chart")
    
    # Apply Du Bois theme
    dubois.set_theme('classic', context='notebook')
    
    # Data
    categories = ['Agriculture', 'Domestic Service', 'Manufacturing', 
                  'Trade', 'Professions', 'Other']
    values = [45, 25, 12, 10, 5, 3]
    
    # Get Du Bois colors
    colors_list = dubois.get_categorical(len(categories))
    
    # Create plot
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(categories, values, color=colors_list, 
                   edgecolor='black', linewidth=1.5)
    
    # Styling
    ax.set_xlabel('Percentage of Negro Workers', fontsize=12, fontweight='bold')
    ax.set_title('OCCUPATIONS OF GEORGIA NEGROES\n1900', 
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xlim(0, 50)
    
    # Add value labels
    for i, (bar, val) in enumerate(zip(bars, values)):
        ax.text(val + 1, i, f'{val}%', va='center', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('examples/example_1_bars.png', dpi=150, facecolor='#F5F5DC')
    print("  Saved to examples/example_1_bars.png")
    plt.close()


def example_2_color_palettes():
    """Example 2: Visualizing different color palettes"""
    print("\nExample 2: Color Palettes")
    
    from dubois.colors import show_palette
    
    # Create examples directory if it doesn't exist
    os.makedirs('examples/palettes', exist_ok=True)
    
    # Show different palettes
    palettes = ['primary', 'extended', 'categorical', 'crimson', 
                'gold', 'green', 'diverging']
    
    for palette in palettes:
        try:
            show_palette(palette, save_path=f'examples/palettes/{palette}.png')
            print(f"  Saved {palette} palette")
        except Exception as e:
            print(f"  Error with {palette}: {e}")


def example_3_sequential_data():
    """Example 3: Line chart with sequential colors"""
    print("\nExample 3: Line Chart with Sequential Colors")
    
    dubois.set_theme('modern', context='notebook')
    
    # Data: hypothetical literacy rates over time
    years = np.arange(1870, 1910, 5)
    literacy = [20, 30, 43, 55, 65, 72, 78, 82]
    
    # Create plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(years, literacy, color=dubois.colors.crimson, 
            linewidth=3, marker='o', markersize=8)
    
    # Fill area under curve
    ax.fill_between(years, 0, literacy, 
                    color=dubois.colors.crimson, alpha=0.2)
    
    # Styling
    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_ylabel('Literacy Rate (%)', fontsize=12, fontweight='bold')
    ax.set_title('DECREASE OF ILLITERACY\nAmong Black Americans, 1870-1905', 
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_ylim(0, 100)
    ax.grid(True, axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('examples/example_3_line.png', dpi=150)
    print("  Saved to examples/example_3_line.png")
    plt.close()


def example_4_stacked_area():
    """Example 4: Stacked area chart"""
    print("\nExample 4: Stacked Area Chart")
    
    dubois.set_theme('classic', context='notebook')
    
    # Data: Free vs Enslaved population over time
    years = np.array([1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870])
    total_pop = np.array([757, 1002, 1378, 1772, 2329, 2874, 3639, 4442, 4880])
    free_pct = np.array([7.9, 11.0, 13.5, 13.2, 13.7, 13.4, 11.9, 11.0, 100.0])
    
    free = total_pop * free_pct / 100
    enslaved = total_pop - free
    
    # Create plot
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # Use Du Bois diverging colors
    colors_div = dubois.get_diverging(2)
    
    ax.fill_between(years, 0, enslaved / 1000, 
                    color='#DC143C', label='SLAVES', alpha=0.9)
    ax.fill_between(years, enslaved / 1000, total_pop / 1000, 
                    color='#00A550', label='FREE', alpha=0.9)
    
    # Styling
    ax.set_xlabel('YEAR', fontsize=12, fontweight='bold')
    ax.set_ylabel('POPULATION (thousands)', fontsize=12, fontweight='bold')
    ax.set_title('PROPORTION OF FREEMEN AND SLAVES\nAmong American Negroes', 
                 fontsize=14, fontweight='bold', pad=20)
    
    # Legend
    ax.legend(loc='upper left', fontsize=11, frameon=True)
    
    # Add annotation for emancipation
    ax.axvline(x=1865, color='black', linestyle='--', linewidth=1.5, alpha=0.5)
    ax.text(1865, ax.get_ylim()[1] * 0.9, 'EMANCIPATION\n1865', 
            ha='center', fontsize=9, style='italic')
    
    plt.tight_layout()
    plt.savefig('examples/example_4_stacked.png', dpi=150, facecolor='#F5F5DC')
    print("  Saved to examples/example_4_stacked.png")
    plt.close()


def example_5_multiple_series():
    """Example 5: Multiple data series"""
    print("\nExample 5: Multiple Data Series")
    
    dubois.set_theme('modern', context='notebook')
    
    # Data: Education levels over time
    years = np.arange(1875, 1905, 5)
    elementary = [10, 20, 35, 48, 58, 65]
    secondary = [0.5, 1, 3, 7, 12, 18]
    higher = [0.1, 0.2, 0.5, 1.2, 2.5, 4]
    
    # Get categorical colors
    colors_cat = dubois.get_categorical(3)
    
    # Create plot
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.plot(years, elementary, color=colors_cat[0], 
            linewidth=3, marker='s', markersize=8, label='Elementary')
    ax.plot(years, secondary, color=colors_cat[1], 
            linewidth=3, marker='o', markersize=8, label='Secondary')
    ax.plot(years, higher, color=colors_cat[2], 
            linewidth=3, marker='^', markersize=8, label='Higher Education')
    
    # Styling
    ax.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax.set_ylabel('Enrollment Rate (%)', fontsize=12, fontweight='bold')
    ax.set_title('NEGRO CHILDREN IN PUBLIC SCHOOLS\nBy Education Level', 
                 fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('examples/example_5_multiple.png', dpi=150)
    print("  Saved to examples/example_5_multiple.png")
    plt.close()


def example_6_context_manager():
    """Example 6: Using context manager for temporary styling"""
    print("\nExample 6: Context Manager")
    
    # First plot without Du Bois style
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Left: default matplotlib
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    ax1.plot(x, y)
    ax1.set_title('Default Matplotlib Style')
    ax1.grid(True)
    
    # Right: with Du Bois style
    with dubois.themes.DuBoisStyle('modern', 'notebook'):
        ax2.plot(x, y, color=dubois.colors.crimson, linewidth=3)
        ax2.set_title('Du Bois Style')
        ax2.grid(True)
    
    plt.tight_layout()
    plt.savefig('examples/example_6_context.png', dpi=150)
    print("  Saved to examples/example_6_context.png")
    plt.close()


def main():
    """Run all examples"""
    print("=" * 60)
    print("Du Bois Visualization Examples")
    print("=" * 60)
    
    # Create examples directory
    os.makedirs('examples', exist_ok=True)
    
    # Run examples
    try:
        example_1_simple_bars()
        example_2_color_palettes()
        example_3_sequential_data()
        example_4_stacked_area()
        example_5_multiple_series()
        example_6_context_manager()
        
        print("\n" + "=" * 60)
        print("All examples completed successfully!")
        print("Check the 'examples/' directory for outputs.")
        print("=" * 60)
        
    except Exception as e:
        print(f"\nError running examples: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        # Reset theme
        dubois.reset_theme()


if __name__ == '__main__':
    main()
