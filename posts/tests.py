from django.test import TestCase
from .models import Post
from django.urls import reverse

class PostModelTest(TestCase):

    def set_up(self):
        Post.objects.create(title='title',content='content')

    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_postname=f"{post.title}"

        self.assertEqual(expected_postname,'title')


class HomePageViewTest(TestCase):
    def SetUp(self):
        Post.objects.create(title='another title',content='another content')
    
    def test_view_url_exists_at_proper_location(self):
        resp=self.client.get('/')
        self.assertEqual(resp.status_code,200)

    def test_view_by_url_name(self):
        resp=self.client.get(reverse('mess_home'))
        self.assertEqual(resp.status_code,200)

    def test_view_gets_correct_template(self):
        resp=self.client.get(reverse('mess_home'))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,'index.html')