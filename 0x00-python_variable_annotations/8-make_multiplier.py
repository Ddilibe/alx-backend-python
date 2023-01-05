#!/usr/bin/env python3

""" Script for basic annotation complex types functions task """
from typing import Callable


def make_multiplier(multipler: float) -> Callable[[float], float]:
    """
        Function that returns a function

        Args:
            :param @multipler - A float argument

        Return:
            Returns a function
    """

    def change(number: float) -> float:
        """
            Function that is inside the make_multipler function

            Args:
                :params @number - A float argument

            Return
                Returns a float
        """
        return multipler * number
    return change
