from django.db import models
from django.urls import reverse

from .data import jobs
from .data import companies
from .data import specialties

# Create your models here.

class Specialty(models.Model):
    code = models.CharField(max_length=20)   # Код (code) например, testing, gamedev
    title = models.CharField(max_length=100)  # Название (title)
    picture = models.ImageField()  # Картинка (picture) (пока оставьте пустой строкой)

class Company(models.Model):
    name = models.CharField(max_length=100)  # Название
    location = models.CharField(max_length=50, blank=True)  # Город
    description = models.TextField(max_length=500, blank=True)  # Информация о компании
    employee_count = models.FloatField()    # Количество сотрудников

class Vacancy(models.Model):
    title = models.CharField(max_length=100)    # Название вакансии
    specialty = models.ForeignKey(Specialty, related_name="vacancies", on_delete=models.CASCADE)    # Специализация
    company = models.ForeignKey(Company, related_name="vacancies", on_delete=models.CASCADE)    # Компания
    skills = models.CharField(max_length=300, blank=True)   # Навыки
    description = models.TextField(max_length=500, blank=True)  # Текст
    salary_min = models.FloatField()    # Зарплата от
    salary_max = models.FloatField()    # Зарплата до
    published_at = models.DateField()   # Опубликовано
