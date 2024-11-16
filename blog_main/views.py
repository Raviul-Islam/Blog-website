from django.http import HttpResponse

def home(request):
    return HttpResponse("Education for Nation")