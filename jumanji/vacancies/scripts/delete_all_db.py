# from django.db import models
# import django_extensions
# from django.urls import reverse
# import datetime
#
# from .data import jobs, companies, specialties
# from ..models import Specialty, Company, Vacancy
#
#
# def run():
#     # delete all objects from database
#     Company.objects.all().delete()
#     Vacancy.objects.all().delete()
#     Specialty.objects.all().delete()
#
#     for speciality in specialties:
#         for key, value in speciality.items():
#             speciality_model = Specialty.objects.create(
#                 code=speciality['code'],
#                 title=speciality['title'],
#                 picture='https://place-hold.it/100x60')
#
#     for company in companies:
#         for value in company.values():
#             company_model = Company.objects.create(
#             name=value, employee_count=1)
#
#     for job in jobs:
#         for key, value in job.items():
#             vacancy_model = Vacancy.objects.create(
#                 title=job['title'],
#                 specialty=speciality_model,
#                 company=company_model,
#                 salary_min=job['salary_from'],
#                 salary_max=job['salary_to'],
#                 published_at=job['posted'])
