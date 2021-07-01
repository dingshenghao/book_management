from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

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
