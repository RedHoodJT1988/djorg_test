from django.shortcuts import render
from . import templates

# Create your views here.
def index(request):
    return render(request, 'bookmarks/index.html', context='bookmarks: Bookmark.objects.all()')