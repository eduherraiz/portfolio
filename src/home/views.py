# -*- coding: utf-8 -*-

from django.views.generic import  TemplateView
from django.template import RequestContext
from django.utils import translation
from unidecode import unidecode


class HomeView(TemplateView):
    template_name = 'home.html'


class ResultadoView(TemplateView):
    template_name = 'resultado.html'

    def get(self, request, *args, **kwargs):
        letters = request.GET.get("l", None)
        context = self.get_words(letters)
        context['request'] = RequestContext(request)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        letters = request.POST.get("l", None)
        context = self.get_words(letters)
        return self.render_to_response(context)

    def get_words(self, letters):

        # Selection dictionary
        cur_language = translation.get_language()
        dictionary = 'dictionarys/%s.dict' % cur_language

        context = {}
        context['letters'] = unicode(letters)

        if letters:
            letters = unidecode(letters.lower())

            words = [line.strip() for line in open(dictionary)]
            final_words = []
            for word in words:
                # Check if the word contains any letter that is in the input
                uword = unidecode(word.decode('utf8'))
                addword = True
                for letter in uword:
                    if not letter in letters:
                        addword = False
                        break

                for letter in letters:
                    if not letter in uword:
                        addword = False
                        break

                if word == letters:
                    addword = False
                    break

                if addword:
                    final_words.append(word)

            final_sorted = sorted(final_words, key=len, reverse=True)
            context['words'] = final_sorted
        return  context