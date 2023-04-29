from django.test import TestCase


from django.contrib.auth import get_user_model
from dashboard.models import Category
from django.urls import reverse
from django.http import request


User = get_user_model()


class CategoryTests(TestCase):
    def setUp(self) -> None:
        self.author = User.objects.create_user(
        username = 'muslimov',
        email="ash_shishan@gmail.com",  
        password="admin.admin",
        )

    #     self.category = Category.objects.create(
    #         name = "games",
    #         author = User  
    #     )

    # def test_category_str(self):
    #          self.assertEqual(str(self.category), self.category.name)

    # def test_category_content(self):
    #     self.assertEqual(f"{self.category.name}", "games")
    #     self.assertEqual(f"{self.category.author}", "")

    def test_category_view(self):
            response = self.client.get(reverse("home"))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "index.html")
            self.assertContains(response, "index")
