from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required



from .models import Article, Author
from .forms import RegisterForm, ArticleForm
from .filters import ArticleFilter

# Create your views here.
User = get_user_model()

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('articles')
                
    return render(request, 'sign_in.html')

def sign_out(request):
    logout(request)
    return redirect(sign_in)

 
# views.py



# Create your views here.
def register(response):
    if response.method == "POST":
	    form = RegisterForm(response.POST)
	    if form.is_valid():
	        form.save()

	    return redirect("/")
    else:
	    form = RegisterForm()

    return render(response, "register.html", {"form":form})






def articles(request):
    article_filter = ArticleFilter(request.GET, queryset=Article.objects.all())
    articles = Article.objects.all()
    return render(
        request,
        "articles.html",
        {"articles": articles}
    )

# def articles(request):
#     article_filter = ArticleFilter(request.GET, queryset=Article.objects.filter(is_active=True))
#     return render(
#         request,
#         "articles.html",
#         {"article_filter": article_filter}
#     )


def article(request, id):
    article = Article.objects.get(id = id)
    article.views += 1
    article.save()
    
    return render(
        request,
        "article.html",
        {"article": article}
    )

def authors(request):
    authors = Author.objects.all()
    return render(
        request,
        "authors.html",
        {"authors": authors}
    )

def author_page(request, pk):
    author = Author.objects.get(id=pk)
    return render(
        request,
        "author.html",
        {"author":author, "user":author.user}
    )

def about(request):
    return render(
        request,
        "about.html"
    )

def edit_article(request, pk):
    article = Article.objects.get(id = pk)

    if request.method == "POST":
        article.title = request.POST.get("title")
        article.text = request.POST.get("text")
        article.save()
        return redirect(article_page, pk)
    return render(request, "update.html", {"article": article})


@login_required(login_url='/sign-in/')
def add_article(request):
    if request.method == "GET":
        return render(request, "add_article.html")
    elif request.method == "POST":
        form = request.POST 
        title = form.get("title")
        text = form.get("text")

        # new_article = Article(title = title, text = text)
        new_article = Article()
        new_article.title = title
        new_article.text = text

        user = request.user
        if not Author.objects.filter(user=user).exists():
            author = Author(user=user, nickname=user.username)
            author.save()
            new_article.author = author
        

        new_article.save()
        return redirect(article, new_article.pk)


def article_form(request):
    context = {}

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
        return redirect(article_page, article.id)
    else:
        form = ArticleForm()

    form = ArticleForm()
    context['form'] = form

    return render(request, 'form.html', context)


def search(request):
    word = request.GET.get("word")
    articles = Article.objects.filter(Q(title__icontains=word) | Q(text__icontains=word)) #LIKE|  is_active=True

    return render(request, "articles.html", {"articles":articles})


def is_author(user):
    if not user.is_authenticated:
        return False
    return Author.objects.filter(user=user).exists()

@user_passes_test(is_author)
def delete_article(request, id):
    myarticle = Article.objects.get(pk=id)
    myarticle.delete()
    return HttpResponse("is deleted")

def top(request):
    articles = Article.objects.order_by("-views")[:3]
    return render(request, "top.html", {"articles":articles})




