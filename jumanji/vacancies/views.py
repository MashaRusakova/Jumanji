from django.shortcuts import render

from django.http import HttpResponse
from django.views import View
from .models import Speciality, Company, Vacancy

# Create your views here.
class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', context={})

class VacanciesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancies.html', context={})

class SpecializationView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancies.html', context={})

class CompanyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'company.html', context={})

class VacancyView(View):
    def get(self, request, id):
        vacancy = Vacancy.objects.get(id=id)
        return render(request, 'vacancy.html', context={'vacancy': vacancy})

