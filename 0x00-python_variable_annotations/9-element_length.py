#!/usr/bin/env python3

""" Script for basic annotation for duck typing an iterable object """

from typing import Tuple, Iterable, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        Function tha does an operation to the argument

        Args:
            :params @lst - An iterable

        Returns:
            Returns a list of tuples of ints
    """
    return [(i, len(i)) for i in list]
