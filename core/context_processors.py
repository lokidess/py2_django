from core.models import Tag


def test_context_processor(request):
    return {
        'tags': Tag.objects.all()
    }
