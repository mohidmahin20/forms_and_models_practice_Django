from django.shortcuts import render
from .forms import ExampleForm, ExampleForm2

# Create your views here.


def one(request):
    form = ExampleForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "practiceOne.html", {"form": form})


def two(request):
    form = ExampleForm2(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "practiceTwo.html", {"form": form})