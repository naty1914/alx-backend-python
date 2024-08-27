#!/usr//bin/env python3
""" A module that defines unit tests """
from typing import Dict
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, MagicMock, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """ A class that defines unit tests for GithubOrgClient """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, mock_get: MagicMock) -> None:
        """It tests org for GithubOrgClient"""
        test = GithubOrgClient(org_name)
        test.org()
        mock_get.assert_called_once_with(test.ORG_URL.format(org=org_name))

    def test_public_repos_url(self):
        """It tests public_repos_url"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            P_load = {'repos_url': "Hello World"}
            mock.return_value = P_load
            test = GithubOrgClient('test')
            res = test._public_repos_url
            self.assertEqual(res, P_load['repos_url'])

    @patch("client.get_json")
    def test_public_repos(self, mock_get: MagicMock) -> None:
        """It tests public_repos for GithubOrgClient"""
        p_load = [{'name': 'Google'}, {'name': 'Twitter'}]
        mock_get.return_value = p_load
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_Pub:
            mock_Pub.return_value = "hello world"
            test = GithubOrgClient('test')
            res = test.public_repos()
            expected = [item["name"] for item in p_load]
            self.assertEqual(res, expected)
            mock_Pub.assert_called_once()
            mock_get.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict, license_key: str,
                         expected: bool) -> None:
        """It tests has_license for GithubOrgClient"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)
