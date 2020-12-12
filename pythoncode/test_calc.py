# -*- coding = utf-8 -*-
# Time : 2020/12/12 20:15
# File : test_calc.py

import pytest
from pythoncode.calculate import Calculator

class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("开始计算")
    def teardown_class(self):
        print("计算结束")
    @pytest.mark.parametrize("a,b,expect",[
        (1,2,3),(-1,-2,-3),(10,20,30)
    ],ids=["addone","addtwo","addthree"])
    def test_add(self,a,b,expect):
        assert expect == self.calc.add(a,b)

    @pytest.mark.parametrize("a,b,expect", [
        (3, 2, 1), (-1, -2, 1), (100, 20, 80)
    ], ids=["subone", "subtwo", "subthree"])
    def test_sub(self, a, b, expect):
        assert expect == self.calc.sub(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (3, 2, 6), (-1, -2, 2), (100, 20, 2000)
    ], ids=["mulone", "multwo", "multhree"])
    def test_mul(self, a, b, expect):
        assert expect == self.calc.mul(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (2, 2, 1), (-2, -2, 1), (100, 20, 5)
    ], ids=["divone", "divtwo", "divthree"])
    def test_div(self, a, b, expect):
        assert expect == self.calc.div(a, b)