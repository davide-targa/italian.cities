# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import italian.cities


class ItalianCitiesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=italian.cities)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'italian.cities:default')


ITALIAN_CITIES_FIXTURE = ItalianCitiesLayer()


ITALIAN_CITIES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ITALIAN_CITIES_FIXTURE,),
    name='ItalianCitiesLayer:IntegrationTesting',
)


ITALIAN_CITIES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ITALIAN_CITIES_FIXTURE,),
    name='ItalianCitiesLayer:FunctionalTesting',
)


ITALIAN_CITIES_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ITALIAN_CITIES_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='ItalianCitiesLayer:AcceptanceTesting',
)
