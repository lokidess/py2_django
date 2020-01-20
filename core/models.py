from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.timezone import now


class TimedAbstractModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def image_upload_to(instance, filename):
    cur_date = now()
    # return f"{cur_date.year}/{cur_date.month}/{cur_date.day}"
    return f"images"


class PostManager(models.Manager):

    def get_published(self):
        return self.get_queryset().filter(is_published=True)

    def get_published_with_users(self):
        return self.get_published().select_related('author')


class Post(TimedAbstractModel):

    PEGI_ADULT = 1
    PEGI_TEEN = 2
    PEGI_ALL = 3
    PEGI_CHOICES = (
        (PEGI_ADULT, '18+'),
        (PEGI_TEEN, '16+'),
        (PEGI_ALL, 'All')
    )

    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True)
    # greeting = models.CharField(max_length=255, blank=True, null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to=image_upload_to, blank=True, null=True)
    pegi = models.PositiveSmallIntegerField(choices=PEGI_CHOICES)
    # file = models.FileField(upload_to='tmp_files')

    objects = PostManager()

    class Meta:
        ordering = ('-id', )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk:
            print('update')
        else:
            print('create')
        return super(Post, self).save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        return super(Post, self).delete(using, keep_parents)


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


def pre_update_handler(*args, **kwargs):
    kwargs['instance'].title = 'EVAL ARE EVIL!!!!'


# pre_save.connect(pre_update_handler, sender=Post)

