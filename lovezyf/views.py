from django.shortcuts import render
from datetime import datetime
from .form import CommentForm
from .models import Comment
from django.http import HttpResponse

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            comment.name = form.cleaned_data['name']
            comment.message = form.cleaned_data['content']
            comment.save()
    else:
        form = CommentForm()
    # begin_time = datetime(2019, 6, 10, 15, 27, 20)
    # the_time = datetime.now() - begin_time
    # days = the_time.days
    # hours = the_time.seconds // 3600
    # minutes = (the_time.seconds % 3600) // 60
    # seconds = the_time.seconds % 60
    # time_str = "%d  天  %d  时  %d  分" % (days, hours, minutes)
    context = {
        # "time_str": time_str,
        "comment_form": form,
        "comment_list": Comment.objects.order_by('-time')
    }
    return render(request, 'lovezyf/index.html', context)
