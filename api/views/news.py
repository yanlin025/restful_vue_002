from django.db.models import F
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning

from api import models
from api.utils.serializers.news_serializer import NewsSerializer
from api.utils.auth import TokenAuth


class NewsView(ViewSetMixin, APIView):
    """深科技"""
    authentication_classes = [TokenAuth]
    # versioning_class = URLPathVersioning

    def list(self, request, *args, **kwargs):
        """文章列表"""
        # print(11, request.version)
        res = {"code": 1000, "data": None}
        try:
            news = models.Article.objects.all()
            ser = NewsSerializer(instance=news, many=True)
            res["data"] = ser.data
        except Exception as e:
            res["code"] = 1001
            res["error"] = e
        return Response(res)

    def retrieve(self, request, *args, **kwargs):
        """文章详情"""
        res = {"code": 1000, "data": None}
        try:
            pk = kwargs.get("pk")
            news = models.Article.objects.filter(pk=pk)
            ser = NewsSerializer(instance=news.first())
            res["data"] = ser.data
            news.update(view_num=F("view_num") + 1)
        except Exception as e:
            res["code"] = 1001
            res["error"] = e
        return Response(res)


class CollectView(APIView):
    """文章收藏"""

    def post(self, request, *args, **kwargs):
        res = {"code": 1000, "error": ""}
        id = request.data.get("id")
        token = request.data.get("token")

        user_obj = models.Account.objects.filter(userauthtoken__token=token).first()
        article_obj = models.Article.objects.filter(id=id)
        obj = article_obj.first().collect.filter(account=user_obj).first()
        if not obj:
            models.Collection.objects.create(account=user_obj, content_object=article_obj.first())
            article_obj.update(collect_num=F("collect_num") + 1)
        else:
            obj.delete()
            article_obj.update(collect_num=F("collect_num") - 1)
            res["code"] = 1001
            res["status"] = False
        return Response(res)


class AgreeView(APIView):
    """文章点赞"""

    def post(self, request, *args, **kwargs):
        res = {"code": 1000, "error": ""}
        id = request.data.get("id")
        token = request.data.get("token")
        user_obj = models.Account.objects.filter(userauthtoken__token=token).first()
        article_obj = models.Article.objects.filter(id=id)
        obj = article_obj.first().agree.filter(account=user_obj).first()
        if not obj:
            models.Agree.objects.create(account=user_obj, content_object=article_obj.first())
            article_obj.update(agree_num=F("agree_num") + 1)
        else:
            obj.delete()
            article_obj.update(agree_num=F("agree_num") - 1)
            res["code"] = 1001
            res["status"] = False
        return Response(res)


class CommentView(APIView):
    """文章评论"""

    def post(self, request, *args, **kwargs):
        res = {"code": 1000, "error": ""}
        id = request.data.get("id")
        token = request.data.get("token")
        comment_content = request.data.get("commentContent")

        user_obj = models.Account.objects.filter(userauthtoken__token=token).first()
        article_obj = models.Article.objects.filter(id=id)
        models.Comment.objects.create(account_id=user_obj.id, content_object=article_obj.first(),
                                      content=comment_content)
        article_obj.update(comment_num=F("comment_num") + 1)
        return Response(res)
