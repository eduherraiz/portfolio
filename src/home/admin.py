# -*- coding: utf-8 -*-

from django import forms
from django.contrib import admin
from models import Profession, Personal, Project
from ckeditor.widgets import CKEditorWidget
from django.forms import TextInput
from django.db import models
from modeltranslation.admin import TranslationAdmin

class ProfessionAdmin(TranslationAdmin):
    list_display = ('name',)
    list_display_links = ('name',)

class ProjectAdminForm(forms.ModelForm):
    short_description_es = forms.CharField(widget=CKEditorWidget(), required=False)
    short_description_ca = forms.CharField(widget=CKEditorWidget(), required=False)
    short_description_en = forms.CharField(widget=CKEditorWidget(), required=False)
    long_description_es = forms.CharField(widget=CKEditorWidget(), required=False)
    long_description_ca = forms.CharField(widget=CKEditorWidget(), required=False)
    long_description_en = forms.CharField(widget=CKEditorWidget(), required=False)
    class Meta:
        model = Project

class ProjectAdmin(TranslationAdmin):
    list_display = ('name','url', 'type',)
    list_display_links = ('name','url')
    form = ProjectAdminForm

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
    }

class PersonalAdminForm(forms.ModelForm):
    welcome_message_es = forms.CharField(widget=CKEditorWidget(), required=False)
    welcome_message_ca = forms.CharField(widget=CKEditorWidget(), required=False)
    welcome_message_en = forms.CharField(widget=CKEditorWidget(), required=False)
    footer_es = forms.CharField(widget=CKEditorWidget(), required=False)
    footer_ca = forms.CharField(widget=CKEditorWidget(), required=False)
    footer_en = forms.CharField(widget=CKEditorWidget(), required=False)
    class Meta:
        model = Personal

class PersonalAdmin(TranslationAdmin):
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
        ('Projects', {
            'classes': ('collapse',),
            'fields': ('projects',)
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

    filter_horizontal = ('professions', 'projects', )

admin.site.register(Personal, PersonalAdmin)
admin.site.register(Profession, ProfessionAdmin)
admin.site.register(Project, ProjectAdmin)

