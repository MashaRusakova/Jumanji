"""jumanji URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

# from vacancies.views import custom_handler404
from django.contrib.auth.views import LogoutView

from vacancies.views import MainView, VacanciesView,\
     SpecializationView, CompanyView, VacancyView,\
     MySignupView, VacanciesSendView, MyCompanyView,\
     MyVacanciesView, MyCompanyVacancyView, MyLoginView

# handler404 = custom_handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('vacancies/', VacanciesView.as_view()),
    path('vacancies/cat/<str:specialty>', SpecializationView.as_view()),
    path('companies/<int:id>', CompanyView.as_view()),
    path('vacancies/<int:id>', VacancyView.as_view()),
    path('vacancies/<vacancy_id>/send', VacanciesSendView.as_view()),
    path('mycompany', MyCompanyView.as_view(), name='my_company'),
    path('mycompany/vacancies', MyVacanciesView.as_view()),
    path('mycompany/vacancies/<vacancy_id>', MyCompanyVacancyView.as_view()),
    path('login', MyLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', MySignupView.as_view(), name='register'),
    # path('vacancies/<int:id>', MySignupView.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

LOGIN_REDIRECT_URL = '/'
