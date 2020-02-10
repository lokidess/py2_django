from django.contrib import messages
from django.views.generic import TemplateView, FormView, CreateView, ListView, DeleteView
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.views.generic.edit import UpdateView, DeleteView
from core.forms import PostCreate
from core.models import Post, Tag
from django.db.models import Count, F, Value, Sum
from django.shortcuts import redirect
from django.template.loader import get_template


# class PostCreateView(TemplateView):
#     template_name = 'post_create.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(PostCreateView, self).get_context_data(**kwargs)
#         context['form'] = PostCreate()
#         return context
#
#     def post(self, request):
#         context = self.get_context_data()
#         form = PostCreate(data=request.POST)
#
#         if form.is_valid():
#             form.save(user=request.user)
#
#         context['form'] = form
#
#         return self.render_to_response(
#             context=context
#         )


# class PostCreateView(FormView):
#     template_name = 'post_create.html'
#     form_class = PostCreate
#     success_url = '/post_create/'
#
#     def form_valid(self, form):
#         self.new_obj = form.save(self.request.user)
#         return super(PostCreateView, self).form_valid(form)

    # def form_invalid(self, form):
    #     return

    # def get_form_kwargs(self):
    #     return {'instance': Post.objects.all().first()}

    # def get_initial(self):
    #     return {
    #         'pegi': Post.PEGI_ALL
    #     }

    # def get_success_url(self):
    #     return f'/post-detail/{self.new_obj.id}'

    # def get_form_class(self):
    #     pass


class PostCreateView(CreateView):
    template_name = 'post_create.html'
    form_class = PostCreate
    success_url = '/post_create/'

    def form_valid(self, form):
        form.save(user=self.request.user)
        messages.add_message(request=self.request, message='CREATED!', level=1)
        return redirect(self.success_url)


class PostUpdateView(UpdateView):
    template_name = 'post_create.html'
    model = Post
    form_class = PostCreate
    # fields = '__all__'
    # form_class = PostCreate
    # success_url = '/post_create/'
    # queryset = Post.objects.all()

    def get_success_url(self):
        return f'/post_edit/{self.kwargs["pk"]}/'

    # def get_queryset(self):
    #     return Post.objects.filter(author=self.request.user)

    # def form_valid(self, form):
    #     form.save(user=self.request.user)
    #     return redirect(self.get_success_url())


class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    model = Post
    success_url = '/'


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['posts'] = Post.objects.all()
        context['lst'] = [1, 2, 3, 4]
        context['dct'] = {'name': 'Loki', 'age': 30}
        context['tags'] = "BOLT"
        context['post_model'] = Post.objects

        # tpl = get_template('yamls/conf.yml')
        # new = tpl.render({'ip': "127.0.0.1", 'port': 937})
        #
        # with open('media/yamls/config.yml', 'w') as conf:
        #     conf.write(new)

        return context


class MyAjaxView(TemplateView):
    template_name = 'test_tpl.html'

    def get_context_data(self, **kwargs):
        context = super(MyAjaxView, self).get_context_data(**kwargs)
        context['post'] = {'id': "OLOLO"}
        context['a'] = 123123
        context['b'] = 123123213
        return context
