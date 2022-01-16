from products.models import category
from setting.models import Info




def get_footer(request):
    footer=Info.objects.last()
    return {'footer': footer}