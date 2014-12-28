# -*- coding: utf-8 -*-

from django.db import models

class Profession(models.Model):
    name = models.CharField(blank=True, max_length=300)

    def __unicode__(self):
        return self.name

class Project(models.Model):
    TYPES = (
        ('IMP', 'Important'),
        ('OLD', 'Old'),
        ('NOR', 'Normal'),
    )

    name = models.CharField(max_length=100)
    url = models.URLField()
    free_code_url = models.URLField(blank=True)
    image = models.ImageField(blank=True,upload_to='projects')
    type = models.CharField(max_length=3, choices=TYPES, default='NOR',)
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True,null=True)

    def __unicode__(self):
        return self.name

class Personal(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    description = models.TextField(blank=True)
    professions = models.ManyToManyField(Profession, blank=True)
    interval_profession = models.IntegerField(blank=True, default=3000)
    link_linkedin = models.URLField(blank=True)
    link_twitter = models.URLField(blank=True)
    link_github = models.URLField(blank=True)
    link_facebook = models.URLField(blank=True)
    link_googleplus = models.URLField(blank=True)
    link_youtube = models.URLField(blank=True)
    link_vimeo = models.URLField(blank=True)
    welcome_message = models.TextField(blank=True)
    website = models.URLField(blank=True)
    link_location = models.URLField(blank=True)
    location = models.CharField(blank=True,max_length=50)
    link_blog_rss = models.URLField(blank=True)
    num_blog_entries = models.IntegerField(blank=True, default=3)
    footer = models.TextField(blank=True)
    analytics_code = models.TextField(blank=True)
    projects = models.ManyToManyField(Project, blank=True)

    def __unicode__(self):
        return self.name
