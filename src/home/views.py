# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.views.generic import FormView


from home.forms import ContactForm
from home.models import Personal

class HomeView(SuccessMessageMixin, FormView):
    template_name = 'home.html'
    form_class = ContactForm
    success_url = '/'
    success_message = "Gracias por contactar"

    def form_valid(self, form):
        message = u"{nombre} / {email} dijo: ".format(
            nombre=form.cleaned_data.get('nombre'),
            email=form.cleaned_data.get('email'))
        message += u"\n\n{0}".format(form.cleaned_data.get('mensaje'))

        subject, from_email, to = 'Mensaje desde eduherraiz.com', settings.EMAIL_FROM, settings.LIST_OF_EMAIL_RECIPIENTS
        text_content = message
        html_content = message
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to], headers={'Reply-To': form.cleaned_data.get('email')})
        msg.attach_alternative(html_content, "text/html")

        msg.send()

        return super(HomeView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['personal'] = Personal.objects.first()
        return context