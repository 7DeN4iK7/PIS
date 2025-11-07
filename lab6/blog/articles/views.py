from django.shortcuts import render, redirect
from django.http import Http404

# Create your views here.
from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404
    
def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            if form["text"] and form["title"]:
                if Article.objects.filter(title=form["title"]).exists():
                    form['errors'] = "Статья с таким названием уже существует"
                    return render(request, 'create_post.html', {'form': form})
                article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                return redirect('get_article', article_id=article.id)
            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html', {})
    else:
        return redirect('auth')
    
def register(request):
    if request.method == "POST":
            form = {
                'login': request.POST["login"], 'password': request.POST["password"], 'email': request.POST['email']
            }
            if form["login"] and form["password"] and form['email']:
                try:
                    User.objects.get(username=form['login'])
                    form['errors'] = u"Такой пользователь уже есть"
                    return render(request, 'register.html', {'form': form})
                except User.DoesNotExist:
                    User.objects.create_user(form['login'], form['email'], form['password'])
                    return redirect('archive')

            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'register.html', {'form': form})
    else:
            return render(request, 'register.html', {})

def auth(request):
    if request.method == "POST":
            form = {
                'login': request.POST["login"], 'password': request.POST["password"]
            }
            if form["login"] and form["password"]:
                    user = authenticate(username=form['login'], password=form['password'])
                    if user is None:
                        form['errors'] = u"Невернные данные для входа"
                        return render(request, 'auth.html', {'form': form})
                    else:
                        login(request, user)
                        return redirect('archive')
            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'auth.html', {'form': form})
    else:
            return render(request, 'auth.html', {})


