from django.db.transaction import atomic
from django.forms import ModelForm, CharField
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from c_viewer.models import Country, Profile


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError("Country name not capitalized")


def region_validator(value):
    correct_regions = ['NORTHERN AMERICA', 'OCEANIA', 'EASTERN EUROPE', 'WESTERN EUROPE', 'LATIN AMER. & CARIB',
                       'BALTICS', 'ASIA (EX. NEAR EAST)', 'SUB-SAHARAN AFRICA', 'NEAR EAST', 'C.W. OF IND. STATES',
                       'NORTHERN AFRICA']
    if value not in correct_regions:
        raise ValidationError(f"You have to provide one of the {correct_regions}")


class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = '__all__'

    name = CharField(validators=[capitalized_validator])
    region = CharField(validators=[region_validator])

    def clean_gdp_per_capita(self):
        return self.cleaned_data['gdp']/self.cleaned_data['population']


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    @atomic
    def save(self, commit=True):
        self.instance.is_active = False
        user = super().save(commit)
        if commit:
            Profile.objects.create(user=user, countries_count=0)
        return user
