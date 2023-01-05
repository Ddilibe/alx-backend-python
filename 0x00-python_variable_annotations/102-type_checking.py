#!/usr/bin/env python3

""" Script containing code for testing type checking """
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
        Function called the zoom_array

        Args:
            :param @lst - A tuple argument
            :param factor - An integer argument

        Return:
            Returns a list of values
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x: List = zoom_array(array)

zoom_3x: List = zoom_array(array, 3)
