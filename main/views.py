from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from dotenv import dotenv_values

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
    json_response = get_experience_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Sayyid Aqil Kusuma",
        "experience_list": experiences,
        "title_query": title_query,
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

    if (request.method == "POST" 
        and form.is_valid() 
        and dotenv_values().get("PASSWORD") == form.cleaned_data["password"]):
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Sayyid Aqil Kusuma",
        "form": form,
    }
    return render(request, "experience_form.html", context)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experience = Experience.objects.all()

    if title_query:
        experience = experience.filter(title__icontains=title_query)

    experience_json = serializers.serialize("json", experience)
    return HttpResponse(experience_json, content_type="application/json")

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")