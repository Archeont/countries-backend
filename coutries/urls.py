"""coutries URL Configuration

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
from django.urls import path, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView

from c_viewer.models import Country
from c_viewer.form import CountryForm
from c_viewer.views import RichCountries, RichCountriesAndPeople, CCountries, SignUpView, \
    CountriesView, UsersWatched, CountriesCreate, CountriesUpdate, CountriesDelete

admin.site.register(Country)

urlpatterns = [
    path('', CountriesView.as_view(), name='root'),
    path('admin/', admin.site.urls),
    path('country/create', CountriesCreate.as_view(), name='create_country'),
    path('country/update/<pk>', CountriesUpdate.as_view()),
    path('country/delete/<pk>', CountriesDelete.as_view()),
    path('rich_countries', RichCountries.as_view()),
    path('rich_countries_and_people', RichCountriesAndPeople.as_view()),
    path('ccountries', CCountries.as_view()),
    path('accounts/login/', LoginView.as_view(template_name='form.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/sign_up', SignUpView.as_view(), name='sign_up'),
    path('users_watched', UsersWatched.as_view())
]
