# -*- coding: utf-8 -*-

from django import forms
from django.contrib import admin
from models import Personal
from ckeditor.widgets import CKEditorWidget

class PersonalAdminForm(forms.ModelForm):
    welcome_message = forms.CharField(widget=CKEditorWidget())
    footer = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Personal

class PersonalAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_display_links = ('name', 'email')
    form = PersonalAdminForm

admin.site.register(Personal, PersonalAdmin)

