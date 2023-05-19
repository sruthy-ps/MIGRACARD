"""migrantlabors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
    path('adminhome', views.adminhome),
    path('userreg', views.userreg),
    path('contractorreg', views.contractorreg),
    path('adminaddpolice', views.adminaddpolice),
    path('adminaddlabor', views.adminaddlabor),
    path('login', views.login),
    path('userhome', views.userhome),
    path('contractorhome', views.contractorhome),
    path('policehome', views.policehome),
    path('admincontractorrequest', views.admincontractorrequest),
    path('adminapprovecontractor', views.adminapprovecontractor),
    path('adminviewreglabors', views.adminviewreglabors),
    path('adminviewlabordetails', views.adminviewlabordetails),
    path('adminlaborwithnoc', views.adminlaborwithnoc),
    path('adminlaborrequest', views.adminlaborrequest),
    path('admingeneratecard', views.admingeneratecard),
    path('jobcard', views.jobcard),
    path('policeviewreglabors', views.policeviewreglabors),
    path('policeviewlabordetails', views.policeviewlabordetails),
    path('policeapprovelabors', views.policeapprovelabors),
    path('policeviewcomplaint', views.policeviewcomplaint),
    path('policesearchsimilarlabor', views.policesearchsimilarlabor),
    path('policeworkdetails', views.policeworkdetails),
    path('userworkrequest', views.userworkrequest),
    path('usertendercalls', views.usertendercalls),
    path('userapprovetender', views.userapprovetender),
    path('userwork', views.userwork),
    path('userviewlabors', views.userviewlabors),
    path('usercompletedwork', views.usercompletedwork),
    path('usercomplaint', views.usercomplaint),
    path('contractorviewlabors', views.contractorviewlabors),
    path('contractorviewlabordetails', views.contractorviewlabordetails),
    path('contractorrequestlabor', views.contractorrequestlabor),
    path('contractorrequest', views.contractorrequest),
    path('contractorlabrequest', views.contractorlabrequest),
    path('contractorworkrequest', views.contractorworkrequest),
    path('contractorviewworkplace', views.contractorviewworkplace),
    path('contractoraddtender', views.contractoraddtender),
    path('contractorwork', views.contractorwork),
    path('contractoraddlabors', views.contractoraddlabors),
    path('contractorupdatework', views.contractorupdatework),
    path('contractorcompletedwork', views.contractorcompletedwork),
    path('adminapproverequest', views.adminapproverequest),
    path('policeupdatecomplaint', views.policeupdatecomplaint),
    path('addpayment', views.addpayment),
    path('adminupdatepolice', views.adminupdatepolice),
    path('contractorprofile', views.contractorprofile),
    path('updatelabourdetails', views.updatelabourdetails),
    path('userprofile', views.userprofile),
    path('adminviewalllabor', views.adminviewalllabor),
    path('adminviewalluser', views.adminviewalluser),

    
    

    

    
    

]
