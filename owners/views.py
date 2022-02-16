# http -v POST 127.0.0.1:8000/opener name="" email="" age=""
# http -v POST 127.0.0.1:8000/cat name="" age="" opener=""

import json

from django.http  import JsonResponse
from django.views import View

from owners.models import Opener, Cat


class CatAndOpenerView(View):
    def get(self, request):
        cats = Cat.objects.all()
        result=[]
        for i in cats:
            result.append(
                {
                    'opener_of_cat':Opener.objects.get(id=i.opener_id).name,
                    'age_of_opener':Opener.objects.get(id=i.opener_id).age,
                    'age_of_cat':i.age,
                    'name_of_cat':i.name,
                }
            )
        return JsonResponse({'result':result},status=200)


class OpenerView(View):
    def get(self, request):
        openers = Opener.objects.all()
        result=[]
        for i in openers:
            result.append(
                {
                    'name':i.name,
                    'email':i.email,
                    'age':i.age,
                }
            )
        return JsonResponse({'result':result},status=200)

    def post(self, request):
        try:
            data = json.loads(request.body)
            Opener.objects.create(
                name  = data["name"],
                email = data["email"],
                age   = data["age"],
            )
        except KeyError:
            return JsonResponse({"MESSEGE":"KEYERROR"}, status=400)
        return JsonResponse({"MESSEGE":"CREATED"}, status=201)

class CatView(View):
    def get(self, request):
        cats = Cat.objects.all()
        result=[]
        for i in cats:
            result.append(
                {
                    'name':i.name,
                    'age':i.age,
                    'opener_name':Opener.objects.get(id=i.opener_id).name
                }
            )
        return JsonResponse({'result':result},status=200)

    def post(self, request):
        data = json.loads(request.body)
        Cat.objects.create(
            name      = data["name"],
            age       = data["age"],
            opener_id = Opener.objects.get(id = int(data["opener"])).id,
        )
        return JsonResponse({"MESSEGE":"CREATED"}, status=201)