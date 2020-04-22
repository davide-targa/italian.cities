# -*- coding: utf-8 -*-
from italian.cities.content.city import ICity  # NOQA E501
from italian.cities.testing import ITALIAN_CITIES_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class CityIntegrationTest(unittest.TestCase):

    layer = ITALIAN_CITIES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_city_schema(self):
        fti = queryUtility(IDexterityFTI, name='City')
        schema = fti.lookupSchema()
        self.assertEqual(ICity, schema)

    def test_ct_city_fti(self):
        fti = queryUtility(IDexterityFTI, name='City')
        self.assertTrue(fti)

    def test_ct_city_factory(self):
        fti = queryUtility(IDexterityFTI, name='City')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ICity.providedBy(obj),
            u'ICity not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_city_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='City',
            id='city',
        )

        self.assertTrue(
            ICity.providedBy(obj),
            u'ICity not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('city', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('city', parent.objectIds())

    def test_ct_city_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='City')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )
