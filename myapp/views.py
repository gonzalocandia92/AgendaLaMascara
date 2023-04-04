from django.shortcuts import render, redirect
from django.http import JsonResponse 
from myapp.models import Events 
from myapp.forms import EventForm
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.

@login_required
def index(request):  
    group = Group.objects.get(user=request.user)
    
    if group.name == 'direccion':
        all_events = Events.objects.all()
        context = {
            "events":all_events,
            "form": EventForm
        }
        return render(request,'index.html',context)
    elif group.name == 'visitante':
        all_events = Events.objects.all()
        context = {
            "events":all_events,
            }
        return render(request,'read_only.html',context)
    
def all_events(request):                                                                                                 
    all_events = Events.objects.all()                                                                                    
    out = []                                                                                                             
    for event in all_events:                                                                                             
        out.append({                                                                                                     
            'title': event.name,                                                                                         
            'id': event.id,                                                                                              
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),    
            'description': event.description,                                                         
        })                                                                                                               
                                                                                                                      
    return JsonResponse(out, safe=False) 
 
def crear_event(request):
    if request.method == "POST" or None:
        name = request.POST["name"]
        startTime = request.POST["start-time"]
        startDate = request.POST["start-date"]
        endTime = request.POST["end-time"]
        endDate = request.POST["end-date"]
        startStr = startDate + ' ' + startTime + ':00'
        start = datetime.strptime(startStr, '%Y-%m-%d %H:%M:%S')
        endStr = endDate + ' ' + endTime + ':00'
        end = datetime.strptime(endStr, '%Y-%m-%d %H:%M:%S')
        description = request.POST["description"]
        Events.objects.get_or_create(
            name = name,
            start = start,
            end = end,
            description = description,
        )
        return redirect('index')
    else:
        return render(request, "event.html")

def actualizar_event(request, id):
    if request.method == "POST" or None:
        name = request.POST["name"]
        startTime = request.POST["start-time"]
        startDate = request.POST["start-date"]
        endTime = request.POST["end-time"]
        endDate = request.POST["end-date"]
        startStr = startDate + ' ' + startTime + ':00'
        start = datetime.strptime(startStr, '%Y-%m-%d %H:%M:%S')
        endStr = endDate + ' ' + endTime + ':00'
        end = datetime.strptime(endStr, '%Y-%m-%d %H:%M:%S')
        description = request.POST["description"]
        event = get_object_or_404(Events, id=id)
        event.start = start
        event.end = end
        event.name = name
        event.description = description
        event.save()
        return redirect('index')
    else:
        return render(request, "event.html")
    

def add_event(request):
    form = EventForm(request.POST or None)
    if request.POST and form.is_valid():
        name = form.cleaned_data["name"]
        start = form.cleaned_data["start"]
        end = form.cleaned_data["end"]
        Events.objects.get_or_create(
            name = name,
            start = start,
            end = end,
        )
        return redirect('index')
    return render(request, "event.html", {"form": form})



 
def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    description = request.GET.get("description", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.description = description
    event.save()
    data = {}
    return JsonResponse(data)
 
def remove(request, id):
    event = get_object_or_404(Events, id=id)
    event.delete()
    return redirect('index')