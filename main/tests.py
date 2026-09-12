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
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Game Development")
        self.assertEqual(self.experience.category, "freelance")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Freelance")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        self.assertContains(response, f'href="{reverse("main:show_skill")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")

    def test_skill_model(self):
        self.assertEqual(str(self.skill), "Java")
        self.assertEqual(self.skill.image, "static/img/Java.png")
        self.assertEqual(self.skill.image_source, "https://techicons.dev/icons/java")

    def test_skill_page(self):
        response = self.client.get(reverse("main:show_skill"))

        # Tes muncul tidaknya halaman
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skill.html")
        # Tes muncul tidaknya data skill
        self.assertContains(response, self.skill.title)
        self.assertContains(response, self.skill.description)
        self.assertContains(response, self.skill.image)
        self.assertContains(response, self.skill.image_source)
        # Tes Navbar
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    # Tes halaman jika skill masih kosong
    def test_empty_skill_page(self):
        Skill.objects.all().delete()
        response = self.client.get(reverse("main:show_skill"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")