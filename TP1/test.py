import pytest
import fonction as f

def test_1():
    assert f.puissance(2, 3) == 8
    assert f.puissance(2, 2) == 4

def test_2():
    # Test avec des valeurs négatives et des exposants négatifs
    assert f.puissance(-2, 2) == 4
    assert f.puissance(-2, -3) == -0.125
    
    # Test avec des valeurs négatives et des exposants positifs
    assert f.puissance(-3, 3) == -27
    assert f.puissance(-4, 5) == -1024
    
    # Cas limite : Exposant nul
    assert f.puissance(10, 0) == 1
    
    # Cas limite : Base nulle, exposant positif
    assert f.puissance(0, 5) == 0
    
    # Cas limite : Base nulle, exposant nul
    assert f.puissance(0, 0) == 1
    
    # Cas limite : Base négative, exposant pair
    assert f.puissance(-2, 4) == 16
    
    # Cas limite : Base négative, exposant impair
    assert f.puissance(-2, 3) == -8

def test_3():
    # Cas limite : Base nulle, exposant négatif (avec une exception)
    with pytest.raises(ValueError):
        f.puissance(0, -5)
