# -*- coding: utf-8 -*-

from django import forms
from django.contrib import admin
from models import Profession, Personal
from ckeditor.widgets import CKEditorWidget
from django.forms import TextInput
from django.db import models

class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)

class PersonalAdminForm(forms.ModelForm):
    welcome_message = forms.CharField(widget=CKEditorWidget())
    footer = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Personal

class PersonalAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_display_links = ('name', 'email')
    form = PersonalAdminForm
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'website',)
        }),
        ('Messages', {
            'classes': ('collapse',),
            'fields': ('description', 'welcome_message', 'footer')
        }),
        ('Profession', {
            'classes': ('collapse',),
            'fields': ('professions', 'interval_profession',)
        }),
        ('Location', {
            'classes': ('collapse',),
            'fields': ('location','link_location',)
        }),
        ('Social links', {
            'classes': ('collapse',),
            'fields': ('link_linkedin', 'link_twitter', 'link_github', 'link_facebook', 'link_googleplus',
                       'link_youtube', 'link_vimeo')
        }),
        ('Blog', {
            'classes': ('collapse',),
            'fields': ('link_blog_rss', 'num_blog_entries')
        }),
        ('Analytics', {
            'classes': ('collapse',),
            'fields': ('analytics_code',)
        })
    )

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
    }

    filter_horizontal = ('professions', )

admin.site.register(Personal, PersonalAdmin)
admin.site.register(Profession, ProfessionAdmin)

