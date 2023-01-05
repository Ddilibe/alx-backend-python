#!/usr/bin/env python3

""" Script for basic annotation duck typing first element of a sequence """
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        Function that returns the first element in a sequence

        Args:
            :param lst: This argument is one with any type

        Return:
            Returns the first element in a sequence
    """
    if lst:
        return lst[0]
    else:
        return None
