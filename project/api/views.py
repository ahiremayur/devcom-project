from urllib import response
from  rest_framework.response import Response
from  rest_framework.decorators import api_view
from base.models import take
from .serializers import takeSerializer
 
@api_view(['GET'])
def getdata(request):
    items = take.objects.all()
    serializer = takeSerializer(items, many=True)
    return Response (serializer.data)

@api_view(['POST'])
def additem(request):
    serializer = takeSerializer(data=request.data)  
    if serializer.is_valid():
        serializer.save()
    return response(serializer.data)    

