from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView

from posts.forms import CommentForm
from posts.models import Post, Comment


class CommentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "index.html"
    model = Comment
    form_class = CommentForm
    success_message = "Комментарий добавлен"

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs.get("pk"))
        comment = form.save(commit=False)
        comment.post = post
        comment.author = self.request.user
        print(comment)
        comment.save()
        return redirect("index")
