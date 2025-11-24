from django.shortcuts import render

# Create your views here.
def index(request):
    nombre = request.GET.get('nombre', 'Juan Luis')
    return render(request, 'home/index.html', {"nombre": nombre})