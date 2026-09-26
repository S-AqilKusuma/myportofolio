from django.forms import ModelForm, TextInput, Textarea, URLInput, FileInput, Select, DateTimeInput

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