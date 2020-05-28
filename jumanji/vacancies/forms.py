from django import forms
from django.forms import ModelForm
from .models import Company


class ApplicationForm(forms.Form):
    written_username = forms.CharField(
        label='Вас зовут',
        max_length=50)
    written_phone = forms.IntegerField(
        label='Ваш телефон',
        max_value=99999999999,
        min_value=10000000000)
    written_cover_letter = forms.CharField(
        label='Сопроводительное письмо',
        max_length=2000)


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        labels = {
            'name': 'Название компании',
            'logo': 'Логотип',
            'employee_count': 'Количество человек в компании',
            'location': 'География',
            'description': 'Информация о компании'
        }
        exclude = ['owner']


form = CompanyForm()


class CompanyEditForm(ModelForm):
    class Meta:
        model = Company
        exclude = ['name', 'logo', 'employee_count', 'location', 'description', 'owner']
