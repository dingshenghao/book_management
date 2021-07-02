from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from admins.models import Category, Book, Borrows
from admins.serializers import AddBookSerializer, EditBookSerializer, EditBookFileSerializer, BorrowsSerializer, \
    BackBookSerializer, ReservationSerializer, AgreeReservationSerializer
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
                'category': Category.objects.get(id=book_model.category_id).name,
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


class BorrowBookView(APIView):

    def post(self, request):
        serializer = BorrowsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'message': '借书成功'})
        else:
            return Response({'status': 400, 'message': serializer.errors['non_field_errors'][0]})


class GetBorrowsBook(APIView):
    """获取借书列表"""

    def get(self, request):
        user_id = request.query_params['id']
        borrows = Borrows.objects.filter(user_id=user_id, status=0)
        book_ids = []
        for borrow in borrows:
            book_ids.append(borrow.book_id)

        book_models = Book.objects.all()
        book_list = []
        for book_model in book_models:
            if book_model.id not in book_ids:
                book_list.append({
                    'id': book_model.id,
                    'name': book_model.name,
                    'product': book_model.product,
                    'principal': book_model.principal,
                    'category_id': book_model.category_id,
                    'category': Category.objects.get(id=book_model.category_id).name,
                    'book_index': book_model.book_index,
                    'ISBN': book_model.ISBN,
                    'img': book_model.img,
                    'create_time': str(book_model.create_time).split('.')[0],
                    'book_status': 1 if Borrows.objects.filter(book_id=book_model.id, status=2).count() > 0 else 0
                })
        return Response({'status': 200, 'message': 'success', 'data': book_list})


class GetBorrowsBook1(APIView):
    """获取还书列表"""

    def get(self, request):
        user_id = request.query_params['id']
        borrows = Borrows.objects.filter(user_id=user_id, status=0)
        book_ids = []
        for borrow in borrows:
            book_ids.append(borrow.book_id)
        book_models = Book.objects.all()
        book_list = []
        for book_model in book_models:
            if book_model.id in book_ids:
                book_list.append({
                    'id': book_model.id,
                    'name': book_model.name,
                    'product': book_model.product,
                    'principal': book_model.principal,
                    'category_id': book_model.category_id,
                    'category': Category.objects.get(id=book_model.category_id).name,
                    'book_index': book_model.book_index,
                    'ISBN': book_model.ISBN,
                    'img': book_model.img,
                    'create_time': str(Borrows.objects.get(book_id=book_model.id).create_time).split('.')[0]
                })
        return Response({'status': 200, 'message': 'success', 'data': book_list})


class BackBookView(APIView):

    def put(self, request):
        user_id = request.data['user_id']
        book_id = request.data['book_id']
        try:
            borrows = Borrows.objects.get(book_id=book_id, user_id=user_id, status=0)
            serializer = BackBookSerializer(instance=borrows, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 200, 'message': '还书成功!'})
        except Borrows.DoesNotExist:
            return Response({'status': 400, 'message': '还书失败!'})


class ReservationBook(APIView):

    def post(self, request):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'message': '申请预约成功!'})
        else:
            return Response({'status': 400, 'message': serializer.errors['non_field_errors'][0]})


class UnReservationView(DestroyAPIView):

    def destroy(self, request, *args, **kwargs):
        instance = Borrows.objects.filter(book_id=request.data['book_id'], user_id=request.data['user_id'], status=2)
        self.perform_destroy(instance)
        return Response({'status': 204, 'message': '取消预约成功'})

    def perform_destroy(self, instance):
        instance.delete()


class GetHistoryView(APIView):

    def get(self, request, pk):
        borrows = Borrows.objects.filter(user_id=pk)
        book_list = []
        for borrow in borrows:
            book_model = Book.objects.get(id=borrow.book_id)
            book_list.append({
                'id': book_model.id,
                'name': book_model.name,
                'product': book_model.product,
                'principal': book_model.principal,
                'category_id': book_model.category_id,
                'category': Category.objects.get(id=book_model.category_id).name,
                'book_index': book_model.book_index,
                'ISBN': book_model.ISBN,
                'img': book_model.img,
                'create_time': str(borrow.create_time).split('.')[0],
                'book_status': borrow.status
            })
        return Response({'status': 200, 'message': 'success', 'data': book_list})


class GetReservationListView(APIView):

    def get(self, request):
        borrows = Borrows.objects.filter(status=2)
        book_list = []
        for borrow in borrows:
            book_model = Book.objects.get(id=borrow.book_id)
            user = User.objects.get(id=borrow.user_id, is_active=1)
            book_list.append({
                'id': borrow.id,
                'name': book_model.name,
                'username': user.username,
                'email': user.email,
                'create_time': str(borrow.create_time).split('.')[0],
            })
        return Response({'status': 200, 'message': 'success', 'data': book_list})


class AgreeReservationView(APIView):

    def put(self, request):
        borrow = Borrows.objects.get(id=request.data['borrow_id'], status=2)
        serializer = AgreeReservationSerializer(instance=borrow, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'message': '同意预约'})
        else:
            return Response({'status': 400, 'message': serializer.errors['non_field_errors'][0]})
