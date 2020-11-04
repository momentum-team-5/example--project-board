from django import forms
from core.models import Cohort


class CohortForm(forms.ModelForm):
    class Meta:
        model = Cohort
        fields = ["name", "graduation_date"]
