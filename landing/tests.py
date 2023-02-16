from django.test import TestCase
from .models import project
from django.core.files.uploadedfile import SimpleUploadedFile

class ProjectModelTest(TestCase):
    def setUp(self):
        self.project = project.objects.create(
            title="Test Project",
            description="This is a test project",
            url="https://example.com"
        )

    def test_title(self):
        self.assertEqual(self.project.title, "Test Project")

    def test_description(self):
        self.assertEqual(self.project.description, "This is a test project")

    def test_url(self):
        self.assertEqual(self.project.url, "https://example.com")

    def test_image_upload(self):
        image = SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")
        self.project.image = image
        self.project.save()
        self.assertEqual(self.project.image.name, "assets/images/test.jpg")