from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *

JS, CSS = (
    'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
    'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
    'modeltranslation/js/tabbed_translation_fields.js',
), {
    'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
}

@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ("name", "about")

    class Media:
        js = JS
        css = CSS

@admin.register(Place)
class PlaceAdmin(TranslationAdmin):
    list_display = ('name', 'location', 'price', 'day', 'about')

    class Media:
        js = JS
        css = CSS

@admin.register(Action)
class ActionAdmin(TranslationAdmin):
    list_display = ('title', 'about', 'date')

    class Media:
        js = JS
        css = CSS

@admin.register(Employee)
class EmployeeAdmin(TranslationAdmin):
    list_display = ('first_name', 'last_name', 'position', 'about')

    class Media:
        js = JS
        css = CSS

@admin.register(Comment)
class CommentAdmin(TranslationAdmin):
    list_display = ('full_name', 'country', 'city', 'comment')

    class Media:
        js = JS
        css = CSS

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'place', 'date_time')

@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    list_display = ('place', 'start_date', 'end_date', 'persons', 'about')

