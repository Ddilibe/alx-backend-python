#!/usr/bin/env python3

""" Script for basic annotation complex type - list of floats """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
        Function to add the component of a list

        Args:
            :param @input_list : A list of floats

        Returns:
            Returns a float
    """
    return sum(input_list)
