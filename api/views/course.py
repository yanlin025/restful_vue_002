from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import Response

from api import models
from api.utils.serializers.course import CourseListSerializer, CourseDetailSerializer


class CourseView(ViewSetMixin, APIView):
    """课程"""
    def list(self, request, *args, **kwargs):
        """课程列表"""
        res = {"code": 1000, "data": None, "error": ""}
        try:
            course = models.Course.objects.all()
            ser = CourseListSerializer(instance=course, many=True)
            res["data"] = ser.data
        except Exception as e:
            res["code"] = 1001
            res["error"] = e
        return Response(res)

    def retrieve(self, request, *args, **kwargs):
        """课程详细"""
        res = {"code": 1000, "data": None, "error": ""}
        try:
            pk = kwargs.get("pk")
            course_obj = models.CourseDetail.objects.filter(id=pk).first()
            ser = CourseDetailSerializer(instance=course_obj, many=False)
            res["data"] = ser.data
        except Exception as e:
            res["code"] = 1001
            res["error"] = e
        return Response(res)
