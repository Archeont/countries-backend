from django.shortcuts import render
from django.views.generic import ListView, CreateView, View, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .models import Country, Profile
from .form import SignUpForm, CountryForm


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser



class RichCountries(ListView):
    template_name = 'countries_list.html'

    def get_queryset(self):
        return Country.objects.filter(gdp__gte=250000000000).all()


class RichCountriesAndPeople(ListView):
    template_name = 'countries_list.html'

    def get_queryset(self):
        return Country.objects.filter(gdp__gte=250000000000).filter(gdp_per_capita__gte=25000).all()


class CCountries(ListView):
    template_name = 'countries_list.html'

    def get_queryset(self):
        return Country.objects.filter(name__startswith='C').all()


class UsersWatched(View):
    def get(self, request):
        return render(request, template_name='users_watched.html',
                      context={'object_list': Profile.objects.all()})


class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')


class CountriesView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = 'c_viewer.view_country'

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        profile.countries_count += 1
        profile.save()
        return render(request, template_name='countries_list.html',
                      context={'object_list': Country.objects.all()})


class CountriesCreate(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = CountryForm
    success_url = reverse_lazy('create_country')
    permission_required = 'c_viewer.add_country'


class CountriesUpdate(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Country
    form_class = CountryForm
    success_url = reverse_lazy('root')
    permission_required = 'c_viewer.change_country'


class CountriesDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'delete.html'
    model = Country
    success_url = reverse_lazy('root')
    permission_required = 'c_viewer.delete_country'
