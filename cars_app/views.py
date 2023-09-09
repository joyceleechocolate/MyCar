from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *


class CarView(APIView):
    def get(self, request, pk=None):
        if pk:
            car = Car.objects.get(pk=pk)
            if car:
                serializer = CarSerializer(car)
                return Response(serializer.data)
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            cars = Car.objects.all()
            serializer = CarSerializer(cars, many=True)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
        except Car.DoesNotExist:    
            return Response(status=status.HTTP_404_NOT_FOUND)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CarModelView(APIView):

    def get(self, request, pk=None):
        if pk:
            car_model = CarModel.objects.get(pk=pk)
            if car_model:
                serializer = CarModelSerializer(car_model)
                return Response(serializer.data)
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            car_models = CarModel.objects.all()
            serializer = CarModelSerializer(car_models, many=True)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = CarModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CarModelSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            car_model = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:    
            return Response(status=status.HTTP_404_NOT_FOUND)
        car_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AppUserView(APIView):
    def get(self, request, pk=None):
        if pk:
            app_user = AppUser.objects.get(pk=pk)
            if app_user:
                serializer = AppUserSerializer(app_user)
                return Response(serializer.data)
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            app_user = AppUser.objects.all()
            serializer = AppUserSerializer(app_user, many=True)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = AppUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            app_user = AppUser.objects.get(pk=pk)
        except AppUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AppUserSerializer(app_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            app_user = AppUser.objects.get(pk=pk)
        except AppUser.DoesNotExist:    
            return Response(status=status.HTTP_404_NOT_FOUND)
        app_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserProfileView(APIView):
    def get(self, request, pk=None):
        if pk:
            user_prof = UserProfile.objects.get(pk=pk)
            if user_prof:
                serializer = UserSerializer(user_prof)
                return Response(serializer.data)
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            user_prof = UserProfile.objects.all()
            serializer = UserSerializer(user_prof, many=True)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            user_prof = UserProfile.objects.get(pk=pk)
        except UserProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user_prof, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            user_prof = UserProfile.objects.get(pk=pk)
        except UserProfile.DoesNotExist:    
            return Response(status=status.HTTP_404_NOT_FOUND)
        user_prof.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class AdView(APIView):
    def get(self, request, pk=None):
        if pk:
            ad = Advertisement.objects.get(pk=pk)
            if ad:
                serializer = AddSerializer(ad)
                return Response(serializer.data)
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            ad = Advertisement.objects.all()
            serializer = AddSerializer(ad, many=True)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = AddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            ad = Advertisement.objects.get(pk=pk)
        except Advertisement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AddSerializer(ad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            ad = Advertisement.objects.get(pk=pk)
        except Advertisement.DoesNotExist:    
            return Response(status=status.HTTP_404_NOT_FOUND)
        ad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)