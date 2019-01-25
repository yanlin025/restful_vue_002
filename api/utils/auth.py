from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from api import models


class TokenAuth(BaseAuthentication):
    """token认证"""
    def authenticate(self, request):
        token = request.query_params.get("token")
        token_obj = models.UserAuthToken.objects.filter(token=token).first()
        if not token:
            raise AuthenticationFailed({"code": 1001, "error": "登录后才能访问"})
        return (token_obj.user, token_obj)

    def authenticate_header(self, request):
        pass
