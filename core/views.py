from django.shortcuts import redirect, render, get_object_or_404
from core.models import Cohort
from datetime import date
from django import forms

# Create your views here.

# Five Big Views

# - list many models
def cohort_list(request):
    cohorts = Cohort.objects.all()
    return render(request, "core/cohort_list.html", {"cohorts": cohorts})


# - show one model
def cohort_detail(request, pk):
    cohort = get_object_or_404(Cohort, pk=pk)
    return render(request, "core/cohort_detail.html", {"cohort": cohort})


# - show one model
def cohort_by_graduation_date(request, year, month, day):
    graduation_date = date(year, month, day)
    cohort = get_object_or_404(Cohort, graduation_date=graduation_date)
    return render(request, "core/cohort_detail.html", {"cohort": cohort})


class CohortForm(forms.ModelForm):
    class Meta:
        model = Cohort
        fields = ["name", "graduation_date"]


# - create a model
def cohort_create(request):
    if request.method == "GET":
        form = CohortForm()
    else:
        form = CohortForm(data=request.POST)
        if form.is_valid():
            cohort = form.save()
            return redirect("cohort-detail", pk=cohort.pk)

    return render(request, "core/cohort_create.html", {"form": form})


# - update a model
def cohort_update(request, pk):
    cohort = get_object_or_404(Cohort, pk=pk)

    if request.method == "GET":
        form = CohortForm(instance=cohort)
    else:
        form = CohortForm(instance=cohort, data=request.POST)
        if form.is_valid():
            cohort = form.save()
            return redirect("cohort-detail", pk=cohort.pk)

    return render(request, "core/cohort_update.html", {"cohort": cohort, "form": form})


# - delete a model
def cohort_delete(request, pk):
    cohort = get_object_or_404(Cohort, pk=pk)

    if request.method == "POST":
        cohort.delete()
        return redirect("cohort-list")

    return render(request, "core/cohort_delete.html", {"cohort": cohort})
