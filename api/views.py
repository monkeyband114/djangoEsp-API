from urllib import request
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators  import api_view
from . models import Espdata
from .serializer import EspSerializer
from django.db.models import IntegerField
from django.db.models.functions import Cast



@api_view(['GET'])
def getData(request):
    routes = [
        {
            'Endpoint':'/espdata/',
            'method':'/GET',
            'body': None,
            'description': 'returns the name and data number'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getData(request):
    esp = Espdata.objects.all()
    serialize = EspSerializer(esp, many=True)
    
    return Response(serialize.data)
    

@api_view(['POST'])
def espData(request):
    data = request.data
    esp = Espdata.objects.create(
        name=data['name']
    )
    serialize = EspSerializer(esp, many=False)
        
    return Response(serialize.data)