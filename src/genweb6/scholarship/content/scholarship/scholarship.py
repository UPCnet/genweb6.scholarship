# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView

from plone import api
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.dexterity.interfaces import IDexteritySchema
from plone.supermodel import model
from zope import schema
from zope.interface import implementer
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

from genweb6.core.utils import pref_lang
from genweb6.core.widgets import FieldsetFieldWidget
from genweb6.scholarship import _


sch_types = [u"Estudis", u"Mobilitat", ]


def build_vocabulary(values):
    return SimpleVocabulary([
        SimpleTerm(title=_(value), value=value, token=token)
        for token, value in enumerate(values)])


class IScholarship(model.Schema, IDexteritySchema):
    """ Scholarship schema """

    directives.widget('fieldset_info', FieldsetFieldWidget)
    fieldset_info = schema.Text(
        default=_(u'General information'),
        required=False,
    )

    summary = RichText(
        title=_(u"Summary"),
        required=True,
    )

    scholarship_type = schema.Choice(
        title=_(u'scholarship_type'),
        required=True,
        vocabulary=SimpleVocabulary(build_vocabulary(sch_types))
    )

    organism = RichText(
        title=_(u"Responsible Organism"),
        description=_(u""),
        required=True,
    )

    recipients = RichText(
        title=_(u"Recipients"),
        description=_(u""),
        required=True,
    )

    others = RichText(
        title=_(u"Others"),
        description=_(u""),
        required=False,
    )

    directives.widget('fieldset_requirements', FieldsetFieldWidget)
    fieldset_requirements = schema.Text(
        default=_(u'Requirements'),
        required=False,
    )

    general_requirements = RichText(
        title=_(u"General requirements"),
        description=_(u""),
        required=False,
    )

    academic_requirements = RichText(
        title=_(u"Academic requirements"),
        description=_(u""),
        required=False,
    )

    economic_requirements = RichText(
        title=_(u"Economic requirements"),
        description=_(u""),
        required=False,
    )

    incompatibilities = RichText(
        title=_(u"Incompatibilities"),
        description=_(u""),
        required=False,
    )

    directives.widget('fieldset_request', FieldsetFieldWidget)
    fieldset_request = schema.Text(
        default=_(u'Request'),
        required=False,
    )

    start_date = schema.Date(
        title=_(u"Application start date"),
        description=_(u""),
        required=False,
    )

    deadline = schema.Date(
        title=_(u"Application deadline"),
        description=_(u""),
        required=False,
    )

    submission = RichText(
        title=_(u"Application submission"),
        description=_(u""),
        required=False,
    )

    documentation = RichText(
        title=_(u"Additional documentation"),
        description=_(u""),
        required=False,
    )

    directives.widget('fieldset_scholarship', FieldsetFieldWidget)
    fieldset_scholarship = schema.Text(
        default=_(u'Scholarship'),
        required=False,
    )

    amount = RichText(
        title=_(u"General amount of scholarship"),
        description=_(u""),
        required=False,
    )

    additional_amount = RichText(
        title=_(u"Additional amounts of scholarship"),
        description=_(u""),
        required=False,
    )

    duration = RichText(
        title=_(u"Duration of the grant"),
        description=_(u""),
        required=False,
    )

    payment = RichText(
        title=_(u"Payment"),
        description=_(u""),
        required=False,
    )

    beneficiaries = RichText(
        title=_(u"Obligations of the beneficiaries"),
        description=_(u""),
        required=False,
    )

    directives.widget('fieldset_award', FieldsetFieldWidget)
    fieldset_award = schema.Text(
        default=_(u'Award'),
        required=False,
    )

    criteria = RichText(
        title=_(u"Award criteria"),
        description=_(u""),
        required=False,
    )

    award_date = schema.Date(
        title=_(u"Award's resolution date"),
        description=_(u""),
        required=False,
    )

    award_resolution = RichText(
        title=_(u"Award's resolution"),
        description=_(u""),
        required=False,
    )

    allegations = RichText(
        title=_(u"Allegations"),
        description=_(u""),
        required=False,
    )

    directives.widget('fieldset_more', FieldsetFieldWidget)
    fieldset_more = schema.Text(
        default=_(u'More information'),
        required=False,
    )

    regulations = RichText(
        title=_(u"Regulations"),
        description=_(u""),
        required=False,
    )


@implementer(IScholarship)
class Scholarship(Item):
    pass


class View(BrowserView):

    def getContactPage(self):
        folder = api.portal.get()[pref_lang()]
        if 'contact' in folder and folder['contact'].text:
            return folder['contact'].text.output
        return False
