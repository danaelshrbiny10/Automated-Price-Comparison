from django import template

register = template.Library()

@register.simple_tag
def param_replace(request, **kwargs):
    updated = request.GET.copy()
    print(updated)
    for k, v in kwargs.items():
        if v is not None:
            updated[k] = v
        else:
            updated.pop(k, 0)
    print(updated.urlencode())
    return updated.urlencode()