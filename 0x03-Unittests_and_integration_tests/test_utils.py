#!/usr/bin/env python3
"""unittest and parametrization"""
from utils import access_nested_map
import unittest
from typing import Mapping, Sequence, Any
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """testing the access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access(self, nested_map: Mapping, path: Sequence,
                    expected: int) -> None:
        """testing the access_nested_map with a bunch of outputs"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_exception(self, nested_map: Mapping,
                       path: Sequence) -> None:
        """raises an exception"""
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)
