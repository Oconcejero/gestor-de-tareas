from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def index(request):
    mensaje = ''
    form = TareaForm()

    if request.method == 'POST':

        tarea_id = request.POST.get('tarea_id')

        # ELIMINAR
        if 'eliminar' in request.POST:
            tarea = Tarea.objects.get(id=tarea_id)
            tarea.delete()
            return redirect('index')

        # CHECKBOX (marcar o desmarcar)
        if tarea_id and 'completed' in request.POST:
            tarea = Tarea.objects.get(id=tarea_id)
            tarea.completed = True
            tarea.save()
            return redirect('index')

        if tarea_id and 'completed' not in request.POST:
            tarea = Tarea.objects.get(id=tarea_id)
            tarea.completed = False
            tarea.save()
            return redirect('index')

        # CREAR TAREA
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            mensaje = 'Error al crear la tarea'

    tareas = Tarea.objects.order_by('-dateLimit')
    return render(request, 'tareas/index.html', {'tareas': tareas, 'form': form, 'mensaje': mensaje})
