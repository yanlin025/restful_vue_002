import uuid
from rest_framework.views import APIView
from rest_framework.response import Response

from api import models


class LoginView(APIView):
    """登录处理"""
    def post(self, request, *args, **kwargs):
        res = {"code": 1000, "error": ""}
        user = request.data.get("user")
        pwd = request.data.get("pwd")
        user_obj = models.Account.objects.filter(username=user, password=pwd).first()
        if not user_obj:
            res["code"] = 1001
            res["error"] = "用户名或密码错误"
        else:
            token = str(uuid.uuid4())
            models.UserAuthToken.objects.update_or_create(user=user_obj, defaults={"token": token})
            res["token"] = token
        return Response(res)
