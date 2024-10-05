from django.shortcuts import render


posts = [
    {
        "author": "alice",
        "date_posted": "October 5th, 2024",
        "title": "Lorem Ipsum",
        "content": "content"
    },
    {
        "author": "bob",
        "date_posted": "September 5th, 2024",
        "title": "Lorem Ipsum",
        "content": "content"
    }
]
# Create your views here.
def home(request):
    context = {"posts": posts, "title": "Home"}
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html")