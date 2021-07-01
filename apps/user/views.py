from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView

from user.models import User
from user.serializers import LoginSerializer, RegisterSerializer, ImgSerializer, EditUserSerializer


class LoginView(APIView):

    def post(self, request):
        query_dict = request.data.copy()
        serializer = LoginSerializer(data=query_dict)
        if serializer.is_valid():
            return Response({'status': 200, 'message': '登录成功', 'data': serializer.validate(query_dict)})
        else:
            return Response({'status': 400, 'message': serializer.errors['non_field_errors'][0]})


class RegisterView(APIView):

    def post(self, request):
        query_dict = request.data
        serializer = RegisterSerializer(data=query_dict)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'message': '注册成功', 'data': serializer.data})
        else:
            return Response({'status': 400, 'message': serializer.errors['username'][0], 'data': None})


class UploadIconView(APIView):

    def put(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = ImgSerializer(instance=user, data=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'message': '上传成功', 'data': user.img})
        else:
            return Response({'status': 400, 'message': serializer.errors['non_field_errors'][0]})


class EditUserView(APIView):

    def put(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = EditUserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'message': '修改成功', 'data': None})
        else:
            return Response({'status': 400, 'message': serializer.errors['username'][0], 'data': None})
