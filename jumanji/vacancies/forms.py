from django import forms


class ApplicationForm(forms.Form):
    written_username = forms.CharField(label='Вас зовут')     # Имя
    written_phone = forms.IntegerField(label='Ваш телефон')  # Телефон
    written_cover_letter = forms.CharField(label='Сопроводительное письмо')     # Сопроводительное письмо
