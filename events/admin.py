from django.contrib import admin

from .models import Venue, Event, MyClubUser

#admin.site.register(Venue)
#admin.site.register(Event)
admin.site.register(MyClubUser)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date', 'description', 'manager')
    list_display = ('name', 'event_date', 'venue')
    list_filter = ('name', 'event_date')
    ordering = ('-event_date',)

