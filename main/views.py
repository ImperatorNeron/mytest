from django.views.generic import ListView

from .models import TestModel


class TestView(ListView):
    model = TestModel
    template_name = "main/index.html"
    context_object_name = "tests"
