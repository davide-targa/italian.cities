from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.interface import implementer


@implementer(IVocabularyFactory)
class CitiesVocabulary(object):

    def __call__(self, context):
        vocabulary = SimpleVocabulary((
        SimpleTerm(u'Bologna', 'bologna', u'Bologna'),
        SimpleTerm(u'Roma', 'roma', u'Roma'),
        SimpleTerm(u'Milano', 'milano', u'Milano'),
        SimpleTerm(u'Palermo', 'palermo', u'Palermo'),
        SimpleTerm(u'Sorrento', 'sorrento', u'Sorrento')))
        return vocabulary