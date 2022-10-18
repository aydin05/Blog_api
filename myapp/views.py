from django.views.generic import ListView

from myapp.models import Post, Category


class HomePageView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'post_list'
    cat = Category

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        context['category_list'] = Category.objects.all()
        return context
