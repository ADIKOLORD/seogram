from django.shortcuts import render

from main.models import Post


def main_page(request):
    context = {
        'title': 'Home',
        'posts': Post.objects.all()[:3],
        'ind': 'active',

    }

    return render(request, 'index.html', context)
