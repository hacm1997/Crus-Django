from apps.CrudApp.models import Servicio
from django import forms
from django.forms import fields

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = (
            'fecha','hora_atencion','hora_final_atencion','empresa','ciudad','asunto',
            'respuesta','fecha_solicitud',
        )

        widgets = {
            'fecha': forms.DateInput(
                attrs = {
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
            'hora_atencion': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'hora_final_atencion': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'empresa': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'ciudad': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'asunto': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'respuesta': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'fecha_solicitud': forms.DateInput(
                attrs = {
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
        }

class EditSolicitudForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = (
            'fecha','hora_atencion','hora_final_atencion','empresa','asunto',
            'respuesta','fecha_solicitud',
        )

        widgets = {
            'fecha': forms.DateInput(
                attrs = {
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
            'hora_atencion': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'hora_final_atencion': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'empresa': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'asunto': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'respuesta': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'fecha_solicitud': forms.DateInput(
                attrs = {
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
        }