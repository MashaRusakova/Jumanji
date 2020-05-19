from django.shortcuts import render

from django.http import Http404, HttpResponseNotFound
from django.db.models import Count
from django.views import View
from .models import Specialty, Company, Vacancy


# Create your views here.
class MainView(View):
    def get(self, request):
        specialties = Specialty.objects.all().\
            annotate(count=Count('vacancies'))
        companies = Company.objects.all().\
            annotate(count=Count('vacancies'))

        return render(request, 'index.html', context={
            'specialties': specialties,
            'companies': companies,
        }
                      )


class VacanciesView(View):
    def get(self, request):
        jobs = Vacancy.objects.all()
        number_of_vacancies = len(jobs)

        return render(request, 'vacancies.html', context={
            'jobs': jobs,
            'number_of_vacancies': number_of_vacancies,
        }
                      )


class SpecializationView(View):
    def get(self, request, specialty):
        specialties = Specialty.objects.filter(code=specialty).first()
        if not specialties:
            raise Http404

        number_of_vacancies = len(specialties.vacancies.all())
        return render(request, 'vacancies_specialties.html', context={
            'specialties': specialties,
            'vacancies': specialties.vacancies.all(),
            'number_of_vacancies': number_of_vacancies,
        }
                      )


class CompanyView(View):
    def get(self, request, id):
        сompany = Company.objects.filter(id=id).first()
        if not сompany:
            raise Http404

        name = сompany.name
        number_of_vacancies = len(сompany.vacancies.all())

        return render(request, 'company.html', context={
            'сompany': сompany,
            'name': name,
            'number_of_vacancies': number_of_vacancies,
            'vacancies': сompany.vacancies.all(),
        }
                      )


class VacancyView(View):
    def get(self, request, id):
        vacancy = Vacancy.objects.filter(id=id).first()
        if not vacancy:
            raise Http404
        context = {'vacancy': vacancy}
        return render(request, 'vacancy.html', context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, такой страницы нет!')
