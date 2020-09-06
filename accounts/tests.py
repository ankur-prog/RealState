from django.test import TestCase


# Create your tests here.
class MyTest(TestCase):

    def normal_test(self):
        self.assertEqual("Ankur", "Ankur")
        print("ankur")
