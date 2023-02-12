from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Turtle
from django.views import View
from .helpers import GetBody
from django.core.serializers import serialize

# Create your views here.

class TurtleView(View):
    ## Index
    def get(self, request):
        all = Turtle.objects.all()
        serialized = serialize("json", all)
        finalData = json.loads(serialized)
        return JsonResponse(finalData, safe=False)
    ## Create
    def post(self, request):
        body = GetBody(request)
        turtle = Turtle.objects.create(name=body["name"], age=body["age"])
        finalData = json.loads(serialize("json", [turtle]))
        return JsonResponse(finalData, safe=False)
    
class TurtleViewID(View):
    ## SHOW
    def get (self, request, id):
        turtle = Turtle.objects.get(id=id)
        finalData = json.loads(serialize("json", [turtle]))
        return JsonResponse(finalData, safe=False)
    
    def put (self, request, id):
        body = GetBody(request)
        Turtle.objects.filter(id=id).update(**body)
        turtle = Turtle.objects.get(id=id)
        finalData = json.loads(serialize("json", [turtle]))
        return JsonResponse(finalData, safe=False)
    
    def delete (self, request, id):
        turtle = Turtle.objects.get(id=id)
        turtle.delete()
        finalData = json.loads(serialize("json", [turtle]))
        return JsonResponse(finalData, safe=False)