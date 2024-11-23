from django.test import TestCase
from django.http import HttpRequest  
#from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
    def test_home_response(self): 
        response = self.client.get('/polls/')
        html = response.content.decode("utf8")  
        self.assertIn("Hello, world", html)  
        self.assertTrue(html.startswith("<html>"))  
        self.assertTrue(html.endswith("</html>"))

#    def test_uses_home_template(self): 
#        response = self.client.get('/')
#        self.assertTemplateUsed(response, 'home.html')

