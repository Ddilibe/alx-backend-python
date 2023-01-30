#!/usr/bin/env python3
""" Script for parameterizing a unit test """
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch
from unittest import TestCase
import requests


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
	def test_access_nested_map_exception(self, nested_map, path):
		"""
			Method for unittesting access nested map
		"""
		args = [nested_map, path]
		with self.assertRaises(KeyError):
			access_nested_map(*args)

class TestGetJson(TestCase):
	"""docstring for TestGetJson"""
	@parameterized.expand([
		("http://example.com", {"payload": True}),
		("http://holberton.io", {"payload": False})
	])
	@patch('requests.get')
	def test_get_json(self, test_url, test_payload, patch_method):
		""" Method for testing the get_jsin function in utils """
		patch_method.return_value.json.return_value = test_payload
		a = get_json(test_url)
		self.assertEqual(a, test_payload)
		patch_method.assert_called_once_with(test_url)

class TestMemoize(TestCase):
	"""docstring for TestMemoize"""
	@patch('memoize')
	def test_memoize(self):
		""" Method for testing memoize """
		class TestClass:

			def a_method(self):
				""" Method that returns 47 """
				return 47

			@memoize
			def a_property(self):
				""" Method that returns self.a_method """
				return self.a_method()
		
