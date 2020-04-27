from z3c.formwidget.query.interfaces import IQuerySource
from zope.interface import implementer
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm


@implementer(IQuerySource)
class ItalianCities(object):

    vocabulary = SimpleVocabulary((
        SimpleTerm(u'Bologna', 'bologna', u'Bologna'),
        SimpleTerm(u'Roma', 'roma', u'Roma'),
        SimpleTerm(u'Milano', 'milano', u'Milano'),
        SimpleTerm(u'Palermo', 'palermo', u'Palermo'),
        SimpleTerm(u'Sorrento', 'sorrento', u'Sorrento')))

    def __init__(self, context):
        self.context = context

    def __contains__(self, value):
        return self.vocabulary.__contains__(value)

    def getTerm(self, value):
        return self.vocabulary.getTerm(value)

    def getTermByToken(self, value):
        return self.vocabulary.getTermByToken(value)

    def search(self, query_string):
        return [v for v in self.vocabulary if query_string.lower() in v.value.lower()]


@implementer(IContextSourceBinder)
class ItalianCitiesSourceBinder(object):

    def __call__(self, context):
        return ItalianCities(context)