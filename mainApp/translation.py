from .models import *
from modeltranslation.translator import TranslationOptions, register

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'about')

@register(Place)
class PlaceTranslationOptions(TranslationOptions):
    fields = ('name', 'location', 'about')

@register(Action)
class ActionTranslationOptions(TranslationOptions):
    fields = ('title', 'about')

@register(Employee)
class EmployeeTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'position', 'about')

@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('full_name', 'comment', 'country', 'city')
