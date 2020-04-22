from z3c.formwidget.query.interfaces import IQuerySource
from zope.interface import implementer
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm


@implementer(IQuerySource)
class ItalianCities(object):

    vocabulary = SimpleVocabulary((
        SimpleTerm(u'Bologna', 'bologna', u'Bologna'),
        SimpleTerm(u'Palermo', 'palermo', u'Palermo'),
        SimpleTerm(u'Sorrento', 'sorrento', u'Sorrento')))

    def __init__(self, context):
        self.context = context

    __contains__ = vocabulary.__contains__
    __iter__ = vocabulary.__iter__
    getTerm = vocabulary.getTerm
    getTermByToken = vocabulary.getTermByToken

    def search(self, query_string):
        return [v for v in self if query_string.lower() in v.value.lower()]


@implementer(IContextSourceBinder)
class ItalianCitiesSourceBinder(object):

    def __call__(self, context):
        return ItalianCities(context)