from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.utils import json

from .models import *
from .serializers import StudentModelSerializer


class Create(CreateAPIView):

    permission_classes = []
    def post(self, request, *args, **kwargs):
        try:
            data= json.loads(request.body)

            student_model = StudentModel()
            if 'full_name' not in data or data['full_name']=='':
                return Response('Please Enter Your Name',status=400)
            if 'class_info' not  in data or data['class_info']=='':
                return Response('Please Enter class info',status=400)
            if 'section' not  in data or data['section']=='':
                return Response('Please Enter section',status=400)

            student_model.full_name=data['full_name']
            student_model.class_info=data['class_info']
            student_model.section=data['section']
            student_model.save()

            result = {}
            result['status'] = HTTP_200_OK
            result['message'] = "success"
            return Response(result)

        except Exception as ex:
            result = {}
            result['status'] = HTTP_400_BAD_REQUEST
            result['message'] = str(ex)
            return Response(result)

class RetrieveAll(ListAPIView):

    permission_classes = []

    def get(self, request):

        data = StudentModel.objects.filter().all()
        data = StudentModelSerializer(data, many=True).data

        return Response(data)


class Retrieve(ListAPIView):

    permission_classes = []
    def get(self, request, full_name):
        student_data = StudentModel.objects.filter(full_name=full_name).first()
        student_data = StudentModelSerializer(student_data).data
        return Response(student_data)

class Edit(CreateAPIView):
    permission_classes = []
    def put(self, request, full_name):
        try:
            data= json.loads(request.body)
            result = {}
            if 'full_name' not in data or data['full_name']=='':
                return Response('Please Enter Your Name',status=400)
            if 'class_info' not  in data or data['class_info']=='':
                return Response('Please Enter class info',status=400)
            if 'section' not  in data or data['section']=='':
                return Response('Please Enter section',status=400)

            student = StudentModel.objects.filter(full_name=full_name).first()

            if not student:
                result['message'] = "No Data found"
                return Response(result, status=HTTP_400_BAD_REQUEST)

            else:
                student.full_name = data['full_name']
                student.class_info = data['class_info']
                student.section = data['section']
                student.save()

                result['message'] = "Success."
                result['status'] = HTTP_200_OK
                return Response(result)

        except Exception as ex:
            result = {}
            result['message'] = str(ex)
            return Response(result)

class Delete(CreateAPIView):
    permission_classes = []

    def delete(self, request, full_name):
        try:
            student = StudentModel.objects.filter(full_name=full_name).first()
            result = {}
            if not student:
                result['message'] = "No Data found"
                return Response(result, status=HTTP_400_BAD_REQUEST)

            student.delete()
            result['status'] = HTTP_200_OK
            result['message'] = "Deleted"
            return Response(result)

        except Exception as ex:
            result = {}
            result['message'] = str(ex)
            return Response(result)