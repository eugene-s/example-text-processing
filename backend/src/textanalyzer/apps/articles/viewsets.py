from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.get_queryset()

    @action(detail=True)
    def process(self, request, pk):
        return Response()
