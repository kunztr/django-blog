from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog, Comment
from django.template import loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils import timezone


def index(request):
    latest_blog_posts_list = Blog.objects.order_by('-posted')[:3]
    # template = loader.get_template('blog/index.html')
    context = {
        'latest_blog_posts_list': latest_blog_posts_list,
    }
    return render(request, 'blog/index.html', context)
    # return HttpResponse(template.render(context, request))
    # output = ', '.join([b.content for b in latest_blog_posts_list])
    # return HttpResponse(output)
    # return HttpResponse("Hello, world. You're at the polls index.")


def blog_archive(request):
    blog_posts_list = Blog.objects.order_by('-posted')
    # template = loader.get_template('blog/index.html')
    context = {
        'blog_posts_list': blog_posts_list,
    }
    return render(request, 'blog/blog_archive.html', context)


def blog_post(request, blog_id):
    blog_post = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog_post.html', {'blog_post': blog_post})
    # return HttpResponse("This is where you make a blog entry i guess")


def comment(request, blog_id):
    if request.method == 'POST':
        b = Blog.objects.get(id=blog_id)
        commenter = request.POST.get('new_comment_name')
        email = request.POST.get('new_comment_email')
        content = request.POST.get('new_comment_content')
        c = b.comment_set.create(commenter=commenter, email=email, content=content, posted=timezone.now())

        c.save()
        b.save()
    return HttpResponseRedirect(reverse('blog:blog_post', args=(blog_id,)))


def about(request):
    return render(request, 'blog/about.html')


def tips(request):
    return render(request, 'blog/tips.html')