from django.utils.deprecation import MiddlewareMixin


class CORSMiddleware(MiddlewareMixin):
    """跨域"""
    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = "content-type"
        return response