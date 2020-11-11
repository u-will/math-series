from math_series.series import fibonacci, lucas, sum_series


def test_import():
    assert fibonacci


def test_fibonacci_0():
    actual = fibonacci(0)
    excepted = 0
    assert actual == excepted


def test_fibonacci_1():
  actual = fibonacci(1)
  excepted = 1
  assert actual == excepted


def test_fibonacci_2():
  actual = fibonacci(2)
  excepted = 1
  assert actual == excepted

def test_fibonacci_3():
  actual = fibonacci(3)
  excepted = 2
  assert actual == excepted

def test_lucas_0():
  actual = lucas(0)
  excepted = 2
  assert actual == excepted

def test_lucas_1():
  actual = lucas(1)
  excepted = 1
  assert actual == excepted

def test_lucas_2():
  actual = lucas(2)
  excepted = 3
  assert actual == excepted

def test_sum_series_2():
  actual = sum_series(2)
  excepted = 1
  assert actual == excepted

def test_sum_series_13():
  actual = sum_series(2,5,8)
  excepted = 13
  assert actual == excepted
  