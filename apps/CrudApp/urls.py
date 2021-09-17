from apps.CrudApp.views import EliminarSolicitud, ListarSolicitudes, CreateSolicitud, ListServices, EditarSolicitud
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ListarSolicitudes, name='list-soli'),
    path('addsolicitud', CreateSolicitud, name='addsolicitud'),
    path('listaservicios/json/read/crud/app', ListServices.as_view(), name='listaservicios'),
    path('actualizar_solicitud/<int:pk>/', EditarSolicitud.as_view(), name='updatesolici'),
    path('eliminar_solicitud/<int:pk>/', EliminarSolicitud.as_view(), name='deletesolici'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)