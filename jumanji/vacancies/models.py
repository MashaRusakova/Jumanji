from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from jumanji.settings import MEDIA_SPECIALITY_IMAGE_DIR,\
    MEDIA_COMPANY_IMAGE_DIR

# Create your models here.


class Specialty(models.Model):
    code = models.CharField(max_length=20)   # Код
    title = models.CharField(max_length=100)  # Название
    picture = models.ImageField(
        upload_to=MEDIA_SPECIALITY_IMAGE_DIR
    )  # Картинка

    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField(max_length=100)  # Название
    logo = models.ImageField(
        upload_to=MEDIA_COMPANY_IMAGE_DIR,
        null=True,
        blank=True
    )  # Логотипчик
    employee_count = models.IntegerField(blank=True)
    location = models.CharField(max_length=50, blank=True)  # Город
    description = models.TextField(max_length=500, blank=True)
    owner = models.ForeignKey(User,
                              blank=True,
                              null=True,
                              on_delete=models.SET_NULL)    # Владелец


class Vacancy(models.Model):
    title = models.CharField(max_length=100)    # Название вакансии
    specialty = models.ForeignKey(
        Specialty,
        related_name="vacancies",
        on_delete=models.CASCADE
    )
    salary_min = models.IntegerField()  # Зарплата от
    salary_max = models.IntegerField()  # Зарплата до
    skills = models.CharField(max_length=300,
                              blank=True)  # Навыки
    description = models.TextField(max_length=500,
                                   blank=True)  # Текст
    company = models.ForeignKey(Company,
                                related_name="vacancies",
                                on_delete=models.CASCADE
                                )
    published_at = models.DateField()   # Опубликовано

    def __str__(self):
        return self.title


class Application(models.Model):
    written_username = models.CharField(max_length=100)
    written_phone = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999999999),
                    MinValueValidator(10000000000)]
    )
    written_cover_letter = models.CharField(max_length=500)
    vacancy = models.ForeignKey(Vacancy,
                                related_name="applications",
                                on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User,
                             related_name="applications",
                             on_delete=models.CASCADE)
