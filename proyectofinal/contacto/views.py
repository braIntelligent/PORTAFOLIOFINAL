from django.shortcuts import render, redirect
from .forms import ContactoForm

# Create your views here.

def contact_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mensaje_enviado')
    else:
        form = ContactoForm()
    return render(request, 'contacto/formulario.html', {'form': form})

def mensaje_enviado(request):
    return render(request, 'contacto/mensaje_enviado.html')