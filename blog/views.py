from django.shortcuts import render, get_object_or_404, redirect

from blog.forms import CommentForm
from main.models import Post


def blog(request):
    context = {
        'title': 'blog',
        'blog': 'active',
        'posts': Post.objects.all()[:9]
    }
    return render(request, 'blog.html', context)


def blog_details(request, key):
    blog = get_object_or_404(Post, pk=key)
    if request.method == "POST":
        print('hello world ')
        form = CommentForm(request.POST)
        for i in form:
            print('form is', i)
        if form.is_valid():
            form.save()
        return redirect('home')
    form = CommentForm()
    context = {
        'title': 'blog_detail',
        'form': form,
        'blog': 'active',
        'one_blog': blog,
    }

    return render(request, 'blog-details.html', context)
