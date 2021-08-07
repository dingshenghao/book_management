"""
自定义权限
"""

from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    message = "必须是管理员才能执行此操作"  # 重写返回的提示信息

    def has_permission(self, request, view):
        if request.user.role == '1':  # 说明是管理员用户
            return True
        return False  # 返回False 页面也显示我们重写的message属性
