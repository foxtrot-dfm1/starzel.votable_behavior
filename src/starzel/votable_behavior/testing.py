# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    PLONE_FIXTURE,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
    applyProfile,
)
from plone.testing import z2

import starzel.votable_behavior


class StarzelVotableBehaviorLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=starzel.votable_behavior)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'starzel.votable_behavior:default')


STARZEL_VOTABLE_BEHAVIOR_FIXTURE = StarzelVotableBehaviorLayer()


STARZEL_VOTABLE_BEHAVIOR_INTEGRATION_TESTING = IntegrationTesting(
    bases=(STARZEL_VOTABLE_BEHAVIOR_FIXTURE,),
    name='StarzelVotableBehaviorLayer:IntegrationTesting',
)


STARZEL_VOTABLE_BEHAVIOR_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(STARZEL_VOTABLE_BEHAVIOR_FIXTURE,),
    name='StarzelVotableBehaviorLayer:FunctionalTesting',
)


STARZEL_VOTABLE_BEHAVIOR_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        STARZEL_VOTABLE_BEHAVIOR_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='StarzelVotableBehaviorLayer:AcceptanceTesting',
)
