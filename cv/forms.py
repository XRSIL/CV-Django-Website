from django import forms
from django.core.mail import send_mail


# Create your forms here.

class ContactForm(forms.Form):
    def styling(*args):
        return forms.TextInput(attrs={
            'style': str(*args),
        })

    name = forms.CharField(max_length=75, label="Ваше Имя:", widget=styling('margin-top: 7px; font-size: 14px'))
    company = forms.CharField(max_length=100, label="Название компании:", widget=styling('margin-top: 7px; '
                                                                                         'font-size: 14px'))
    email = forms.EmailField(max_length=150, label="Ваш Email", widget=styling('margin-top: 7px; font-size: 14px'))
    message = forms.CharField(widget=forms.Textarea(attrs={'style':'margin-top: 7px; font-size: 14px'}),
                              max_length=2000, label="Сообщение:")

    def result(self):
        return send_mail(self.data["name"] + ' from company ' + self.data["company"], self.data['message'],
                         'main_mail_of_ilya_site@gmail.com', [self.data['email']])
