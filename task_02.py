#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This docstring interacts with lists and performs some functions."""

import data
BALLETS = data.BALLETS
del BALLETS[11]
BALLETS[1] = 'Swan Lake'
print BALLETS
BALLETS.append('Herman Schmerman')
print BALLETS
BALLETS.extend(['Don Quixote'])
BALLETS.extend(['Sylvia'])
