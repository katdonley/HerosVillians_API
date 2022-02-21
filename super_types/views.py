from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SuperTypes
from .serializers import SuperTypesSerializer


@api_view(['GET'])
def super_types_list(request):
    super_type = SuperTypes.objects.all()
    serializer = SuperTypesSerializer(super_type, many=True)
    return Response(serializer.data)

        