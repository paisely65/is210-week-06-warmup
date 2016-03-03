#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This docstring modifies a list"""


def flip_keys(to_flip):
    """This function that shows mutability.

    Args:
        to_flip(list): The input is a list.

    Returns:
        list:The original list is reversed.

    Examples:
        >>>flip_keys(['pepper'], ['salt'], [10, 20, 30])

        >>>flip_keys(['hello','world'])

    """
    tally = 0
    for item in to_flip:
        to_flip[tally] = item[::-1]
        tally += 1

    return to_flip
       

