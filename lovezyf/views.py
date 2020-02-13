from django.shortcuts import render, redirect
from django.template import loader
import time
from datetime import datetime
from django.contrib import messages

# Create your views here.

def index(request):
    begin_time = datetime(2019, 6, 10, 15, 27, 20)
    the_time = datetime.now() - begin_time
    days = the_time.days
    hours = the_time.seconds // 3600
    minutes = (the_time.seconds % 3600) // 60
    seconds = the_time.seconds % 60
    time_str = "%d  天  %d  时  %d  分" % (days, hours, minutes)
    context = {
        "time_str": time_str
    }
    return render(request, 'lovezyf/index.html', context)

def submit(request):
    messages.error(request, '告诉你后台没开发┗( ▔, ▔ )┛')
    return redirect('/')