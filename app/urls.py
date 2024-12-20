from django.urls import path
from app.views import CursoListView, registrar_curso, eliminar_curso, edicion_curso, editar_curso, eliminar_docente


urlpatterns = [
    path('', CursoListView.as_view(), name='gestion_cursos'),
    path('registrarCurso/', registrar_curso),
    path('eliminacionCurso/<int:id>', eliminar_curso),
    path('edicionCurso/<int:id>', edicion_curso),
    path('editarCurso/', editar_curso),

    path('eliminarDocente/<int:id>', eliminar_docente),  # Nueva ruta para eliminar docente
#    path('', views.home, name='gestionCursos'),  # Nombre correcto de la vista
#    path('gestionCursos/', views.gestion_cursos, name='gestionCursos'),  # Asegúrate de que esta línea exista

]
