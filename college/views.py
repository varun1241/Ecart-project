from django.shortcuts import render

# Create your views here.
from .models import College

from rest_framework.views import APIView

from .serializers import CollegeSerilizer

from rest_framework.response import Response

from rest_framework import status

class CollegeView(APIView):
    def get(self,request):

        college=College.objects.all()

        data=CollegeSerilizer(college,many=True)

        return  Response(data.data)
    
    def post(self, request, format=None):
        serializer =CollegeSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)





class CollegeUpadteView(APIView):
    def get(self,request,pk):

        print(pk,"pkvalue")
        college=College.objects.get(college_id=int(pk))
        print(college,"collegedata")

        data=CollegeSerilizer(college)

        return  Response(data.data)
    
    def put(self,request,pk):

        print(pk,"pkvalue")
        college=College.objects.get(college_id=int(pk))
        serializer =CollegeSerilizer(college,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

    def delete(self,request,pk):

        college=College.objects.get(college_id=int(pk))

        college.delete()

        return Response(status=status.HTTP_202_ACCEPTED)





    
    

