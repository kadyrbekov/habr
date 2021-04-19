from django.test import TestCase
from django.urls import reverse
from core.models import Article
from .factories import ArticleFactory


class HomepageTestCase(TestCase):

    def setUp(self):
        self.url = reverse('articles')


    def test_homepage_loads_success(self):
       
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Habr')
    
    def test_homepage_with_articles_success(self):
        n = 3
        for i in range(n):
            # article = Article()
            # article.title = f'Test Title {i}'
            # article.text = f'Bla bla bla text {i}'
            # article.save()

            article = ArticleFactory()
            

        article.is_active = False
        article.save()

        
        response = self.client.get(self.url)
        self.assertIn('articles', response.context)
        articles = Article.objects.filter(is_active=True)
        self.assertEqual(articles.count(), n - 1)

        for article in articles:
            self.assertContains(response, article.title)
            self.assertContains(response, article.text)
