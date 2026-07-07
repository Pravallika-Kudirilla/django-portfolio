from django.test import TestCase

class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        print("STATUS CODE IS:", response.status_code)
        if response.status_code == 500:
            print(response.content.decode('utf-8'))
