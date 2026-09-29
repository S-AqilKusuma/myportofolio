from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, Textarea, URLInput, FileInput, Select, DateTimeInput
from django.utils.html import strip_tags

from main.models import Experience, Skill

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "ended_at",
        ]

        labels = {
            "title": "Nama",
            "description": "Deskripsi",
            "category": "Kategori",
            "thumbnail": "URL Thumbnail",
            "ended_at": "Tanggal Selesai",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Masukan Nama Pengalaman",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Pengalamanmu",
                    "rows": 3,
                }
            ),
            "category": Select(),
            "thumbnail": URLInput(
                attrs={
                    "required": False,
                }
            ),
            "ended_at": DateTimeInput(
                attrs={
                    "required": False,
                }
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama pengalaman tidak boleh hanya berisi tag HTML.")
        return title

    def clean_description(self):
        description = strip_tags(self.cleaned_data["description"]).strip()
        if not description:
            raise ValidationError("Deskripsi pengalaman tidak boleh hanya berisi tag HTML.")
        return description

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = [
            "title",
            "description",
            "image",
            "image_source",
        ]

        labels = {
            "title": "Nama",
            "description": "Deskripsi",
            "image": "Logo",
            "image_source": "Sumber Logo",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Masukan Nama Skill",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Deskripsikan Skillmu",
                    "rows": 3,
                }
            ),
            "image": FileInput(
                attrs={
                    "required": False,
                }
            ),
            "image_source": URLInput(
                attrs={
                    "required": False,
                }
            ),
        }