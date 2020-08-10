from rest_framework import serializers

from textanalyzer.apps.articles.models import Article


class ArticleSerializer(serializers.Serializers):
    class Meta:
        model = Article
        fields = "__all__"
