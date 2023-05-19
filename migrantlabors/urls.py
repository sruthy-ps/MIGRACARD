"""migrantlabors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from migrantapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('adminhome', views.adminhome, name='adminhome'),
    path('adminaddlabor', views.adminaddlabor, name='adminaddlabor'),
    path('adminaddpolice', views.adminaddpolice, name='policereg'),
    path('delpolice', views.deletepolice, name='deletepolice'),
    path('adminviewreglabors', views.adminviewreglabors, name='adminviewreglabors'),
    path('adminviewlabordetails', views.adminviewlabordetails,
         name='adminviewlabordetails'),
    path('policehome', views.policehome, name='policehome'),
    path('policechangepwd', views.policechangepwd, name='policechangepwd'),
    path('policeviewreglabors', views.policeviewreglabors,
         name='policeviewreglabors'),
    path('policeviewlabordetails', views.policeviewlabordetails,
         name='policeviewlabordetails'),
    path('policeapprovelabors', views.policeapprovelabors,
         name='policeapprovelabors'),
    path('adminlaborwithnoc', views.adminlaborwithnoc, name='adminlaborwithnoc'),
    path('contractorreg', views.contractorreg, name='contractorreg'),
    path('admincontractorrequest', views.admincontractorrequest,
         name='admincontractorrequest'),
    path('adminapprovecontractor', views.adminapprovecontractor,
         name='adminapprovecontractor'),
    path('adminchoosecontractor', views.adminchoosecontractor,
         name='adminchoosecontractor'),
    path('adminchoosecontractor', views.adminchoosecontractor,
         name='adminchoosecontractor'),
    path('admingeneratecard', views.admingeneratecard, name='admingeneratecard'),
    path('jobcard', views.jobcard, name='jobcard'),
    path('adminsearchlabor', views.adminsearchlabor, name='adminsearchlabor'),
    path('contractorhome', views.contractorhome, name='contractorhome'),
    path('contractorviewlabors', views.contractorviewlabors,
         name='contractorviewlabors'),
    path('contractorchangepwd', views.contractorchangepwd,
         name='contractorchangepwd'),
    path('contractorviewlabordetails', views.contractorviewlabordetails,
         name='contractorviewlabordetails'),
    path('userhome', views.userhome, name='userhome'),
    path('userchangepwd', views.userchangepwd, name='userchangepwd'),
    path('userreg', views.userreg, name='userreg'),
    path('userworkrequest', views.userworkrequest, name='userworkrequest'),
    path('contractorworkrequest', views.contractorworkrequest,
         name='contractorworkrequest'),
    path('contractoraddtender', views.contractoraddtender,
         name='contractoraddtender'),
    path('usertendercalls', views.usertendercalls, name='usertendercalls'),
    path('userapprovetender', views.userapprovetender, name='userapprovetender'),
    path('userwork', views.userwork, name='userwork'),
    path('userviewlabors', views.userviewlabors, name='userviewlabors'),
    path('contractorwork', views.contractorwork, name='contractorwork'),
    path('contractoraddlabors', views.contractoraddlabors,
         name='contractoraddlabors'),
    path('contractorupdatework', views.contractorupdatework,
         name='contractorupdatework'),
    path('contractorcompletedwork', views.contractorcompletedwork,
         name='contractorcompletedwork'),
    path('usercompletedwork', views.usercompletedwork, name='usercompletedwork'),
    path('useraddfeedback', views.useraddfeedback, name='useraddfeedback'),
    path('contractorfeedback', views.contractorfeedback, name='contractorfeedback'),
    path('usercomplaint', views.usercomplaint, name='usercomplaint'),
    path('policeviewcomplaint', views.policeviewcomplaint,
         name='policeviewcomplaint'),
    path('policesearchsimilarlabor', views.policesearchsimilarlabor,
         name='policesearchsimilarlabor'),
    path('policeworkdetails', views.policeworkdetails, name='policeworkdetails'),
    path('contractorviewworkplace', views.contractorviewworkplace,
         name='contractorviewworkplace'),
    path('verifylabor', views.verifylabor),
    path('policeaddcriminals', views.policeaddcriminals),
    path('policeviewcriminals', views.policeviewcriminals),
]
