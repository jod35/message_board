from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):

    def set_up(self):
        Post.objects.create(title='title',content='content')

    def test_text_content(self):
        post=Post.objects.get(id=7)
        expected_postname=f"{post.title}"

        self.assertEqual(expected_postname,'title')


