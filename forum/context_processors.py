
from .models import Category


def cat_list(request):
    cat = Category.objects.all()
    return {'cat':cat}
