from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from admins.models import Category, Book
from admins.serializers import AddBookSerializer, EditBookSerializer, EditBookFileSerializer
from user.models import User


class GetUsersView(APIView):

    def get(self, request):
        users = User.objects.filter(role=0, is_active=1)
        user_list = []
        for user_model in users:
            user = {
                'id': user_model.id,
                'username': user_model.username,
                'email': user_model.email,
                'date': str(user_model.date_joined).split(' ')[0]
            }
            user_list.append(user)
        return Response({'status': 200, 'message': 'success', 'data': user_list})


class DeleteUserView(DestroyAPIView):
    queryset = User.objects.filter()

    def destroy(self, request, *args, **kwargs):
        super(DeleteUserView, self).destroy(request, *args, **kwargs)
        return Response({'status': 200, 'message': '删除成功！'})

    def perform_destroy(self, instance):
        instance.is_active = 0
        instance.save()


class GetCategoryView(APIView):

    def get(self, request):
        category_models = Category.objects.all()
        category_list = []
        for category_model in category_models:
            category_list.append({
                'id': category_model.id,
                'name': category_model.name
            })
        return Response({'status': 200, 'message': 'success', 'data': category_list})


class AddBookView(APIView):

    def post(self, request):
        query_dict = request.data.dict().copy()
        serializer = AddBookSerializer(data=query_dict)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'message': '发布成功!'})
        else:
            return Response({'status': 400, 'message': '发布失败'})


class GetBooksView(APIView):

    def get(self, request):
        book_models = Book.objects.all()
        book_list = []
        for book_model in book_models:
            book_list.append({
                'id': book_model.id,
                'name': book_model.name,
                'product': book_model.product,
                'principal': book_model.principal,
                'category_id': book_model.category_id,
                'book_index': book_model.book_index,
                'ISBN': book_model.ISBN,
                'img': book_model.img,
                'create_time': str(book_model.create_time).split('.')[0]
            })
        return Response({'status': 200, 'message': 'success', 'data': book_list})


class EditBookView(APIView):

    def put(self, request, pk):
        query_dict = request.data.dict().copy()
        file = query_dict['file']
        book = Book.objects.get(id=pk)
        if file == 'None':
            serializer = EditBookSerializer(instance=book, data=query_dict)
        else:
            serializer = EditBookFileSerializer(instance=book, data=query_dict)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'message': '修改成功'})
        else:
            return Response({'status': 400, 'message': serializer.errors})


class DeleteBookView(DestroyAPIView):
    queryset = Book.objects.filter()

    def destroy(self, request, *args, **kwargs):
        super(DeleteBookView, self).destroy(request, *args, **kwargs)
        return Response({'status': '204', 'message': '删除成功'})
