"""
Tests for dubois.colors module
"""

import pytest
from dubois import colors


class TestColorPalettes:
    """Test color palette functions"""
    
    def test_get_palette_primary(self):
        """Test getting primary palette"""
        palette = colors.get_palette('primary')
        assert 'crimson' in palette
        assert 'gold' in palette
        assert 'black' in palette
        assert 'tan' in palette
        assert palette['crimson'] == '#DC143C'
    
    def test_get_palette_extended(self):
        """Test getting extended palette"""
        palette = colors.get_palette('extended')
        assert len(palette) > 4
        assert 'green' in palette
        assert 'purple' in palette
    
    def test_get_palette_invalid(self):
        """Test invalid palette name"""
        with pytest.raises(ValueError):
            colors.get_palette('nonexistent')
    
    def test_get_sequential_crimson(self):
        """Test sequential crimson palette"""
        seq = colors.get_sequential('crimson')
        assert len(seq) == 8
        assert all(isinstance(c, str) for c in seq)
        assert all(c.startswith('#') for c in seq)
    
    def test_get_sequential_custom_n(self):
        """Test sequential palette with custom n"""
        seq = colors.get_sequential('crimson', n=5)
        assert len(seq) == 5
    
    def test_get_sequential_invalid(self):
        """Test invalid sequential color"""
        with pytest.raises(ValueError):
            colors.get_sequential('invalid')
    
    def test_get_categorical(self):
        """Test categorical palette"""
        cat = colors.get_categorical(4)
        assert len(cat) == 4
        assert cat[0] == colors.DUBOIS_CLASSIC_4[0]
    
    def test_get_categorical_large(self):
        """Test categorical palette with more than 8 colors"""
        cat = colors.get_categorical(12)
        assert len(cat) == 12
    
    def test_get_diverging(self):
        """Test diverging palette"""
        div = colors.get_diverging(7)
        assert len(div) == 7
    
    def test_get_diverging_even_warning(self):
        """Test warning for even number in diverging palette"""
        import warnings
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            div = colors.get_diverging(6)
            assert len(div) == 7  # Should be incremented to 7
            assert len(w) == 1
            assert 'odd' in str(w[0].message).lower()


class TestColorConversion:
    """Test color conversion functions"""
    
    def test_hex_to_rgb(self):
        """Test hex to RGB conversion"""
        rgb = colors.hex_to_rgb('#DC143C')
        assert len(rgb) == 3
        assert all(0 <= c <= 1 for c in rgb)
        # Test approximate values
        assert abs(rgb[0] - 0.863) < 0.01  # Red
        assert abs(rgb[1] - 0.078) < 0.01  # Green
        assert abs(rgb[2] - 0.235) < 0.01  # Blue
    
    def test_rgb_to_hex(self):
        """Test RGB to hex conversion"""
        hex_color = colors.rgb_to_hex(1.0, 0.0, 0.0)
        assert hex_color.lower() == '#ff0000'
    
    def test_round_trip_conversion(self):
        """Test converting hex -> RGB -> hex"""
        original = '#DC143C'
        rgb = colors.hex_to_rgb(original)
        converted = colors.rgb_to_hex(*rgb)
        assert converted.lower() == original.lower()


class TestQuickAccess:
    """Test quick access color variables"""
    
    def test_quick_access_colors(self):
        """Test module-level color variables"""
        assert colors.crimson == '#DC143C'
        assert colors.gold == '#D4AF37'
        assert colors.black == '#000000'
        assert colors.tan == '#D2B48C'


class TestPaletteConstants:
    """Test palette constant definitions"""
    
    def test_dubois_primary(self):
        """Test primary palette constant"""
        assert len(colors.DUBOIS_PRIMARY) == 4
        assert all(isinstance(v, str) for v in colors.DUBOIS_PRIMARY.values())
    
    def test_dubois_classic_3(self):
        """Test 3-color classic palette"""
        assert len(colors.DUBOIS_CLASSIC_3) == 3
    
    def test_dubois_classic_4(self):
        """Test 4-color classic palette"""
        assert len(colors.DUBOIS_CLASSIC_4) == 4
    
    def test_dubois_categorical_8(self):
        """Test 8-color categorical palette"""
        assert len(colors.DUBOIS_CATEGORICAL_8) == 8
    
    def test_sequential_palettes(self):
        """Test sequential palette constants"""
        assert len(colors.CRIMSON_SEQUENTIAL) == 8
        assert len(colors.GOLD_SEQUENTIAL) == 8
        assert len(colors.GREEN_SEQUENTIAL) == 8


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
