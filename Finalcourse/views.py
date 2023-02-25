from django.http import HttpResponse

def salute(request):

    return HttpResponse ("hello world!")