from django.shortcuts import render

import calendar
from calendar import HTMLCalendar

from datetime import datetime

from .forms import VenueForm

from .models import Event


def add_venue(request):
    #submitted = False
    #if request.method == "POST":

    form = VenueForm
    return render(request, 'events/add_venue.html', {'form': form})


def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/events_list.html',
                  {'event_list': event_list})


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = 'Ivan'
    month = month.title()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    month = month.capitalize()
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%I:%M:%S %p')

    cal = HTMLCalendar().formatmonth(
        year,
        month_number)
    return render(request, 'events/home.html', {'name': name,
                                                'year': year,
                                                'month': month,
                                                'month_number': month_number,
                                                'cal': cal,
                                                'current_year': current_year,
                                                'time': time,
                                                })
