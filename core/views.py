from django.views.generic import TemplateView, FormView, CreateView, ListView, DeleteView
from django.contrib.auth.models import User
from core.models import Post, Tag


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

        Post.objects.filter(title__icontains='qwe').delete()

        Post.objects.get(id=1).delete()

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
        return context
