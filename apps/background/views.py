from django.shortcuts import render
from apps.background import models as m


def landingPage(request):
    basicStatics = m.statistic.objects.all()
    
    return render(request, "background/landing_page.html", {'basicStatistics': basicStatics})