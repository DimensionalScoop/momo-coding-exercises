import read
import numpy.testing as npt 

def test_line_to_number():
    line = " 1 2, 3   47   100"
    expected = [1,2,3,47,100]
    actual = read.line_to_numbers(line)

    npt.assert_allclose(actual,expected)


