from .models import License
from .serializers import LicenseSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny



@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def license_list(request, format=None):
    
    if request.method == 'POST':
        serializer = LicenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:    
            return Response(serializer.errors, status=status.HTTP_403_BAD_REQUEST)
            
    else: 
        licenses = License.objects.all()
        serializer = LicenseSerializer(licenses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def license_detail(request, id, format=None):
    
    try:
         license_var = License.objects.get(pk=id)
    except License.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
     
    if request.method == 'PUT':
        serializer = LicenseSerializer(license_var, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:    
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        license_var.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    else:
        serializer = LicenseSerializer(license_var)
        return Response(serializer.data, status=status.HTTP_200_OK)