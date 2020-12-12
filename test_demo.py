# -*- coding = utf-8 -*-
# Time : 2020/12/12 18:53
# File : test_demo.py

import pytest

def add_func(a,b):
    return a+b

# @pytest.mark.parametrize("a,b,expected",[
#     (3,5,8),(-1,-2,-3),(10,10,20)
# ],ids=["int","minus","bigint"])
# def test_add(a,b,expected):
#     assert add_func(a,b) == expected

@pytest.mark.parametrize("a",[0,1])
@pytest.mark.parametrize("b",[2,3])
def test_add(a,b):
    print("测试数据组合：a->%s,b->%s"%(a,b))