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

	@parameterized.expand([
		({}, ("a",)),
		({"a": 1}, ("a", "b"))
	])
	def test_Access_nested_map_exception(self, nested_map, path):
		"""
			Method for unittesting access nested map
		"""
		args = [nested_map, path]
		with self.assertRaises(KeyError):
			access_nested_map(*args)
