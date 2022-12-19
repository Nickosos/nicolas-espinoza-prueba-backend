from django.shortcuts import render, redirect
from Api_Proyecto.models import Inscritos
from Api_Proyecto.models import Institucion
from Api_Proyecto.forms import FormInscritos
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import InscritosSerializer
from .serializers import InstitucionSerializer
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listarincripcion(request):
    ins = Inscritos.objects.all()
    data = {'Inscritos': ins}
    return render(request, 'listarinscripcion.html', data)

def agregarinscripcion(request):
    form = FormInscritos()
    if request.method == 'POST':
        form = FormInscritos(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarinscripcion.html', data)

def eliminarinscripcion(request, id):
    ins = Inscritos.objects.get(id = id)
    ins.delete()
    return redirect('/listarinscripcion# modelo institucion')

def actualizainscripcion(request, id):
    ins = Inscritos.objects.get(id = id)
    form = FormInscritos(instance=ins)
    if request.method == 'POST':
        form = FormInscritos(request.POST, instance=ins)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'agregarinscripcion.html', data)

def verinscripcionesDb(request):
    inscripciones = Inscritos.objects.all()
    data = {'inscripciones' : list(inscripciones.values('id','nombre','telefono','fechainscripción','institucion','horainscripcion','estados','observacion'))}

    return JsonResponse(data)


#function

@api_view(['GET', 'POST'])
def inscripcion_list(request):
    if request.method == 'GET':
        inscripciones = Institucion.objects.all()
        serial = InstitucionSerializer(inscripciones, many=True)
        return Response(serial.data)
    
    if request.method == 'POST':
        serial = InstitucionSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def inscripcion_detalle(request, pk):
    try:
        inscripciones = Institucion.objects.get(id = pk)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InstitucionSerializer(inscripciones)
        return Response(serial.data)

    if request.method == 'PUT':
        serial = InstitucionSerializer(inscripciones, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        inscripciones.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#class base
class ListarInscripciones(APIView):

    def get(self, request):
        inscripciones = Inscritos.objects.all()
        serial = InscritosSerializer(inscripciones, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = InscritosSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DetalleInscripciones(APIView):

    def get_object(self, pk):
        try:
            return Inscritos.objects.get(pk=pk)
        except Inscritos.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        inscripciones = self.get_object(pk)
        serial = InscritosSerializer(inscripciones)
        return Response(serial.data)

    def put(self, request, pk):
        inscripciones = self.get_object(pk)
        serial = InscritosSerializer(inscripciones, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        inscripciones = self.get_object(pk)
        inscripciones.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







