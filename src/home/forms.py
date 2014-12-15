from captcha.fields import ReCaptchaField  # Only import different from yesterday
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import floppyforms as forms

class ContactForm(forms.Form):

    nombre = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    mensaje = forms.CharField(widget=forms.Textarea, required=True)
    suma = forms.CharField(required=True,  label='1+1=?', help_text='Mi filtro anti-robots y anti-personas-que-no-quiero-que-contacten')

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('enviar', 'Enviar'))
        super(ContactForm, self).__init__(*args, **kwargs)