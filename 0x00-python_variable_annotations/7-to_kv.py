#!/usr/bin/env python3

""" Script for the complex types -string and int/float task """

from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        Function that accepts some argument

        Args:
            :param @k - A string argument
            :param @v - A int or float argument

        Return:
            Returns a tuple
    """
    return (k, v*v)
