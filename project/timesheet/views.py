import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from timesheet.models import Timesheet


# Create your views here.


@login_required
def new_timesheet(request):
    Timesheet.objects.create(user_id=request.user.id,
                             start_date=datetime.datetime.now())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def stop_timesheet(request):
    Timesheet.objects.filter(user_id=request.user.id,
                             end_date=None).update(end_date=datetime.datetime.now())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

