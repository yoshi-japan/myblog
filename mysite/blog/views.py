from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DeleteView,
                                  DetailView, CreateView, UpdateView)
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment
from .forms import CommentForm, PostForm


# Create your views here.


class AboutViews(TemplateView):

    template_name = "about.html"


class PostListView(ListView):
    # this is ListView function, if this called we can display a list based on the queryset set below.
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin,CreateView):
    # @login_require decorator is only for function based view so we need to use another for CBV
    # the thing we need to use is mixin

    # where we want persons to go in cases persons are not logged in
    # these fields are necessary to have if you inherit LoginRequireMixin
    login_url = '/login/'
    redirect_field_name = "blog/post_detail.html"

    form_class = PostForm
    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = "blog/post_detail.html"
    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    # reverse_lazy waits until we actually delete the post
    success_url = reverse_lazy("post_list")


class DraftView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_data')

    #####


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = CommentForm(request.Post)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", pk=post.pk)
        else:
            form = CommentForm()
        return render(request, 'blog/comment_form.html', {'form':form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)