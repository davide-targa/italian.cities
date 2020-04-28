from italian.cities.sources import ItalianCitiesSourceBinder
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.supermodel import model
from plone.app.z3cform.widget import AjaxSelectFieldWidget
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.interface import implementer
from zope import schema


class ICity(model.Schema):
    """ Marker interface and Dexterity Python Schema for City
    """
    city = schema.Choice(
        title=u"City name",
        description=u"For example: Bologna, Roma, etc...",
        vocabulary="italian.cities.list"
    )
    directives.widget(
        'city',
        AjaxSelectFieldWidget,
        vocabulary="italian.cities.list"
    )


@implementer(ICity)
class City(Item):
    """
    """
