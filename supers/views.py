from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Super
from .serializers import SuperSerializer

@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        supers = Super.objects.all()
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
   
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def super_type_detail(request):
    type_param = Super.objects.all()
    custom_response_dictionary = {}

    if type_param == 'heroes':
        records = Super.objects.filter(super__type='1')
        serializer = SuperSerializer(records, data=request.data)
        print(type_param)
        return Response(serializer.data)

    elif type_param == 'villians':
        records = Super.objects.filter(super__type='2')
        serializer = SuperSerializer(records, data=request.data)
        print(type_param)
        return Response(serializer.data)
    
    else:
        records = Super.objects.all()
        serializer = SuperSerializer(records)
        return Response(serializer.data, status=status.HTTP_200_OK)
