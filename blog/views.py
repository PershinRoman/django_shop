from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import BlogPost


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Только опубликованные посты
        return BlogPost.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        # Увеличиваем счётчик просмотров
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save(update_fields=['views_count'])
        return obj


class BlogCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/blog_form.html'
    fields = ['title', 'content', 'preview', 'is_published']

    def get_success_url(self):
        return reverse_lazy('blog:detail', kwargs={'pk': self.object.pk})


class BlogUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/blog_form.html'
    fields = ['title', 'content', 'preview', 'is_published']

    # После редактирования — на страницу поста
    success_url = reverse_lazy('blog:detail')   # ← работает только если pk передаётся автоматически


    # Лучше так (более надёжно):
    def get_success_url(self):
        return reverse_lazy('blog:detail', kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:list')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        # Увеличиваем просмотры
        obj.views_count += 1
        obj.save(update_fields=['views_count'])

        # Проверяем, достигли ли 100
        if obj.views_count == 100:
            send_mail(
                subject='Поздравляем! Статья набрала 100 просмотров',
                message=f'Статья "{obj.title}" достигла 100 просмотров!',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],  # себе на почту
                fail_silently=False,
            )

        return obj