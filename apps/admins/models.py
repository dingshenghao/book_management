from django.db import models

from book_management.utils.BaseModel import BaseModel


class Book(BaseModel):
    name = models.CharField(verbose_name='书名', max_length=20, null=False)
    category_id = models.CharField(verbose_name='分类id', max_length=20, null=False),
    product = models.CharField(verbose_name='出版社', max_length=20, null=False)
    principal = models.CharField(verbose_name='负责人', max_length=20, null=False)
    book_index = models.CharField(verbose_name='图书索引', max_length=30, null=False)
    ISBN = models.CharField(verbose_name='ISBN号', max_length=40, null=False)
    img = models.CharField(verbose_name='图书封面路径', max_length=1024, null=False)

    class Meta:
        db_table = 'book'
        verbose_name = '图书'


class Category(BaseModel):
    name = models.CharField(verbose_name='分类名称', max_length=10, unique=True)

    class Meta:
        db_table = 'category'
        verbose_name = '图书分类'
