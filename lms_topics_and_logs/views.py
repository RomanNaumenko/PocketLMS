from django.shortcuts import render
from .models import Topic, Entry


# Create your views here.
def index(request):
    return render(request, 'home.html', {})


def show_topics(request):
    topics = Topic.objects.all()
    return render(request, 'topics.html', {'topics': topics})

