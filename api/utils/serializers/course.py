from rest_framework import serializers

from api import models


class CourseListSerializer(serializers.ModelSerializer):
    """课程列表序列化类"""
    course_type = serializers.CharField(source="get_course_type_display")
    level = serializers.CharField(source="get_level_display")
    status = serializers.CharField(source="get_status_display")
    sub_category = serializers.CharField(source="sub_category.name")
    degree_course = serializers.SerializerMethodField()

    def get_degree_course(self, obj):
        if obj.degree_course:
            degree_course = obj.degree_course
            return degree_course.name

    class Meta:
        model = models.Course
        fields = [
            "id",
            "name",
            "course_img",
            "course_type",
            "brief",
            "level",
            "pub_date",
            "period",
            "order",
            "attachment_path",
            "status",
            "template_id",
            "sub_category",
            "degree_course"
        ]


class CourseDetailSerializer(serializers.ModelSerializer):
    """课程详细序列化类"""
    course = serializers.CharField(source="course.name")
    recommend_courses = serializers.SerializerMethodField()
    teacher = serializers.SerializerMethodField()

    def get_recommend_courses(self, obj):
        recommend_courses = obj.recommend_courses.all()
        return [{"id": item.id, "name": item.name} for item in recommend_courses]

    def get_teacher(self, obj):
        teacher = obj.teacher.all()
        return [{"id": item.id, "name": item.name} for item in teacher]

    class Meta:
        model = models.CourseDetail
        fields = [
            "id",
            "course",
            "hours",
            "course_slogon",
            "video_brief_link",
            "why_study",
            "what_to_study_brief",
            "career_improvement",
            "prerequisite",
            "course",
            "recommend_courses",
            "teacher"
        ]
