from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Category, Donation
from decimal import Decimal


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_detail', pk=post.pk)


def post_list(request, category_slug=None):
    category = None
    posts = Post.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)
    return render(request, 'blog/post_list.html', {'posts': posts, 'category': category})


def donate_to_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        amount = Decimal(request.POST.get('amount'))


        return redirect('post_detail', pk=post.pk)

    return render(request, 'blog/donate.html', {'post': post})

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

