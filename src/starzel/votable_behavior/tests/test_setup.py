# -*- coding: utf-8 -*-
"""Setup tests for this package."""
import unittest

from plone import api
from plone.app.testing import TEST_USER_ID, setRoles

from starzel.votable_behavior.testing import (  # noqa: E501
    STARZEL_VOTABLE_BEHAVIOR_INTEGRATION_TESTING,
)

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that starzel.votable_behavior is properly installed."""

    layer = STARZEL_VOTABLE_BEHAVIOR_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if starzel.votable_behavior is installed."""
        self.assertTrue(self.installer.is_product_installed(
            'starzel.votable_behavior'))

    def test_browserlayer(self):
        """Test that IStarzelVotableBehaviorLayer is registered."""
        from plone.browserlayer import utils

        from starzel.votable_behavior.interfaces import IStarzelVotableBehaviorLayer
        self.assertIn(
            IStarzelVotableBehaviorLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = STARZEL_VOTABLE_BEHAVIOR_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstall_product('starzel.votable_behavior')
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if starzel.votable_behavior is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed(
            'starzel.votable_behavior'))

    def test_browserlayer_removed(self):
        """Test that IStarzelVotableBehaviorLayer is removed."""
        from plone.browserlayer import utils

        from starzel.votable_behavior.interfaces import IStarzelVotableBehaviorLayer
        self.assertNotIn(IStarzelVotableBehaviorLayer, utils.registered_layers())
