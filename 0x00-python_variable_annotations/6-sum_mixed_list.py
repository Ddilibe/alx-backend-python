#!/usr/bin/env python3

""" Script for the basic annotation complex types mixed list task """

from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
        Function that finds the sum of a list containing integers and floats

        Args:
            :param @mxd_list - A list containing integers and float

        Returns:
            Returns a float
    """
    return sum(mxd_list)
