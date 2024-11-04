#!/usr/bin/env python3
"""unittest and parametrization"""
from utils import access_nested_map
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """testing the access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access(self, nested_map, path, expected):
        """testing the access_nested_map with a bunch of outputs"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
