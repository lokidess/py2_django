from django.contrib import messages
from django.views.generic import TemplateView, FormView, CreateView, ListView, DeleteView
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.views.generic.edit import UpdateView, DeleteView
from core.forms import PostCreate
from core.models import Post, Tag
from django.db.models import Count, F, Value, Sum
from django.shortcuts import redirect


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
    fields = '__all__'
    # form_class = PostCreate
    # success_url = '/post_create/'
    # queryset = Post.objects.all()

    def get_success_url(self):
        return f'/post_edit/{self.kwargs["pk"]}/'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

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


        # user = User.objects.get(id=1)
        #
        # context['posts'] = user.post_set.all()

        # context['posts'] = user.post_set.all()

        # print(User.objects.filter(post__title='qwe'))

        # context['posts'] = Post.objects.filter(
        #     is_published=True,
        #     title__startswith='QWE',
        #     author='admin'
        # ).select_related('author').prefetch_related('tags')

        # Post.objects.all().update(
        #     title='qweqwe',
        #     text='hello'
        # )

        # post = Post.objects.get(id=1)
        # post.title = 'new'
        # post.text = 'hola'
        # post.save()

        # Post.objects.filter(title__icontains='qwe').delete()
        #
        # Post.objects.get(id=1).delete()

        # tags = ['сказочноебали', 'test', 'loki']
        # tags_obj = []
        # for tag_name in tags:
        #     # Tag.objects.create(name=tag_name)
        #     tags_obj.append(
        #         Tag(name=tag_name)
        #     )
        # Tag.objects.bulk_create(tags_obj)
        # Post.objects
        # Post.objects.get_or_create(title='qwe', defaults={
        #     'title': 'not found qwe',
        #     'text': 'qwe',
        #     'author_id': 1,
        #     'pegi': Post.PEGI_ALL
        # })

        # Tag.objects.create(
        #     name='some_test_name'
        # )

        # Tag.objects.get_or_create(name='some_test_name')

        # print(context['posts'])
        # context['posts'] = Post.objects.get_published_with_users()

        # context['posts'] = Post.objects.all()\
        #     .prefetch_related('tags')\
        #     .select_related('author')\
        #     .order_by('-created_at')[:2]
        # context['posts'] = Post.objects.filter(
        #     title='qwe', pegi=Post.PEGI_TEEN
        # )
        # | - OR
        # & - AND
        # ~ - NOT

        # my_query_logic = Q()
        # my_query_logic.add(Q(title='qwe'), Q.AND)
        # my_query_logic.add(Q(pegi=Post.PEGI_TEEN), Q.OR)

        # context['posts'] = Post.objects.filter(
        #     # Q(title='qwe') & Q(pegi=Post.PEGI_TEEN)
        #     # ~Q(pegi=Post.PEGI_ADULT)
        #     # my_query_logic
        #     # title=F('text')
        #     # text__startswith=F('title')
        # )
        # from django.db import models
        # context['posts'] = Post.objects.all().annotate(
        #     tags_count=Count('tags', output_field=models.CharField())
        # ).filter(tags_count__gte=2).order_by('-tags_count').prefetch_related('tags')\
        #     .select_related('author')
        context['posts'] = Post.objects.all().values(
            'title', 'author__username'
        )
        #
        # context['posts_count'] = Post.objects.all().annotate(
        #     tags_count=Count('tags')
        # ).aggregate(Sum('tags_count'))

        # context['post'] = Post.objects.filter().first()
        # context['post'] = Post.objects.filter().last()



        # context['posts_count'] = sum(context['posts_count'])
        # context['my_query_logic'] = my_query_logic

        return context
