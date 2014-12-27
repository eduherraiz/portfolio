# -*- coding: utf-8 -*-

from django.db import models

class Personal(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    description = models.TextField(blank=True)
    profession = models.CharField(blank=True, max_length=100)
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
    footer = models.TextField(blank=True)
    analytics_code = models.TextField(blank=True)