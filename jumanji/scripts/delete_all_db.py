# from django.db import models
# import django_extensions
# from django.urls import reverse
# import datetime

#from jumanji.data import jobs, companies, specialties
from jumanji.vacancies.models import Speciality, Company, Vacancy


def run():
    # delete all objects from database
    Company.objects.all().delete()
    Vacancy.objects.all().delete()
    Speciality.objects.all().delete()

    vacancy = Vacancy.objects.create(title='Разработчик на Python',
                                     specialty='backend',
                                     company='staffingsmarter',
                                     salary_min=10000,
                                     salary_max=150000,
                                     published_at='2020-03-11')
    vacancy.save()
