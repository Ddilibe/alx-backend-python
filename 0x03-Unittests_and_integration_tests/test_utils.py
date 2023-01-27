#!/usr/bin/env python3
""" Script for parameterizing a unit test """
from utils import access_nested_map
from unittest import TestCase
from parameterized import parameterized


class TestAccessNestedMap(TestCase):
	"""
		Class for Unittesting access nested map
	"""

	@parameterized.expand([
		({"a": 1}, ("a",), 1),
		({"a": {"b": 2}}, ("a",), {"b": 2}),
		({"a": {"b": 2}}, ("a", "b"), 2)
	])
	def test_access_nested_map(self, nested_map, path, ans):
		"""
			Method for Unittesting access nested map
		"""
		self.assertEqual(access_nested_map(nested_map, path), ans)

	
