# coding=utf-8
from django.views.generic import TemplateView, DetailView, ListView
from data.models import BlogArticle


class IndexView(TemplateView):
    
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        return context


class BlogDetailView(DetailView):

    model = BlogArticle


class BlogListView(ListView):

    model = BlogArticle
    paginate_by = 10
    context_object_name = 'object_list'

    def get_queryset(self):
        classfy_id = self.request.GET.get('classfy_id', None)

        queryset = self.model.objects.all().order_by('-updatetime')
        if classfy_id:
            queryset = queryset.filter(classify_id=classfy_id)
        return queryset
