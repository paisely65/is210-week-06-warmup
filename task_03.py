#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This docstring creates and slices tuples."""

import data
DIRECTIONS = data.DIRECTIONS
print DIRECTIONS[-1]
print DIRECTIONS[:3]
print DIRECTIONS[:3] + tuple('Western')
