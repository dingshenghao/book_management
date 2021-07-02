from rest_framework import serializers
import oss2

from admins.models import Book


endpoint = 'https://oss-cn-beijing.aliyuncs.com'

bucket = oss2.Bucket(auth, endpoint, 'dsh-book-management')

# 这个是上传图片后阿里云返回的uri需要拼接下面这个url才可以访问，根据自己情况去写这步
base_file_url = 'https://dsh-book-management.oss-cn-beijing.aliyuncs.com/'


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


class AddBookSerializer(serializers.ModelSerializer):
    file = serializers.FileField(label='图书封面')

    class Meta:
        model = Book
        fields = ['id', 'name', 'category_id', 'product', 'principal', 'book_index', 'ISBN', 'file']

    def create(self, validated_data):
        file = validated_data['file']
        result = upload_file_to_oss(file)
        del validated_data['file']
        book = Book(**validated_data)
        book.img = result
        book.save()
        return book


class EditBookSerializer(serializers.ModelSerializer):
    file = serializers.CharField(label='图书封面', write_only=True, max_length=1024)

    class Meta:
        model = Book
        fields = ['id', 'name', 'category_id', 'product', 'principal', 'file', 'book_index', 'ISBN', 'img']

    def update(self, instance, validated_data):
        del validated_data['file']
        super(EditBookSerializer, self).update(instance, validated_data)
        return instance


class EditBookFileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(label='图书封面', write_only=True, max_length=1024)

    class Meta:
        model = Book
        fields = ['id', 'name', 'category_id', 'product', 'principal', 'file', 'book_index', 'ISBN', 'img']

    def update(self, instance, validated_data):
        file = validated_data.pop('file')
        result = upload_file_to_oss(file)
        validated_data['img'] = result
        super(EditBookFileSerializer, self).update(instance, validated_data)
        return instance
