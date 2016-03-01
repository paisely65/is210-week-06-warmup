#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This docstring creates and slices tuples."""

import data
DIRECTIONS = data.DIRECTIONS
a = DIRECTIONS[3]
c = DIRECTIONS[:3]
b = DIRECTIONS[3][10:18]
DIRECTIONS = DIRECTIONS[:3], DIRECTIONS[3][10:18]
print DIRECTIONS




