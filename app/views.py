from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
# Se agregó Docente
from .models import Curso, Docente
# Create your views here.
def home(request):
    cursosListados = Curso.objects.all()
    # Se agregó la línea de abajo para Docente
    docentesListados = Docente.objects.all()
    data = {
        'titulo': 'Gestion de Cursos Avanzados',
        'cursos': cursosListados,
        # Se agregó para docente
        'docentes': docentesListados
    }
    return render(request, "gestionCursos.html", data)
class CursoListView(ListView):
    model = Curso
    template_name = 'gestionCursos.html'
    def get_queryset(self):
        return Curso.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gestion de Cursos Avanzados'
        return context

def registrar_curso(request):
    if request.method == 'POST':
        nombre = request.POST.get('txtNombre')
        creditos = request.POST.get('numCreditos')
        docente_id = request.POST.get('docente')  # Docente seleccionado
        nuevo_docente = request.POST.get('nuevoDocente')  # Nuevo docente a agregar

        if nuevo_docente:  # Si se ingresó un nuevo docente
            docente = Docente.objects.create(nombre=nuevo_docente)  # Crear nuevo docente
        else:  # Verifica si hay un docente_id
            docente = Docente.objects.get(id=docente_id)

        # Crear el curso con los valores proporcionados
        curso = Curso.objects.create(nombre=nombre, creditos=creditos, docente=docente)
    return redirect('/')

def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect('/')


def edicion_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    docentes = Docente.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('txtNombre')
        creditos = request.POST.get('numCreditos')
        docente_id = request.POST.get('docente')
        nuevo_docente = request.POST.get('nuevoDocente')
        if nuevo_docente:  # Si el campo 'nuevoDocente' no está vacío, se crea un nuevo docente
            docente = Docente.objects.create(nombre=nuevo_docente)
        else:
            docente = Docente.objects.get(id=docente_id)
        # Actualizar el curso con los nuevos valores
        curso.nombre = nombre
        curso.creditos = creditos
        curso.docente = docente  # Asignar el docente (nuevo o existente)
        curso.save()
        return redirect('gestionCursos')  # Redirigir a la vista que lista los cursos
    data = {
        'titulo': 'Edición de Curso',
        'curso': curso,
        'docentes': docentes,
    }
    return render(request, "edicionCurso.html", data)
def editar_curso(request):
    id = int(request.POST['id'])
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
    docente_id = request.POST['docente']

    curso = Curso.objects.get(id=id)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.docente = Docente.objects.get(id=docente_id)
    curso.save()
    return redirect('/')


def eliminar_docente(request, id):
    docente = Docente.objects.get(id=id)
    docente.delete()  # Los cursos asociados se eliminan automáticamente
    return redirect('/')
