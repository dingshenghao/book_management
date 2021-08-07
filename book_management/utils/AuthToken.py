"""
自定义token认证类
"""
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import NotAuthenticated
from rest_framework_jwt.authentication import jwt_decode_handler

from user.models import User


class UserAuthToken(BaseAuthentication):

    def authenticate(self, request):
        # 获取请求头中的 token数据
        http_token = request.META.get('HTTP_TOKEN')
        if http_token is None:
            raise NotAuthenticated('缺少token')
        # 对 token解密，获取用户信息
        user_model = jwt_decode_handler(http_token)
        user = User.objects.get(id=user_model['user_id'])
        return user, http_token
