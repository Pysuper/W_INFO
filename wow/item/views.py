from django.http import JsonResponse
from django.shortcuts import render
import json
from item.models import Items


def search(request):
    if request.method == "GET":
        return render(request, "items/search.html")
    key = json.loads(request.body)["key"]
    if key:
        item = Items.objects.get(name=key)
        if item:
            return JsonResponse({"data": item.table})
    return JsonResponse({"status": False})
