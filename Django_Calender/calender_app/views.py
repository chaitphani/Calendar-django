from django.shortcuts import render, redirect
from .models import Event
from django.http import JsonResponse,HttpResponse
from django.core import serializers

# Create your views here.

def calendar(request):
    events_list = Event.objects.all()

    return render(request, 'index.html', {"events":events_list})

def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Event(name=str(title), start=start, end=end)
    event.save()
    event = Event.objects.all()
    datas={}
    datas['events'] = serializers.serialize("json",event)
    print(datas)
    return JsonResponse(datas)


def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Event.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()

    event = Event.objects.all()
    datas={}
    datas['events'] = serializers.serialize("json",event)
    print(datas)
    return JsonResponse(datas)


def remove(request):
    id = request.GET.get("id", None)
    event = Event.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)