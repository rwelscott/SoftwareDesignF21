import pytest

@pytest.mark.parametrize("intpoints, expected", [ 
    ([(2,1), (3,2)],1), ([(15,10),(3,4)],0.5)])
def test_slope_calc(intpoints, expected):
    from line_function import slope_calc
    answer = slope_calc(intpoints)
    assert answer == expected

@pytest.mark.parametrize("intpoints, slope, x_parameter, expected", [ 
    ([(2,1), (3,2)],1,1,0), ([(15,10),(3,4)],0.5,0,2.5)])
def test_y_para_calc(intpoints, slope, x_parameter, expected):
    from line_function import y_para_calc
    answer = y_para_calc(intpoints, slope, x_parameter)
    assert answer == expected
