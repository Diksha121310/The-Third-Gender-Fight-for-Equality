"""VR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.urls import path
import app.views
from VR import settings

urlpatterns = [
                  path('', app.views.index),
                  path('mregistration', app.views.mregistration),
                  path('vregistration', app.views.vregistration),
                  path('eregistration', app.views.eregistration),
                  path('videos', app.views.videos),
                  path('login', app.views.login),
                  path('eventmaster', app.views.eventmaster),
                  path('videomaster', app.views.videomaster),
                  path('member', app.views.member),
                  path('volunteer', app.views.volunteer),
                  path('employer', app.views.employer),
                  path('uploadadoptiondata', app.views.uploadadoptiondata),
                  path('viewadoptiondata', app.views.viewadoptiondata),
                  path('viewadoptionrequest', app.views.viewadoptionrequest),
                  path('downloadresume', app.views.downloadresume),
                  path('addjob', app.views.addjob),
                  path('viewjob', app.views.viewjob),
                  path('addevent', app.views.addevent),
                  path('viewevent', app.views.viewevent),
                  path('addvideo', app.views.addvideo),
                  path('viewvideo', app.views.viewvideo),
                  path('jobs', app.views.jobs),
                  path('adoptions', app.views.adoptions),
                  path('astatus', app.views.astatus),
                  path('jstatus', app.views.jstatus),
                  path('changepassword', app.views.changepassword),
                  path('nregistration', app.views.nregistration),
                  path('ngo', app.views.ngo),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
