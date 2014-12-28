from captcha.fields import ReCaptchaField  # Only import different from yesterday
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import floppyforms as forms
from django.utils.translation import ugettext_lazy as _

class ContactForm(forms.Form):

    nombre = forms.CharField(label=_('Nombre'), required=True)
    email = forms.EmailField(label=_('Email'), required=True)
    mensaje = forms.CharField(label=_('Mensaje'), widget=forms.Textarea, required=True)
    captcha = ReCaptchaField(label=_('Antirobot'),required=True)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('enviar', 'Enviar'))
        super(ContactForm, self).__init__(*args, **kwargs)