# from django.db import models
# from django.urls import reverse
# import datetime
#
# from .data import jobs, companies, specialties
# from jumanji.vacancies.models import Specialty, Company, Vacancy
#
#
#
# for speciality in specialties:
#     for key, value in speciality.items():
#         print(key, value)
#         speciality_model = Specialty.objects.create(code=speciality['code'],
#                                                     title=speciality['title'],
#                                                     picture='https://place-hold.it/100x60')
#
# for company in companies:
#     for value in company.values():
#         company_model = Company.objects.create(name=value)
#
# for job in jobs:
#     for key, value in job.items():
#         vacancy_model = Vacancy.objects.create(title=job['title'],
#                                                specialty=job['cat'],
#                                                company=job['company'],
#                                                salary_min=job['salary_from'],
#                                                salary_max=job['salary_to'],
#                                                published_at=job['posted'])
#
# speciality_model.save()
# company_model.save()
# vacancy_model.save()
