#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    max_length = a + b
    min_length = a - b
    if min_length < 0: min_length *= -1
    if c >= max_length or c <= min_length:
        raise TriangleError("Not a legal triangle!")

    triangle_set = {a, b, c}
    for item in triangle_set:
        if item <= 0:
            raise TriangleError("Not a legal side length!")

    if len(triangle_set) == 1:
        return "equilateral"
    elif len(triangle_set) == 2:
        return "isosceles"
    else:
        return "scalene"

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
