from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Post
from .forms import BlogForm, CommentForm
from slugify import slugify


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blog.html'


def post_detail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            messages.success(
                request, 'Successfully added comment!')
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


@login_required
def add_post(request):
    """ View for store owner to add post """
    if not request.user.is_superuser:
        messages.error(request,
                       'Oops! Only store owners have access to this page.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.save()
            messages.success(request, 'Successfully added post!')
            return redirect(reverse('blog'))

        else:
            messages.error(request,
                           'Failed to add post.'
                           'Please ensure the form is valid.')
    else:
        form = BlogForm()

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_post(request, slug):
    """ Edit a blog post  """
    if not request.user.is_superuser:
        messages.error(request,
                       'Oops! Only store owners have access to this page.')
        return redirect(reverse('home'))
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited blog post!')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Failed to edit blog post.'
                           'Please ensure the form is valid.')

    else:
        form = BlogForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, slug):
    """ Delete a post from the blog """
    if not request.user.is_superuser:
        messages.error(request,
                       'Oops! Only store owners have access to this page.')
        return redirect(reverse('home'))
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(reverse('blog'))
