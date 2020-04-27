from italian.cities.sources import ItalianCitiesSourceBinder
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.supermodel import model
from plone.formwidget.autocomplete import AutocompleteFieldWidget
from zope.interface import implementer
from zope import schema


class ICity(model.Schema):
    """ Marker interface and Dexterity Python Schema for City
    """
    directives.widget(city=AutocompleteFieldWidget)
    city = schema.Choice(
        title=u"City name",
        description=u"For example: Bologna, Roma, etc...",
        source=ItalianCitiesSourceBinder(),
        required=False,
    )


@implementer(ICity)
class City(Item):
    """
    """
