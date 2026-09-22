from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import serializers
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
import datetime
import os

from main.models import Experience, Skill
from main.forms import ExperienceForm, SkillForm


# Registration
def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Sayyid Aqil Kusuma",
        "form": form,
    }
    return render(request, "register.html", context)

# Login
def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)
    next_value = request.GET.get("next", "main:show_main")

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        next_value = request.POST.get("next", "main:show_main")
        response = redirect(next_value)
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response


    context = {
        "name": "Sayyid Aqil Kusuma",
        "form": form,
        "next": next_value
    }
    return render(request, "login.html", context)

# Logout
def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

# Main
def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Sayyid Aqil Kusuma",
        "npm": "2506596331",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            """A 3rd semester CS student at Universitas Indonesia. Aspiring to be a game developer.
            Planning to graduate with minimal GPA of 3.00 within 4 years of study period (or less)."""
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)

# Experience
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

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ExperienceForm(request.POST or None)

    if (request.method == "POST" 
        and form.is_valid() 
        and os.getenv("PASSWORD") == form.cleaned_data["password"]):
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

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

# Skill
def show_skill(request):
    json_response = get_skill_json(request)
    
    skills = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    skills = [skill.object for skill in skills]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Sayyid Aqil Kusuma",
        "skill_list": skills,
        "title_query": title_query,
    }
    return render(request, "skill.html", context)

@login_required(login_url="/login/")
def create_skill(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = SkillForm(request.POST or None, request.FILES or None)

    if (request.method == "POST" 
        and form.is_valid() 
        and os.getenv("PASSWORD") == form.cleaned_data["password"]):
        form.save()
        messages.success(request, "Skill baru berhasil ditambahkan!")
        return redirect("main:show_skill")

    context = {
        "name": "Sayyid Aqil Kusuma",
        "form": form,
    }
    return render(request, "skill_form.html", context)

def get_skill_json(request):
    title_query = request.GET.get("title", "").strip()
    skill = Skill.objects.all()

    if title_query:
        skill = skill.filter(title__icontains=title_query)

    skill_json = serializers.serialize("json", skill)
    return HttpResponse(skill_json, content_type="application/json")

@login_required(login_url="/login/")
def edit_skill(request, skill_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    skill = get_object_or_404(Skill, pk=skill_id)
    form = SkillForm(request.POST or None, request.FILES or None, instance=skill)

    if (request.method == "POST" 
        and form.is_valid() 
        and os.getenv("PASSWORD") == form.cleaned_data["password"]):
        form.save()
        messages.success(request, "Skill baru berhasil ditambahkan!")
        return redirect("main:show_skill")

    context = {
        "name": "Sayyid Aqil Kusuma",
        "form": form,
        "skill_id": skill_id,
    }
    return render(request, "skill_form.html", context)

@login_required(login_url="/login/")
def delete_skill(request, skill_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    skill = get_object_or_404(Skill, pk=skill_id)

    if request.method == "POST":
        skill.delete()
        messages.success(request, "Skill berhasil dihapus!")

    return redirect("main:show_skill")