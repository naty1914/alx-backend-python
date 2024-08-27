#!/usr/bin/env python3
""" A module that defines unit tests """
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any, Dict
from unittest.mock import patch, Mock


class TestAcessNestedMap(unittest.TestCase):
    """A class that defines unit tests for access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Any):
        """It tests access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence, exception: Exception):
        """It tests access_nested_map exception"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """A class that defines unit tests for get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url: str, test_payload: Dict) -> None:
        """It tests get_json"""
        attribute = {'json.return_value': test_payload}
        result = get_json(url)
        with patch('return.get', return_value=Mock(**attribute)) as mock_get:
            self.assertEqual(result, test_payload)
            mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """A class that defines unit tests function memoize"""
    def test_memoize(self):
        """It tests memoize"""

        class TestClass:
            """A class that defines unit tests for memoize"""
            def a_method(self):
                """A method that returns 42"""
                return 42

            @memoize
            def a_property(self):
                """A property that calls a_method"""
                return self.a_method()
        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_method:
            test = TestClass()
            self.assertEqual(test.a_property, 42)
            self.assertEqual(test.a_property, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
