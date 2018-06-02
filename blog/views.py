from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from .models import Blog


def index(request):
	posts = list(Blog.objects.all())
	posts.reverse()

	blog_posts = posts[:5]

	return render_to_response('blog/index.html', {'posts': blog_posts,
													'links': posts,})

def view_post(request, slug):
	blog_links = list(Blog.objects.all())
	blog_links.reverse()

	return render_to_response('blog/view_post.html', {
		'post': get_object_or_404(Blog, slug=slug),
		'links': blog_links,
	})
