from django.db.models import Count
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
# from django.db import models
from vacancies import models
from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from .models import Company, Vacancy, Specialty, Application
from .forms import ApplicationForm, CompanyForm


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
        vacancies = Vacancy.objects.all()
        number_of_vacancies = len(vacancies)

        return render(request, 'vacancies.html', context={
            'vacancies': vacancies,
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
        company = Company.objects.filter(id=id).first()
        if not company:
            raise Http404

        name = company.name
        logo = company.logo
        number_of_vacancies = len(company.vacancies.all())

        return render(request, 'company.html', context={
            'company': company,
            'name': name,
            'number_of_vacancies': number_of_vacancies,
            'vacancies': company.vacancies.all(),
            'logo': logo,
        }
                      )


class VacancyView(View):
    def get(self, request, id, *args, **kwargs):
        application_form = ApplicationForm()
        vacancy = Vacancy.objects.filter(id=id).first()
        if not vacancy:
            raise Http404
        context = {'vacancy': vacancy, 'application_form': application_form}
        return render(request, 'vacancy.html', context)

    def post(self, request, id, *args, **kwargs):
        if request.method == 'POST':
            application_form = ApplicationForm(request.POST)
            if application_form.is_valid():
                data = application_form.cleaned_data
                application_form.user = request.user
                application = Application(user=request.user,
                                          vacancy=Vacancy.objects.filter(id=id).first(),
                                          written_username=data['written_username'],
                                          written_phone=data['written_phone'],
                                          written_cover_letter=data['written_cover_letter'],
                                          )
                application.save()
                return render(request, 'sent.html')
        else:
            application_form = ApplicationForm()
        return render(request, 'vacancy.html', {'application_form': application_form})


class VacanciesSendView(View):
    def get(self, request,  *args, **kwargs):
        return render(request, 'sent.html', context={})


class MyCompanyEditView(View):
    def get(self, request, *args, **kwargs):
        my_company_req = models.Company.objects.filter(owner=request.user)
        company_form = CompanyForm()
        if len(my_company_req) == 0:
            return render(request,
                          'company-create.html',
                          context={'title': 'Создайте карточку компании'}
                          )
        else:
            return render(request,
                          'company-edit.html',
                          context={'title': 'Моя компания',
                                   'company_form': CompanyForm(instance=my_company_req.first())
                                   }
                          )

    def post(self, request, *args, **kwargs):
        my_company_req = models.Company.objects.filter(owner=request.user)
        company_form = CompanyForm(request.POST, request.FILES)
        if company_form.is_valid():
            company = my_company_req.first()
            company_form = CompanyForm(request.POST,
                                       request.FILES,
                                       instance=company)
            company_form.save()
            return HttpResponseRedirect(request.path, content={'title': 'Моя компания'})
        else:
            return render(
                request, 'company-edit.html',
                context={'title': 'Информация о компании обновлена',
                         'form': CompanyForm(initial={'owner': request.user})
                         }
            )


class MyCompanyCreateView(View):
    def get(self, request, *args, **kwargs):
        my_company_req = models.Company.objects.filter(owner=request.user)
        company_form = CompanyForm()
        return render(request,
                      'company-edit.html',
                      context={'title': 'Создайте карточку компании',
                               'company_form': company_form,
                               }
                      )

    def post(self, request, *args, **kwargs):
        my_company_req = models.Company.objects.filter(owner=request.user)
        company_form = CompanyForm(request.POST, request.FILES)
        if company_form.is_valid():
            company = company_form.save(commit=False)
            company.owner = request.user
            company.save()
            return redirect(request.path, )
        else:
            return render(
                request, 'company-edit.html',
                context={'title': 'Моя компания',
                         'company_form': company_form
                         }
            )


class MyVacanciesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy-list.html', context={})


class MyCompanyVacancyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy-edit.html', context={})


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'
    next = '/'


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = '/login'
    template_name = 'register.html'


# def custom_handler404(request, exception):
#     return HttpResponseNotFound('Ой, такой страницы нет!')
