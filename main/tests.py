from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience
from main.models import Skill


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Game Development",
            description="Mencoba membuat game dengan menggunakan Godot V4.4.1.",
            category="freelance",
        )

        self.skill = Skill.objects.create(
            title="Java",
            description="Experienced at programming using Java, Java library, \
                and Java OOP implementation at an intermediate level.",
            image="static/img/Java.png",
            image_source="https://techicons.dev/icons/java"
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Game Development")
        self.assertEqual(self.experience.category, "freelance")
        self.assertTrue(self.experience.is_ongoing)

    def test_completed_experience(self):
        self.assertTrue(self.experience.is_ongoing)

        self.experience.ended_at = timezone.now()
        self.experience.save()

        self.assertFalse(self.experience.is_ongoing)

    def test_skill_model(self):
        self.assertEqual(str(self.skill), "Java")
        self.assertEqual(self.skill.image, "static/img/Java.png")
        self.assertEqual(self.skill.image_source, "https://techicons.dev/icons/java")