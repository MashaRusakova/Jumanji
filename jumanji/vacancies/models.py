from django.db import models
from django.contrib.auth.models import User

from jumanji.settings import MEDIA_SPECIALITY_IMAGE_DIR,\
    MEDIA_COMPANY_IMAGE_DIR

# Create your models here.


class Specialty(models.Model):
    code = models.CharField(max_length=20)   # Код (code)
    title = models.CharField(max_length=100)  # Название (title)
    picture = models.ImageField(upload_to=MEDIA_SPECIALITY_IMAGE_DIR)  # Картинка


class Company(models.Model):
    name = models.CharField(max_length=100)  # Название
    logo = models.ImageField(upload_to=MEDIA_COMPANY_IMAGE_DIR)  # Логотипчик
    employee_count = models.IntegerField(blank=True)
    location = models.CharField(max_length=50, blank=True)  # Город
    description = models.TextField(max_length=500, blank=True)
    owner = models.ForeignKey(User,
                              blank=True,
                              null=True,
                              on_delete=models.SET_NULL)    # Владелец


class Vacancy(models.Model):
    title = models.CharField(max_length=100)    # Название вакансии
    specialty = models.ForeignKey(Specialty,
                                  related_name="vacancies",
                                  on_delete=models.CASCADE
                                  )
    company = models.ForeignKey(Company,
                                related_name="vacancies",
                                on_delete=models.CASCADE
                                )
    skills = models.CharField(max_length=300, blank=True)   # Навыки
    description = models.TextField(max_length=500, blank=True)  # Текст
    salary_min = models.IntegerField()    # Зарплата от
    salary_max = models.IntegerField()    # Зарплата до
    published_at = models.DateField()   # Опубликовано


class Application(models.Model):
    written_username = models.CharField(max_length=100)     # Имя
    written_phone = models.IntegerField()  # Телефон
    written_cover_letter = models.CharField(max_length=500)     # Сопроводительное письмо
    vacancy = models.ForeignKey(Vacancy,
                                related_name="applications",
                                on_delete=models.CASCADE)  # Вакансия
    user = models.ForeignKey(User,
                             related_name="applications",
                             on_delete=models.CASCADE)   # Пользователь


