from django.test import TestCase
from my_passwords.models import Category
from django.contrib.auth.models import User 

class MyCategoryTest(TestCase):
    def test_category_print(self):
        c = Category.objects.get(id=1)
        self.assertEqual(c.__str__(), c.name)

    def test_category_create(self):
        # Ensure it is possible to add a new category 
        u = User.objects.get(id=1)
        old_length = len(Category.objects.all())
        Category.objects.create(name="Test Category", user=u)
        self.assertEqual(old_length + 1, len(Category.objects.all()))

# class YourTestClass(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         print("setUpTestData: Run once to set up non-modified data for all class methods.")
#         pass

#     def setUp(self):
#         print("setUp: Run once for every test method to setup clean data.")
#         pass

#     def test_false_is_false(self):
#         print("Method: test_false_is_false.")
#         self.assertFalse(False)

#     def test_false_is_true(self):
#         print("Method: test_false_is_true.")
#         self.assertTrue(False)

#     def test_one_plus_one_equals_two(self):
#         print("Method: test_one_plus_one_equals_two.")
#         self.assertEqual(1 + 1, 2)
