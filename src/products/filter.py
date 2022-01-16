from souq.models import Souq
import django_filters
from souq.models import Souq

class propertyFilter(django_filters.FilterSet):
    def get_choices():
        choices = []
        for k in Souq.objects.values_list("manufacture").distinct().order_by('manufacture'):
            choices.append((k[0], k[0]))
        return choices
    manufacture = django_filters.ChoiceFilter(choices=get_choices())

    
    class Meta:
        model = Souq
        fields = ['category','manufacture']