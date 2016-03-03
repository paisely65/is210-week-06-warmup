#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This docstring creates a for loop"""


def process_data(data):
    """This function calculates sum and average using data froma tuple

    Args:
        data(mixed):String or integers

    Returns:
        mysum(int):Sum of the data in the tuple
        myaverage(int): Average of the data in the tuple

    Example:

        >>> process_data([2, 4, 6])
        (12, 4.0)

        """
    mysum = 0
    for mynum in data:
        mysum += mynum
    myavg = (mysum / float(len(data)))
    return(mysum, myavg)
