"""
自定义节流器
    如果继承 BaseThrottle  需要重写 allow_request（）、 wait（） 两个方法
"""
from rest_framework.throttling import BaseThrottle, SimpleRateThrottle
import time

VISIT_RECORD = {}  # 保存访问记录


class VisitThrottle(BaseThrottle):
    """60s内只能访问三次"""

    def __init__(self):
        self.history = None  # 初始化访问记录

    def allow_request(self, request, view):
        remote_addr = self.get_ident(request)  # 获取用户ip
        ctime = time.time()
        if remote_addr not in VISIT_RECORD:
            VISIT_RECORD[remote_addr] = [ctime, ]
            return True  # True表示可以访问
        # 获取当前ip的历史访问记录
        history = VISIT_RECORD.get(remote_addr)
        # 初始化访问记录
        self.history = history

        # 如果有历史访问记录，并且最早一次的访问记录离当前时间超过60s，就删除最早的那个访问记录，
        # 只要为True，就一直循环删除最早的一次访问记录
        while history and history[-1] < ctime - 60:
            history.pop()
        # 如果访问记录不超过三次，就把当前的访问记录插到第一个位置（pop删除最后一个）
        if len(history) < 3:
            history.insert(0, ctime)
            return True

    def wait(self):
        """还需要等多久才能访问"""
        ctime = time.time()
        return 60 - (ctime - self.history[-1])


"""
SimpleRateThrottle类实现节流
"""


class VisitThrottle1(SimpleRateThrottle):
    """匿名用户60s只能访问三次（根据ip）"""
    scope = 'throttle'  # 这里面的值，自己随便定义，settings里面根据这个值配置throttle

    def get_cache_key(self, request, view):
        # 通过ip 限制节流
        return self.get_ident(request)


class UserThrottle(SimpleRateThrottle):
    """登录用户60s可以访问10次"""
    scope = 'userThrottle'  # 这里面的值，自己随便定义，settings里面根据这个值配置userThrottle

    def get_cache_key(self, request, view):
        return request.user.id
