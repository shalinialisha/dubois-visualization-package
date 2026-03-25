"""
Du Bois Chart Types

Specialized chart types inspired by W.E.B. Du Bois' original data
visualizations from the 1900 Paris Exposition.

Available chart modules:
- bar: Enhanced horizontal/vertical bar charts, grouped and stacked
- area: Stacked area and proportional area charts
- butterfly: Back-to-back mirror comparison charts
- spiral: Spiral charts and concentric ring charts (Plate 11 style)
- wrapped: Wrapped/snake bar charts along circular paths
- pictorial: Icon grid and pictograph charts
"""

from dubois.charts import bar
from dubois.charts import area
from dubois.charts import butterfly
from dubois.charts import spiral
from dubois.charts import wrapped
from dubois.charts import pictorial

__all__ = ['bar', 'area', 'butterfly', 'spiral', 'wrapped', 'pictorial']
