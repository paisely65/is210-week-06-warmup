#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This docstring creates and slices tuples."""

import data

DIRECTIONS = data.DIRECTIONS

DIRECTIONS = list(DIRECTIONS[:len(DIRECTIONS) - 1])

DIRECTIONS.append('West')

DIRECTIONS = tuple(DIRECTIONS)
