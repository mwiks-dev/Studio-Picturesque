from django.test import TestCase
from .models import Pictures,Category,Location
from PIL import Image as Pictures

# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.montreal = Location(loc='Montreal')

    def test_location_instance(self):
        self.assertTrue(isinstance(self.montreal,Location))

    def test_save_location(self):
        self.montreal.save_location()
        places = Location.objects.all()
        self.assertTrue(len(places)> 0)

    def test_delete_location(self):
        self.montreal.save_location()
        places=Location.objects.all()
        self.assertEqual(len(places),1)
        self.montreal.delete_location()
        places = Location.objects.all()
        self.assertEqual(len(places), 0)

    def test_display_locations(self):
        self.montreal.save_location()
        self.assertEqual(len(Location.display_all_locations()),1)

    def test_update_location(self):
        self.montreal.save_location()
        self.montreal.update_location(self.montreal.id,'bot')
        update = Location.objects.get(loc = "bot")
        self.assertTrue(update.loc, 'bot')

class CategoryTestClass(TestCase):
    def setUp(self):
        self.rare = Category(name="rare")

    def test_save_category(self):
        self.rare.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

    def test_delete_category(self):
        self.rare.save_category()
        categories= Category.objects.all()
        self.assertEqual(len(categories),1)
        self.rare.delete_category()
        categories=Category.objects.all()
        self.assertEqual(len(categories),0)

    def test_update_category(self):
        self.rare.save_category()
        self.rare.update_category(self.rare.id,'bot')
        update = Category.objects.get(name = "bot")
        self.assertTrue(update.name, 'bot')

    def test_display_categories(self):
        self.rare.save_category()
        self.assertEqual(len(Category.display_all_categories()),1)


# class PicturesTestClass(TestCase):

#     def setUp(self):
#         """
#         Create a pic for testing
#         """
#         Pictures.objects.create(
#             name="Test Image",
#             description="Test Description",
#             location=Location.objects.create(loc="Test Location"),
#             category=Category.objects.create(name="Test Category"),
#             pub_date=None
#         )

#     def test_pic_name(self):
#         """
#         Test that the pic name is correct
#         """
#         pic = Pictures.objects.get(name="Test Image")
#         self.assertEqual(pic.name, "Test Image")

#     def test_pic_description(self):
#         """
#         Test that the pic description is correct
#         """
#         pic = Pictures.objects.get(name="Test Image")
#         self.assertEqual(pic.description, "Test Description")

#     def test_pic_location(self):
#         """
#         Test that the image location is correct
#         """
#         pic = Pictures.objects.get(name="Test Image")
#         self.assertEqual(pic.location.loc, "Test Location")

#     def test_pic_category(self):
#         """
#         Test that the image category is correct
#         """
#         pic = Pictures.objects.get(name="Test Image")
#         self.assertEqual(pic.category.name, "Test Category")


# class CategoryTestClass(TestCase):

#     def setUp(self):
#         """
#         Create a category for testing
#         """
#         Category.objects.create(name="Test Category")

#     def test_category_name(self):
#         """
#         Test that the category name is correct
#         """
#         category = Category.objects.get(name="Test Category")
#         self.assertEqual(category.name, "Test Category")

#     def test_category_str(self):
#         """
#         Test that the category string representation is correct
#         """
#         category = Category.objects.get(name="Test Category")
#         self.assertEqual(str(category), "Test Category")

# class LocationTestCase(TestCase):

#     def setUp(self):
#         """
#         Create a location for testing
#         """
#         Location.objects.create(loc="Test Location")

#     def test_location_loc(self):
#         """
#         Test that the location name is correct
#         """
#         location = Location.objects.get(loc="Test Location")
#         self.assertEqual(location.loc, "Test Location")

#     def test_location_str(self):
#         """
#         Test that the location string representation is correct
#         """
#         location = Location.objects.get(loc="Test Location")
#         self.assertEqual(str(location), "Test Location")