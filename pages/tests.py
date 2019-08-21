from django.test import SimpleTestCase

class simpeTests(SimpleTestCase):
    def get_home_page_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def get_about_page_status(self):
        response = self.client.get('about/')
        self.assertEqual(response.status_code, 200)

# Create your tests here.
