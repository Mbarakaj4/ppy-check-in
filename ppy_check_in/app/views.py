from django.shortcuts import render
from .models import Estudiante

# Create a view that renders index.html
def index(request):
  return render(request, 'index.html')

def submit(request):
  if request.method == 'POST':
    # Process form data
    try:
        cedula_identidad = request.POST['cedula_identidad']
        instance = Estudiante(
        ci = cedula_identidad
        )
        instance.save()
    except Exception:
        # key doesn't exist
        print('Key does not exist')

    # Save to database etc
  return render(request, 'registrado.html') 
