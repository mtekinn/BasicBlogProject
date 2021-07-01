from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .models import Article, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ArticleForms


def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, "articles.html", {"articles":articles})
    articles = Article.objects.all()

    return render(request, "articles.html", {"articles": articles})


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

@login_required
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {
        "articles": articles
    }
    return render(request, "dashboard.html", context=context)

@login_required(login_url="user:login")
def addarticle(request):
    form = ArticleForms(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Your article has been added")
        return redirect("article:dashboard")

    return render(request, "addarticle.html", {'form': form})


def details(request, id):
    # article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article, id=id)
    comments = article.comments.all()

    return render(request, "details.html", {'article': article, "comments":comments})


@login_required(login_url="user:login")
def updateArticle(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForms(request.POST or None, request.FILES or None, instance=article)
    
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, "You updated the article.")
        return redirect("article:dashboard")


    return render(request, "update.html", {"form": form})


@login_required(login_url="user:login")
def deleteArticle(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    messages.success(request, "You deleted the article")
    return redirect("article:dashboard")


def addComment(request, id):
    article = get_object_or_404(Article,id = id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author=comment_author, comment_content=comment_content)

        newComment.article = article

        newComment.save()
        
    return redirect(reverse("article:details", kwargs={"id":id}))
