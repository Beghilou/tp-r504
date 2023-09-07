import pytest
import fonction as f

def test_1():
	assert f.Puissance_2(2,3) == 8
	assert f.Puissance_2(2,2) == 4

def test_2():
	assert f.Puissance_2(-2,3) <0

def test_3():
	assert f.Puissance_2(0,0) = 1
