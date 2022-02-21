from rest_framework.decorators import api_view
from rest_framework.response import Response

import super_types
from .models import SuperTypes
from .serializers import SuperTypesSerializer


@api_view(['GET'])
def super_types_list(request):
    super_types = SuperTypes.objects.all()
    serializer = SuperTypesSerializer(super_types, many=True)
    
    return Response(serializer.data)