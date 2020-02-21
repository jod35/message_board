from django.views.generic import ListView
from .models import Post

class HomePageView(ListView):
    template_name='index.html'
    model=Post