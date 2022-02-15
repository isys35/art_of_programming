from E import euclidean_algorithm
from F import euclidean_algorithm as euclidean_algorithm_2
import pytest


@pytest.mark.parametrize("test_input_m, test_input_n, expected",
                         [(544, 119, 17), (119, 544, 17), (36, 18, 18), (165, 14, 1), (27, 15, 3)])
def test_euclidean_algorithm(test_input_m, test_input_n, expected):
    assert euclidean_algorithm(test_input_m, test_input_n) == expected


@pytest.mark.parametrize("test_input_m, test_input_n, expected",
                         [(544, 119, 17), (119, 544, 17), (36, 18, 18), (165, 14, 1), (27, 15, 3)])
def test_euclidean_algorithm_2(test_input_m, test_input_n, expected):
    assert euclidean_algorithm_2(test_input_m, test_input_n) == expected