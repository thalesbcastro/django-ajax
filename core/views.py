from django.http import JsonResponse
from django.views.generic import ListView, CreateView
from django.views.generic.base import View, TemplateView

from .models import CrudUser


# Create your views here.


class CrudView(TemplateView):
    template_name = 'core/crud.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = CrudUser.objects.all()
        return context


class CreateCrudUser(View):
    def get(self, request):
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.create(
            name=name1,
            address=address1,
            age=age1
        )

        user = {'id': obj.id, 'name': obj.name, 'address': obj.address, 'age': obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)


class DeleteCrudUser(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        CrudUser.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class UpdateCrudUser(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.get(id=id1)
        obj.name = name1
        obj.address = address1
        obj.age = age1
        obj.save()

        user = {'id': obj.id, 'name': obj.name, 'address': obj.address, 'age': obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)
