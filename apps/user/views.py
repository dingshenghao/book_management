from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import jwt_decode_handler
from rest_framework import status
from rest_framework import authentication, permissions
from rest_framework import generics

from book_management.utils.AuthToken import UserAuthToken
from book_management.utils.throttle import VisitThrottle
from user.models import User
from user.serializers import LoginSerializer, RegisterSerializer, ImgSerializer, EditUserSerializer


class LoginView(APIView):
    authentication_classes = []  # 规避全局token认证
    permission_classes = []  # 规避全局权限认证
    # 默认的节流是登录用户（10/m）,AuthView不需要登录，这里用匿名用户的节流（3/m）
    throttle_classes = [VisitThrottle, ]

    def post(self, request):
        query_dict = request.data.copy()
        serializer = LoginSerializer(data=query_dict)
        if serializer.is_valid():
            return Response({'status': 200, 'message': '登录成功', 'data': serializer.validate(query_dict)})
        else:
            return Response({'status': 400, 'message': serializer.errors['non_field_errors'][0]})


class RegisterView(APIView):
    authentication_classes = []  # 规避全局token认证
    permission_classes = []  # 规避全局权限认证
    # 默认的节流是登录用户（10/m）,AuthView不需要登录，这里用匿名用户的节流（3/m）
    throttle_classes = [VisitThrottle, ]

    def post(self, request):
        query_dict = request.data
        serializer = RegisterSerializer(data=query_dict)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'message': '注册成功', 'data': serializer.data})
        else:
            return Response({'status': 400, 'message': serializer.errors['username'][0], 'data': None})


class UploadIconView(APIView):
    authentication_classes = [UserAuthToken, ]  # 不设置全局认证，单独设置认证
    permission_classes = []  # 规避全局权限认证

    def put(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = ImgSerializer(instance=user, data=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'message': '上传成功', 'data': user.img})
        else:
            return Response({'status': 400, 'message': serializer.errors['non_field_errors'][0]})


class EditUserView(APIView):
    authentication_classes = [UserAuthToken, ]
    permission_classes = []  # 规避全局权限认证

    def put(self, request, pk):
        # 获取请求头中的 token数据
        http_token = request.META.get('HTTP_TOKEN')
        # 对 token解密，获取用户信息
        user = jwt_decode_handler(http_token)

        user = User.objects.get(id=pk)
        serializer = EditUserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'message': '修改成功', 'data': None})
        else:
            return Response({'status': 400, 'message': serializer.errors['username'][0], 'data': None})
