import pytest
from sumaMinima import caminoSumaMin

def test_sumaMinima4x4():
    cuad = [[1,1,2,2],[1,1,3,6],[5,10,1,1],[7,7,4,1]]
    result = caminoSumaMin(cuad)
    assert result == 9

def test_sumaMinima3x3():
    cuad = [[1, 4, 5],[2, 7, 6],[6, 8, 7]]
    result = caminoSumaMin(cuad)
    assert result == 23

def test_sumaMinima1x1():
    cuad = [[1]]
    result = caminoSumaMin(cuad)
    assert result == 1

def test_sumaMinimaError1():
    cuad = [[1,1,2,2],[1,1,3,6],[5,10,1,1],[7,7,4,1]]
    result = caminoSumaMin(cuad)
    assert result != 8

def test_sumaMinimaError2():
    cuad = [[1,1],[1,1]]
    result = caminoSumaMin(cuad)
    assert result != 4

def test_sumaMinimaError2():
    cuad = []
    result = caminoSumaMin(cuad)
    assert result == 0