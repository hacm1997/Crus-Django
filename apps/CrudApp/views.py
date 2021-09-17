from apps.CrudApp.forms import SolicitudForm, EditSolicitudForm
from apps.CrudApp.models import Servicio
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView, ListView
from django.contrib import messages
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core.serializers import serialize
from django.urls import reverse_lazy

# Create your views here.
def ListarSolicitudes(request):
    servi = Servicio.objects.all()
    context = {'services': servi}

    return render(request, 'index.html', context)

#JSON PARA LISTADO DE SERVICIOS
class ListServices(ListView):
    model = Servicio
    template_name = "listado-services-json.html"
    #context_object_name = "datescal"

    def get_queryset(self):
        return self.model.objects.all()

    def get(self,request,*args,**kwargs):
        if request.is_ajax():
            
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
            
        else:
            return render(request, self.template_name)

def CreateSolicitud(request):
    if request.is_ajax():
        form = SolicitudForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'¡Agregado con éxito!')
            #response = JsonResponse
            return redirect('list-soli')
        else:
            form = SolicitudForm
    return render(request, 'create_solicitud.html', {'form': form})

class EditarSolicitud(UpdateView):
    model = Servicio
    form_class = EditSolicitudForm
    template_name = 'editar_solicitud.html'
    #success_url = reverse_lazy('list-soli')

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                messages.success(request, f'¡Solicitud editada con éxito!')
                return redirect('list-soli')
            else:
                messages.success(request, f'¡Error! No se pudo editar la solicitud')
                return redirect('list-soli')
        else:
            return redirect('list-soli')

class EliminarSolicitud(DeleteView):
    model = Servicio
    template_name = 'eliminar_solicitud.html'

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            serv = self.get_object()
            serv.delete()

            return redirect('list-soli')
        else:
            return redirect('list-soli')