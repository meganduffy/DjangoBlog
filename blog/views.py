from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


# Create your views here.
def post_list(request):
    """
    Create a view that will return a list of Posts that were
    published prior to 'now' and render them to the 'blogposts.html'
    template
    """
    # Django allows us to append strings to table fields that act as boolean operators
    # __lte = les-than-or-equal-to
    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')  # - indicates descending order
    return render(request, "blogposts.html", {'posts': posts})


def post_detail(request, id):
    """
    Create a view that returns a single Post object based on the
    post id and render it to the 'postdetail.html' template or return
    a 404 error if the post is not found
    """
    post = get_object_or_404(Post, pk=id)
    post.views += 1  # clock up the number of post views
    post.save()
    return render(request, "postdetail.html", {'post': post})


def top_five(request):
    """
    Create a view that will return a list of top 5 Posts sorted by views
    """
    most_pop = Post.objects.filter(published_date__lte=timezone.now()
                                   ).order_by('-views')[:5]
    return render(request, "top_five.html", {'most_pop': most_pop})
