from django.shortcuts import render
# Create your views here.
def hesa(request):
    return render(request, 'hello.html', {'message': 'Hello'})