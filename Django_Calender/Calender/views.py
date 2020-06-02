from django.shortcuts import render
from .models import Events
from django.http import JsonResponse,HttpResponse
from django.core import serializers

# Create your views here.
def calendar(request):
    all_events = Events.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'Calender/calender.html',context)

def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end)
    event.save()
    event = Events.objects.all()
    datas={}
    datas['events'] = serializers.serialize("json",event)
    print(datas)
    return JsonResponse(datas)


def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()

    event = Events.objects.all()
    datas={}
    datas['events'] = serializers.serialize("json",event)
    print(datas)
    return JsonResponse(datas)


def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)