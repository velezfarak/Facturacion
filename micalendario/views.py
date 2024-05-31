from django.shortcuts import render
import calendar
# Create your views here.

def  calendario(request):
    text_calendar = calendar.TextCalendar()
    list_dias = text_calendar.itermonthdays2(2024, 5)
    losdias = [dias for dias in list_dias]

    return render(request,'micalendario/lcalendar.html',{'calendario':'calendario',
                                                   'dias':losdias})
