from django.shortcuts import render
from .models import Prestamo, Encargado, Estudiante

def lista_prestamos(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'ListaPrestamos.html', {'prestamo': prestamos})
