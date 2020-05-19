from django.db import models

# Create your models here.


class Specialty(models.Model):
    code = models.CharField(max_length=20)   # Код (code)
    title = models.CharField(max_length=100)  # Название (title)
    picture = models.ImageField()  # Картинка


class Company(models.Model):
    name = models.CharField(max_length=100)  # Название
    location = models.CharField(max_length=50, blank=True)  # Город
    logo = models.ImageField(blank=True)  # Логотипчик(logo)
    description = models.TextField(max_length=500, blank=True)
    employee_count = models.IntegerField(blank=True)


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
