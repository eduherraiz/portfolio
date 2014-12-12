# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import FormView

from home.forms import ContactForm


class HomeView(FormView):
    template_name = 'home.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        message = "{nombre} / {email} dijo: ".format(
            nombre=form.cleaned_data.get('nombre'),
            email=form.cleaned_data.get('email'))
        message += "\n\n{0}".format(form.cleaned_data.get('mensaje'))
        send_mail(
            subject='Mensaje desde eduherraiz.com',
            message=message,
            from_email=form.cleaned_data.get('email'),
            recipient_list=[settings.LIST_OF_EMAIL_RECIPIENTS],
        )
        return super(HomeView, self).form_valid(form)