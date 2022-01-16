from products.models import category

def add_variable_to_context(request):
    Categories = category.objects.all().order_by('sweetName')
    return {
    'Categories':Categories
    }