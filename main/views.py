from django.shortcuts import render

from main.models import Experience


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