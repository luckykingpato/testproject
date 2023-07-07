from django.http import HttpResponse

# Create your views here.
def homePageview(request):
    return HttpResponse("<h1>Hello, World")