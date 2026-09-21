from django.urls import path

from main.views import (
    register,
    login_user,
    logout_user,
    show_main,
    show_experience,
    create_experience, 
    get_experience_json,
    delete_experience,
    show_skill,
    create_skill,
    get_skill_json,
    edit_skill,
    delete_skill
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("api/skill/", get_skill_json, name="get_skill_json"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:experience_id>/delete/",delete_experience,name="delete_experience"),
    path("skill/", show_skill, name="show_skill"),
    path("skill/add/", create_skill, name="create_skill"),
    path("skill/<uuid:skill_id>/edit/", edit_skill ,name="edit_skill"),
    path("skill/<uuid:skill_id>/delete/", delete_skill ,name="delete_skill"),
]