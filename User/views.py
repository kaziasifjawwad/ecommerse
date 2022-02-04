
# Create your views here.
from Car.CarSerializer import CarSerializer
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from .models import *
from .userserializer import *

@api_view(['GET','POST'])
def createUser(request):
    if request.method=='GET':
        data = User.objects.all()
        serialized = UserSerializer(instance=data,many=True)
        return Response(serialized.data,status.HTTP_200_OK)
    elif request.method=='POST':
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status.HTTP_200_OK)
        else:
            return Response(serializers.errors,status.HTTP_400_BAD_REQUEST)


# @api_view(['PUT'])
# def updateUser(request):


@api_view(['PUT'])
def addFevMovie(request,userId,carId):
    try:
        user = User.objects.get(pk=userId)
        car = Car.objects.get(pk=carId)
        user.favouriteCar.add(car)
        print(user)
        user.save()
        serializers = UserSerializer(instance=user)
        return Response(serializers.data,status.HTTP_200_OK)
    except Car.DoesNotExist:
        return Response({"message": "No car with this id"},status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({"message": "No user with this id"}, status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def removeFevMovie(request,userId,carId):
    try:
        user = User.objects.get(pk=userId)
        car = Car.objects.get(pk=carId)
        user.favouriteCar.remove(car)
        if user.favouriteCar.count()==0:
            return Response({"Message":"No car exists"},status.HTTP_400_BAD_REQUEST)
        print(user)
        user.save()
        serializers = UserSerializer(instance=user)
        return Response(serializers.data,status.HTTP_200_OK)
    except Car.DoesNotExist:
        return Response({"message": "No car with this id"},status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({"message": "No user with this id"}, status.HTTP_400_BAD_REQUEST)


class SearchFevCar(ListAPIView):
    # queryset = self.kwargs['']
    serializer_class = CarSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        print(User.objects.get(pk=id).favouriteCar)
        return User.objects.get(pk=id).favouriteCar

    # pagination_class = PageN
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']

#
class SearchCarByRange(ListAPIView):
    serializer_class = CarSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields=['price']

    #get customed queryset
    def get_queryset(self):
        #path variables should be get from kwardgs
        start = self.kwargs['start']
        end = self.kwargs['end']
        return Car.objects.filter(price__range=(start,end))


class SearchByComplexQuery(ListAPIView):
    serializer_class = CarSerializer
    def get_queryset(self):
        name = self.kwargs['name']
        brand = self.kwargs['brand']
        #__iexact will get data without checking upper or lower character
        return Car.objects.filter(Q(name__iexact=name)&Q(brand__iexact=brand))







