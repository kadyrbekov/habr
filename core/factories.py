import factory
from .models import Article

class ArticleFactory(factory.django.Django):
    class Meta:
        model =Article
