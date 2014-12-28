from modeltranslation.translator import translator, TranslationOptions
from models import Personal, Profession, Project

class PersonalTranslationOptions(TranslationOptions):
    fields = ('description','welcome_message', 'footer',)

class ProfessionTranslationOptions(TranslationOptions):
    fields = ('name',)

class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'short_description', 'long_description',)

translator.register(Personal, PersonalTranslationOptions)
translator.register(Profession, ProfessionTranslationOptions)
translator.register(Project, ProjectTranslationOptions)
