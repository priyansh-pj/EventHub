from django.shortcuts import render, redirect
from .forms import *


def event_list(request):
    view_data = {
        "title": 'events List',
        "events": Event.objects.filter(status=True)
    }
    return render(request, 'event_list.html', view_data)


def event_details(request, id):
    view_data = {
        "title": 'events Info',
        "events": Event.objects.get(id=id)
    }
    return render(request, 'event_details.html', view_data)


def create_event(request):
    view_data = {
        "title": 'Create Event',
        "form": EventForm()
    }
    print(request.POST)
    if request.method == "POST":
        forms = EventForm(request.POST, request.FILES)

        if forms.is_valid():
            forms.save()
            return redirect('Event_List')
    return render(request, 'create_event.html', view_data)


def delete_event(request, id):
    event_data = Event.objects.get(id=id)
    event_data.delete()
    return redirect('Event_List')


def edit_event(request, id):
    event_data = Event.objects.get(id=id)
    view_data = {
        "title": 'Edit Event',
        "id": id,
        "form": EventForm(instance=event_data)
    }
    if request.method == 'POST':
        forms = EventForm(request.POST, request.FILES, instance=event_data)
        if forms.is_valid():
            forms.save()
            return redirect('Event_List')

    return render(request, 'edit_event.html', view_data)
