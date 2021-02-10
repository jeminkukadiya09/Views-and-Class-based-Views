from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

# @api_view()
# def hello_world(request):
# 	return Response({'msg' : 'Hello World'})
class StudentAPI(APIView):
	def get(self, request,id=None, format=None):


		if id is not None:
			stu = Student.objects.get(id=id)
			serializer = StudentSerializer(stu)
			return Response(serializer.data)
		stu = Student.objects.all()
		serializer = StudentSerializer(stu, many=True)
		return Response(serializer.data)


	def post(self, request, id=None, format=None):

		serializer = StudentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg' : 'data Create !!'}, status=status.HTTP_201_CREATED  )
		return Response('serializer.errors')


	def put(self, request,id=None, format=None):
		stu = Student.objects.get(id=id)
		serializer = StudentSerializer(stu, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg' : 'complate data updataed'})
			return Response(serializer.errors)

	def patch(self, request, id=None, format=None):
		stu = Student.objects.get(id=id)
		serializer = StudentSerializer(stu, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg' : 'data updataed'})
			return Response(serializer.errors)

	def delete(self, request, id=None,format=None):
		stu = Student.objects.get(id=id)
		stu.delete()
		return Response({'msg' : 'data delete'})









# @api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# def student_api(request, id=None):
# 	if request.method == 'GET':

# 		if id is not None:
# 			stu = Student.objects.get(id=id)
# 			serializer = StudentSerializer(stu)
# 			return Response(serializer.data)
# 		stu = Student.objects.all()
# 		serializer = StudentSerializer(stu, many=True)
# 		return Response(serializer.data)


		
# 	if request.method == 'POST':
# 		serializer = StudentSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response({'msg' : 'data Create !!'}, status=status.HTTP_201_CREATED  )
# 		return Response('serializer.errors')


# 	if request.method == 'PUT':
# 		stu = Student.objects.get(id=id)
# 		serializer = StudentSerializer(stu, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response({'msg' : 'complate data updataed'})
# 			return Response(serializer.errors)

# 	if request.method == 'PATCH':
# 		stu = Student.objects.get(id=id)
# 		serializer = StudentSerializer(stu, data=request.data, partial=True)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response({'msg' : 'data updataed'})
# 			return Response(serializer.errors)


# 	if request.method == 'DELETE':
# 		stu = Student.objects.get(id=id)
# 		stu.delete()
# 		return Response({'msg' : 'data delete'})

		
# 			