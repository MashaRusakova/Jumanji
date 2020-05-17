#  from django.db import models
#  from django.urls import reverse
#
#  from .data import jobs
#  from .data import companies
#  from .data import specialties
#  from jumanji.vacancies.models import Specialty
#  from jumanji.vacancies.models import Company
#  from jumanji.vacancies.models import Vacancy
#
# for speciality in specialties:
#     for key, value in speciality.items():
#         print(key, value)
        # speciality_model = Specialty.objects.create(code=speciality["code"],
        #                                             title=speciality["title"],
        #                                             picture='https://place-hold.it/100x60')

# for company in companies:
#     for value in company.values():
#         company_model = Company.objects.create(name='value')
#
# for job in jobs:
#     for key, value in job.items():
#         vacancy_model = Vacancy.objects.create(title='job["title"]',
#                                                specialty='job["cat"]',
#                                                company='job["company"]',
#                                                salary_min='job["salary_from"]',
#                                                salary_max='job["salary_to"]',
#                                                published_at='job["posted"]')
#
# speciality_model.save()
# company_model.save()
# vacancy_model.save()
