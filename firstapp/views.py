from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def lists(request):
    return render(request, 'welcome_students.html')
def Student(request):
    return HttpResponse(["<h1>Hi ladies!</h1>", "<p>Welcome to AkiraChix class.</p>"])
def create(request):
    pass
def details(request):
    pass
def update(request):
    pass
def delete(request):
    pass
