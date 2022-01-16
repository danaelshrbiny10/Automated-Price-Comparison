from django.contrib.auth.models import User
from django.http import request
from accounts.models import Profile
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.postgres.search import TrigramDistance
from django.db.models import Q
from products.models import category, notifyme,priceHistory
from souq.models import Souq
from jumia.models import Jumia
from noon.models import Noon
from .filter import propertyFilter
from django_filters.views import FilterView
from notifications.signals import notify
from django.core.paginator import Paginator
from django.http import JsonResponse

from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

# UPDATE jumia SET manufacture = LOWER(manufacture);




def population_chart(request,itemid):
    print("(========================================================================================)")

    print(itemid)
    
    print("(========================================================================================)")
    # return("hello")
    labels = []
    data = []
    soquD=Souq.objects.get(pk=itemid)
    # queryset = priceHistory.objects.values('timeDate').order_by('timeDate')
    queryset = priceHistory.objects.filter(souq=soquD).order_by('timeDate')

    for entry in queryset:
        labels.append(entry.timeDate)
        data.append(entry.lastprice)
        
    
    return JsonResponse(data={
        "view": "<products.views.LineChartJSONView object at 0x000001DF0954F910>",
        "labels":labels,
        "datasets": [
            {
                "data":data,
                "backgroundColor": "rgba(202, 201, 197, 0.5)",
                "borderColor": "rgba(202, 201, 197, 1)",
                "pointBackgroundColor": "rgba(202, 201, 197, 1)",
                "pointBorderColor": "#fff",
                "label": "souq",
                "name": "souq"
            }
        ]
    })



class LineChartJSONView(BaseLineChartView):


    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["souq"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35]]


line_chart = TemplateView.as_view(template_name='souq/souq_detail.html')
line_chart_json = LineChartJSONView.as_view()     


class SearchResultsView(FilterView):
    model = Souq
    paginate_by = 50
    filterset_class = propertyFilter
    template_name= 'product/souq_list.html'


    def get_queryset(self): # new
        query = self.request.GET.get('q','')
        object_lists = Souq.objects.filter(
            Q(title__icontains=query))
        return object_lists  


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["brands"] = Souq.objects.values('manufacture').distinct().order_by('manufacture')
        context["Categories"]  = category.objects.all().order_by('sweetName')
        # context["cate"] = self.GET.get('category')
        context["counts"] = self.object_list.count()


        return context


def is_valid_queryparam(param):
    return param != '' and param is not None


def Product(request):
    qs = Souq.objects.all()
    count = Souq.objects.all().count()
    Categories = category.objects.all().order_by('sweetName')
    bar = category.objects.values('id')

    Recently_Viewed =Souq.objects.filter()[:50]
    manufacture = request.GET.get('manufacture')
    categorys = request.GET.get('category')
    paginator = Paginator(qs, 10) # Show 50 contacts per page.
    brands= Souq.objects.values('manufacture').distinct().order_by('manufacture')
    obj = Souq.objects.values('rate')
    # print('+++++++++++++++++++++++++++++++++++++=')
    # print(Categories[2])
    if is_valid_queryparam (manufacture) and manufacture != 'Choose...':
        qs = qs.filter(manufacture__icontains=manufacture)
        count = qs.filter(manufacture__icontains=manufacture).count()
        paginator = Paginator(qs, 50) # Show 50 contacts per page.
    if is_valid_queryparam (categorys) and categorys != 'Choose...':
        qs = qs.filter(category__sweetName=categorys)
        count = qs.filter(category__sweetName=categorys).count()
        paginator = Paginator(qs, 50) # Show 50 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'product/jumia_list.html',{
        'page_obj' : page_obj ,
        'Categories' : Categories,
        'brands':brands,
        'count':count,
        'Recently_Viewed':Recently_Viewed,
        'object': obj,
        'categorys':categorys,
        'bar':bar
        
         })

class itemDetails(DetailView):
    model = Souq
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        curTitle= self.object.title
        curManufacture=self.object.manufacture
        souq=Souq.objects.annotate(distance=TrigramDistance('title',curTitle),).filter(distance__lte=0.7,manufacture=curManufacture).order_by('distance')[:4]
        noon=Noon.objects.annotate(distance=TrigramDistance('title',curTitle),).filter(distance__lte=0.7,manufacture=curManufacture).order_by('distance')[:4]
        jumia=Jumia.objects.annotate(distance=TrigramDistance('title',curTitle),).filter(distance__lte=0.7,manufacture=curManufacture).order_by('distance')[:4]
        data['noon'] = noon
        data['jumia'] = jumia
        data['souqPlus'] = souq
        data['Categories'] =category.objects.all().order_by('sweetName')
        return data 






def load_brand(request):
    categoryName = request.GET.get('category')
    brandDrop = Souq.objects.filter(category=category.objects.get(sweetName=categoryName)).values("manufacture").distinct().order_by('manufacture')
    print(brandDrop)
    data = []
    for item in brandDrop:
        dataa={}
        dataa["name"] = item["manufacture"]
        data.append(dataa)
    return JsonResponse(data=data, safe=False)

def interest(request):
    if (request.method == "POST") and ("subscribe" in request.POST):
        # profile = Profile.objects.get(user = request.user)
        # sender = User.objects.get(username=profile)
        # receiver = User.objects.get(username=profile)
        # notify.send(sender, recipient=receiver, verb='Message', description=f"interest in {request.POST.get('title')}")
        b = notifyme.objects.create(username=request.POST.get('username'),souqid=request.POST.get('id'),lastPrice=request.POST.get('lastprice'),expectedPrice=request.POST.get('num'))
        b.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


