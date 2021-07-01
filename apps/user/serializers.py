import re
import uuid

import oss2
from django.contrib.auth.hashers import check_password
from rest_framework import serializers
from rest_framework.utils.serializer_helpers import ReturnDict

from user.models import User

auth = oss2.Auth('LTAI5t78wRZmQuUtVUQLYkt5', 'X1mctiwjRl74Yg4dpHsnHTmbPi2iWY')

endpoint = 'https://oss-cn-beijing.aliyuncs.com'

bucket = oss2.Bucket(auth, endpoint, 'dsh-book-management')

# 这个是上传图片后阿里云返回的uri需要拼接下面这个url才可以访问，根据自己情况去写这步
base_file_url = 'https://dsh-book-management.oss-cn-beijing.aliyuncs.com/'


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(label='用户名', max_length=20)
    password = serializers.CharField(label='密码', max_length=128)

    def validate(self, attrs):
        username = attrs['username']
        password = attrs['password']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError('用户不存在')
        if check_password(password, user.password):
            attrs['id'] = user.id
            attrs['img'] = user.img
            attrs['role'] = user.role
            attrs['email'] = user.email
            attrs['desc'] = user.desc
            del attrs['password']
            return attrs
        else:
            raise serializers.ValidationError('用户名或密码错误')


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(label='确认密码', write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'password2', 'email']
        extra_kwargs = {
            'username': {
                'min_length': 3,
                'max_length': 20,
                'error_messages': {  # 自定义校验出错的错误信息
                    'min_length': '仅允许3-20个字符的⽤户名',
                    'max_length': '仅允许3-20个字符的⽤户名',
                }
            },
            'password': {
                'write_only': True,  # 进行设置True以确保在更新或创建实例时可以使用该字段，但在序列化表示形式时不包括该字段。
                'min_length': 3,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许3-20个字符的密码',
                    'max_length': '仅允许3-20个字符的密码',
                }
            }
        }

    def validata_email(self, value):
        """校验邮箱"""
        if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', value):
            return value
        else:
            raise serializers.ValidationError("邮箱格式错误")

    def validata_username(self, value):
        """校验用户名"""
        count = User.objects.filter(username=value).count()
        if count > 0:
            raise serializers.ValidationError("用户名已存在")
        return value

    def create(self, validated_data):
        del validated_data['password2']
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


def upload_file_to_oss(file):
    """
     ！ 上传单张图片
    :param file:
    :return:
    """
    name = file.name
    # 生成文件名
    base_fil_name = str(name)
    # 生成外网访问的文件路径
    file_name = base_file_url + base_fil_name
    # 这个是阿里提供的SDK方法 bucket是调用的4.1中配置的变量名
    res = bucket.put_object(base_fil_name, file, progress_callback=None)
    # 如果上传状态是200 代表成功 返回文件外网访问路径
    # 下面代码根据自己的需求写
    if res.status == 200:
        return file_name
    else:
        return False


class ImgSerializer(serializers.Serializer):
    # username = serializers.CharField(label='用户名', max_length=20)
    img = serializers.FileField(label='用户头像')

    def update(self, instance, validated_data):
        file = validated_data['img']
        result = upload_file_to_oss(file)
        instance.img = result
        instance.save()
        instance.url = result
        return instance


class EditUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'desc']

    def validata_username(self, value):
        count = User.objects.filter(username=value).count()
        if count > 0:
            raise serializers.ValidationError("用户名已存在，请重新修改")
        else:
            return value

    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        instance.email = validated_data['email']
        instance.desc = validated_data.get('desc', '')
        instance.save()
        return instance
