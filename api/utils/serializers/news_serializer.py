from rest_framework import serializers

from api import models


class NewsSerializer(serializers.ModelSerializer):
    """深科技序列化类"""
    status = serializers.CharField(source="get_status_display")
    position = serializers.CharField(source="get_position_display")
    source = serializers.CharField(source="source.name")

    class Meta:
        model = models.Article
        fields = [
            "id",
            "title",
            "article_type",
            "brief",
            "head_img",
            "content",
            "pub_date",
            "offline_date",
            "status",
            "vid",
            "comment_num",
            "agree_num",
            "view_num",
            "collect_num",
            "date",
            "position",
            "source",
        ]


