from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Skill
from main.forms import ExperienceForm


def show_main(request):
    context = {
        "name": "Sayyid Aqil Kusuma",
        "npm": "2506596331",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            """A 3rd semester CS student at Universitas Indonesia. Aspiring to be a game developer.
            Planning to graduate with minimal GPA of 3.00 within 4 years of study period (or less)."""
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Sayyid Aqil Kusuma",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_skill(request):
    context = {
        "name": "Sayyid Aqil Kusuma",
        "skill_list": Skill.objects.all(),
    }
    return render(request, "skill.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Sayyid Aqil Kusuma",
        "form": form,
    }
    return render(request, "experience_form.html", context)