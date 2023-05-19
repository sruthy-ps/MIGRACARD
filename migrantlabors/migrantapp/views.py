from asyncio.windows_events import NULL
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Max

# Create your views here.


def index(request):
    """ 
        The function to load index page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    return render(request,"index.html")

def adminhome(request):
    """ 
        The function to load admin home page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """  
    return render(request,"adminhome.html")

def userhome(request):
    """ 
        The function to load admin home page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """  
    return render(request,"userhome.html")

def contractorhome(request):
    """ 
        The function to load admin home page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """  
    name=request.session['name']
    return render(request,"contractorhome.html",{'name':name})

def policehome(request):
    """ 
        The function to load admin home page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """  
    name=request.session['name']
    return render(request,"policehome.html",{"name":name})


def userreg(request):
    """ 
        The function to register user
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    
    if(request.POST):
        name=request.POST["Name"]
        aadhar=request.POST["Aadhar"]
        email=request.POST["Email"]
        phone=request.POST["Contact"]
        pwd=request.POST["Password"]
        user = authenticate(username=email, password=pwd)
        if user is  None:
            try:
                r = Userreg.objects.create(
                    name=name,aadhar=aadhar,email=email,contact=phone)
                r.save()
            except:
                messages.info(request, 'Sorry some error occured')
            else:
                try:
                    u = User.objects.create_user(
                        password=pwd, username=email, is_superuser=0, is_active=1, email=email)
                    ut=Usertypes(logid=u,utype="user")
                    u.save()
                    ut.save()

                except:
                    messages.info(request, 'Sorry some error occured')
                else:
                    messages.info(request,'Registration successfull')
                    return redirect("/")
        else:
             msg="Already Registered" 
             return redirect("/")          
    return render(request,"index.html",{"msg":msg})

def contractorreg(request):
    """ 
        The function to register contractor
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    
    if(request.POST):
        name=request.POST["Name"]
        address=request.POST["address"]
        licenseno=request.POST["License"]
        img=request.FILES["File"]
        email=request.POST["Email"]
        phone=request.POST["Contact"]
        pwd=request.POST["Password"]
        user = authenticate(username=email, password=pwd)
        if user is None:
            try:
                r = Contractorreg.objects.create(
                    name=name,address=address,phone=phone,email=email,license=licenseno,certificate=img)
                r.save
            except:
                messages.info(request,'Something Went wrong')
            else:
                try:
                    u = User.objects.create_user(
                        password=pwd, username=email, is_superuser=0, is_active=0, email=email)
                    ut=Usertypes(logid=u,utype="contractor")
                    u.save()
                    ut.save()
                except:
                    messages.info(request,'Sorry Login Process Error')
                else:
                    messages.info(request,'Registered Successfully')
                    return redirect("/")
        else:
                    messages.info(request,'Already Registered')
                    return redirect("/")
    return render(request,"index.html",{"msg":msg})

def adminaddpolice(request):
    """ 
        The function to add labors
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    police=Policestation.objects.all()
    if(request.POST):
        name=request.POST["Name"]
        address=request.POST["address"]
        stationcode=request.POST["StationCode"]
        circle=request.POST["Circle"]
        email=request.POST["Email"]
        phone=request.POST["Phone"]
        pwd=request.POST["Password"]
        user = authenticate(username=email, password=pwd)
        if user is None:
            try:
                r = Policestation.objects.create(
                    pscode=stationcode,pname=name,address=address,circle=circle,contact=phone,email=email,username=email)
                r.save
            except:
                messages.info(request,'Sorry register error')
            else:
                try:
                    u = User.objects.create_user(
                        password=pwd, username=email, is_superuser=0, is_active=1, email=email)
                    ut=Usertypes(logid=u,utype="police")
                    u.save()
                    ut.save()
                except:
                    messages.info(request,'Sorry Login Process Error')
                else:
                    messages.info(request,'Registered Successfully')
                    return redirect("/adminaddpolice")
        else:
                messages.info(request,'Already Registered')
                return redirect("/adminaddpolice")
    return render(request,"adminpolice.html",{"msg":msg,"police":police})


def adminaddlabor(request):
    """ 
        The function to add labors
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    police=Policestation.objects.all()
    if(request.POST):
        name=request.POST["Name"]
        address=request.POST["Address"]
        place=request.POST["Place"]
        id1=request.POST["Id1"]
        id2=request.POST["Id2"]
        phone=request.POST["Phone"]
        aadhar=request.POST["Aadhar"]
        work=request.POST["work"]    
        img=request.FILES["Photo"]
        sign=request.FILES["Sign"]
        afile=request.FILES["Afile"]
        height=request.POST["Height"]
        weight=request.POST["Weight"]
        color=request.POST["Color"]
        disease=request.POST["Disease"]
        station=request.POST["station"]
        pl=Policestation.objects.get(id=station)
        try:
            s=Labourreg.objects.get(aadhar=aadhar)
        except:
            s=None
        if s is None:
            try:
                r = Labourreg.objects.create(
                    name=name,pid=pl,address=address,place=place,idmark1=id1,idmark2=id2,contact=phone,aadhar=aadhar,aadharfile=afile,color=color,photo=img,disease=disease,sign=sign,status='registered',height=height,weight=weight)
                r.save
            except:
                messages.info(request,'Some Error Occured')
            else:
                messages.info(request,'Labour Registered Successfully')
                return redirect("/adminaddlabor")
        else:
             messages.info(request,'Already Registered')
             return redirect("/adminaddlabor")

    return render(request,"adminlabor.html",{"msg":msg,"police":police})

def login(request):
    """ 
        The function to check login process 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        email=request.POST.get("Email")
        pwd=request.POST.get("Password")
        s=User.objects.get(username=email)
        user = authenticate(username=email, password=pwd)
        print(s.username)
        print(s.password)
        print(user)
        if user is None:
            messages.info(request,'Invalid Username and Password')
        else:
            s=User.objects.get(username=email)
            if s.is_superuser == 1:
                if email == "admin@gmail.com":
                    return redirect("/adminhome")
                else:
                    messages.info(request, 'Something went Wrong')
                    return redirect("/login")
            else:
                if s.is_staff == 0:
                        r = Usertypes.objects.get(logid=s.id)
                        if r.utype == 'user':
                            us=Userreg.objects.get(email=email)
                            request.session["id"] = us.id
                            request.session["name"] = us.name
                            return redirect("/userhome") 
                        elif r.utype == 'contractor':
                            us=Contractorreg.objects.get(email=email)
                            request.session["id"] = us.id
                            request.session["name"] = us.name
                            return redirect("/contractorhome")
                        elif r.utype == 'police':
                            us=Policestation.objects.get(email=email)
                            request.session["id"] = us.id
                            request.session["name"] = us.pname
                            return redirect("/policehome")
                        else:
                            messages.info(request, 'Something went Wrong')
                        return redirect("/login")
                else:
                        messages.info(request, 'Something went Wrong')
                        return redirect("/login")


    return render(request,"index.html",{"msg":msg})

def admincontractorrequest(request):
    """ 
        The function to load contractors for approval 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    k=Usertypes.objects.filter(utype='contractor')
    s=Contractorreg.objects.all()
    
    return render(request,"admincontractorsforapproval.html",{"data":k,"data1":s})

def adminapprovecontractor(request):
    """ 
        The function to approve or reject contractors by admin
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    cid=request.GET.get("id")
    try:
        User.objects.filter(id=cid).update(is_active=1)
    except:
        print("shit")
        messages.info(request, 'Something went Wrong')
        return redirect("/admincontractorrequest")
    else:
        print("wow")
        messages.info(request, 'Success')
        return redirect("/admincontractorrequest")

def adminviewreglabors(request):

    
    """ 
        The function to load all registered labors 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            labor details
    """
    # s="select * from tbllabour where labId not in(select labId from tblglobalid)"
    # c.execute(s)
    # data=c.fetchall()
    s=Globalid.objects.all().values('labid')
    data=Labourreg.objects.exclude(id__in=s)
    return render(request,"adminviewreglabor.html",{"data":data})

def adminviewlabordetails(request):

    
    """ 
        The function to load details of a particular registered labors 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            labor details
    """
    lid=request.GET.get("id")
    data=Labourreg.objects.get(id=lid)
    return render(request,"adminviewreglabordetails.html",{"d":data})

def adminlaborwithnoc(request):

    
    """ 
        The function to load details of labors with noc
        --------------------------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            labor details
    """
    
    s=Globalid.objects.all().values('labid')
    data=Labourreg.objects.filter(status='approved').exclude(id__in=s)
    return render(request,"adminlaborwithnoc.html",{"data":data})

#####
def adminlaborrequest(request):

    
    """ 
        The function to approve labor request
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            labor details
    """
    data=Labourrequest.objects.filter(status='requested')
    return render(request,"adminlaborrequest.html",{"data":data})


def admingeneratecard(request):

    
        """ 
            The function to generate job card
            --------------------------------------------------------------
            Parameters: 
                HTTP request 
            
            Returns: 
                html page
        """
        lid=request.GET.get("id")
        l=Labourreg.objects.get(id=lid)
        try:
            s=Globalid.objects.create(labid=l,status='active')
        except:
            messages.info(request, 'Sorry some error occured')
        else:
            messages.info(request, 'Id Generated')
            res = Globalid.objects.filter().aggregate(max_id=Max('id'))
            count=res.get('max_id')
            request.session["gid"]=count
            return redirect("/jobcard")
    
        return render(request,"adminlaborwithnoc.html")

def jobcard(request):

    
    """ 
        The function to print job card
        --------------------------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    gid=request.session["gid"]
    i=Globalid.objects.get(id=gid)
    return render(request,"jobcard.html",{"d":i})

def adminapproverequest(request):

    
    """ 
        The function to approve labor request
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            labor details
    """
    reqid=request.GET.get("id")
    status=request.GET.get("status")
    Labourrequest.objects.filter(id=reqid).update(status=status)
    if status == 'Approved':
        d=Labourrequest.objects.filter(id=reqid).values('conid','lid')
        for a in d:
            conid=a['conid']
            lid=a['lid']
        c=Contractorreg.objects.get(id=conid)
        Labourreg.objects.filter(id=lid).update(cid=c)
        messages.info(request,'Approved Successfully')
    return redirect("/adminlaborrequest")

def policeviewreglabors(request):

    
    """ 
        The function to load all registered labors for police
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            labor details
    """
    id=request.session["id"]
    s=Globalid.objects.all().values('labid')
    data=Labourreg.objects.filter(status='registered',pid=id).exclude(id__in=s)
    return render(request,"policelabor.html",{"data":data})

def policeviewlabordetails(request):

    
    """ 
        The function to load details of a particular registered labors 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            labor details
    """
    lid=request.GET.get("id")
    data=Labourreg.objects.get(id=lid)
    return render(request,"policeviewreglabordetails.html",{"d":data})

def policeapprovelabors(request):

    
    """ 
        The function to approve or reject registered labors 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            Html page
    """
    lid=request.GET.get("id")
    status=request.GET.get("status")
    try:
        Labourreg.objects.filter(id=lid).update(status=status)
    except:
        messages.info(request,'some error occured')
    else:
        messages.info(request,'Status Updated')
        return redirect("/policeviewreglabors")
    return render(request,"policeviewreglabordetails.html")


def policeviewcomplaint(request):

    
    """ 
        The function to load all complaints for police
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            complaint details
    """
    id=request.session["id"]
    data=Complaint.objects.filter(pid=id)
    return render(request,"policeviewcomplaint.html",{"data":data})

def policesearchsimilarlabor(request):

    
    """ 
        The function to load search result for complaints
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            labor details
    """
    height=request.GET.get("height")
    h1=int(height)-10
    h2=int(height)+10
    
    weight=request.GET.get("weight")
    w1=int(weight)-10
    w2=int(weight)+10
    s=Labourreg.objects.filter(height__gte=h1,height__lte=h2,weight__gte=w1,weight__lte=w2)
    data=Globalid.objects.filter(labid__in=s)
    return render(request,"policesearchsimilarlabor.html",{"data":data})

def policeworkdetails(request):

    
    """ 
        The function to load search result for complaints
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            complaint details
    """
    lid=request.GET.get("id")
    data=Worklabors.objects.filter(glid=lid)
    return render(request,"policeworkdetails.html",{"data":data})


def userworkrequest(request):

    """ 
        The function to load work request page for user . 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """  
    id=request.session["id"]
    uid=Userreg.objects.get(id=id)
    if(request.POST):
        work=request.POST["Work"]
        wdate=request.POST["Wdate"]
        place=request.POST["Place"]
        l1=request.POST["l1"]
        l2=request.POST["l2"]
        try:
            s=Tender.objects.create(uid=uid,reqdesc=work,reqdate=wdate,place=place,lat=l1,lon=l2,status='requested')
            s.save
        except:
            messages.info(request,'some error occured')
        else:
            messages.info(request,'Data updated successfully')
    return render(request,"userrequest.html")

def usertendercalls(request):

    
    """ 
        The function to load all tender calls for users 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    id=request.session["id"]
    # s="select tbltendercall.*,tbltender.reqDescription,tblcontractor.conName,conPhone from tbltender,tbltendercall,tblcontractor where tbltendercall.conEmail=tblcontractor.conEmail and tbltender.reqId=tbltendercall.reqId and tbltender.reqStatus='requested' and tbltender.uEmail='"+email+"'"
    # c.execute(s)
    data=Tendercall.objects.filter(reqid__uid=id,reqid__status='requested')
    return render(request,"usertendercalls.html",{"data":data})


def userapprovetender(request):    
    """ 
        The function to approve tender calls for users 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    tid=request.GET.get("id")
    
    s=Tendercall.objects.get(id=tid)
 
    try:
        Tendercall.objects.filter(id=tid).update(status='accepted')
    except:
        messages.info(request,'some error occured')
        return redirect("/usertendercalls")
    else:
        # s="update tbltendercall set tenStatus='rejected' where tcId<>'"+str(tid)+"' and reqId ='"+str(reqid)+"'"
        try:
            Tendercall.objects.filter(reqid=s.reqid).exclude(id=tid).update(status='rejected')
        except:
            messages.info(request,'some error occured')
            return redirect("/usertendercalls")
        else:
            # s="update tbltender set reqStatus='set' where reqId ='"+str(reqid)+"'"
            try:
              Tender.objects.filter(id=s.reqid.id).update(status='set')  
            except:
                messages.info(request,'some error occured')
                return redirect("/usertendercalls")
            else:
                
                # s="insert into tblworkdetails (tcId,workAmt,wSdate,wEdate,wStatus) values('"+str(tid)+"','"+str(tenAmt)+"','"+str(sDate)+"','"+str(eDate)+"','commited')"
                try:
                  w=Workdetails.objects.create(tcid=s,wrkamount=s.amount,wsdate=s.sdate,wedate=s.edate,status='commited')
                  w.save
                except:
                    # msg="Sorry some error occured"
                    return redirect("/usertendercalls")
                else:
                    return redirect("/userwork")

def userwork(request):

    """ 
        The function to load all work for users 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    id=request.session["id"]
    # s="select tblworkdetails.wSdate,tblworkdetails.wEdate,tblworkdetails.workAmt,tblworkdetails.wStatus,tbltender.reqDescription,tblcontractor.conName,tblcontractor.conPhone,tblworkdetails.workId from tbltender,tbltendercall,tblcontractor,tblworkdetails where tbltendercall.conEmail=tblcontractor.conEmail and tbltender.reqId=tbltendercall.reqId and tbltender.uEmail='"+email+"' and tblworkdetails.tcId=tbltendercall.tcId"
    data=Workdetails.objects.filter(tcid__reqid__uid=id).exclude(status__in=['Completed','Paid'])
    return render(request,"userwork.html",{"data":data})

########
def userviewlabors(request):
    """ 
        The function to load all workers for a work 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    wid=request.GET.get("id")
    # s="select tbllabour.labName,tbllabour.labPhoto,tblworklabors.globalId from tbllabour,tblglobalid,tblworklabors where tbllabour.labId=tblglobalid.labId and tblworklabors.globalid=tblglobalid.globalId and tblworklabors.workId='"+wid+"'"
    # c.execute(s)
    data=Worklabors.objects.filter(wrkid=wid)
    return render(request,"userviewlabors.html",{"data":data})


def usercompletedwork(request):

    
    """ 
        The function to view completed work details of users 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            labor details
    """
    id=request.session["id"]
    # s="select tblworkdetails.wSdate,tblworkdetails.wEdate,tblworkdetails.workAmt,tblworkdetails.wStatus,tbltender.reqDescription,tblcontractor.conName,tblcontractor.conPhone,tblworkdetails.workId from tbltender,tbltendercall,tblcontractor,tblworkdetails where tbltendercall.conEmail=tblcontractor.conEmail and tbltender.reqId=tbltendercall.reqId and tbltender.uEmail='"+email+"' and tblworkdetails.tcId=tbltendercall.tcId and tblworkdetails.wStatus='Completed'"
    # c.execute(s)
    data=Workdetails.objects.filter(tcid__reqid__uid=id,status__in=['Completed','Paid'])
    return render(request,"usercompletedwork.html",{"data":data})

def usercomplaint(request):
    """ 
        The function to add complaint for user. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    uid=request.session["id"]
    comp=Complaint.objects.filter(uid=uid)
    police=Policestation.objects.all()
    if(request.POST):
        uid=request.session["id"]
        us=Userreg.objects.get(id=uid)
        pol=request.POST["Police"]
        pl=Policestation.objects.get(id=pol)
        complaint=request.POST["Complaint"]
        height=request.POST["Height"]
        weight=request.POST["Weight"]
        place=request.POST["Place"]
        l1=request.POST["l1"]
        l2=request.POST["l2"]
        # s="insert into tblcomplaint(uEmail,pEmail,compDetails,culpritHeight,culpritWeight,compPlace,compLat,compLon,compStatus) values('"+email+"','"+pol+"','"+complaint+"','"+height+"','"+weight+"','"+place+"','"+l1+"','"+l2+"','Submitted')"
        try:
            c=Complaint.objects.create(uid=us,pid=pl,complaint=complaint,status='submitted',clheight=height,clweight=weight,place=place,lat=l1,lon=l2)
            c.save
        except:
            messages.info(request,'some error occured')
        else:
            messages.info(request,'complaint added successfully')
        
    return render(request,"usercomplaint.html",{"police":police,"comp":comp})


def contractorviewlabors(request):  
    """ 
        The function to load all labors for contractors
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            labor details
    """
    id=request.session["id"]
    # s="select tbllabour.*,tblglobalid.* from tbllabour,tblglobalid where tbllabour.conEmail='"+email+"' and tbllabour.labId=tblglobalid.labId"
    # c.execute(s)
    data=Labourreg.objects.filter(cid=id)
    return render(request,"contrctorviewlabor.html",{"data":data})

def contractorviewlabordetails(request):

    
    """ 
        The function to load details of a particular registered labors 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            labor details
    """
    lid=request.GET.get("id")
    # s="select tbllabour.*,tblglobalid.* from tbllabour,tblglobalid where tbllabour.labId='"+lid+"' and tbllabour.labId=tblglobalid.labId"
    # c.execute(s)
    data=Labourreg.objects.filter(id=lid)
    return render(request,"contractorviewlabordetails.html",{"data":data})

def contractorrequestlabor(request):

    
    """ 
        The function to request labor for contractors
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            labor details
    """
    id=request.session["id"]
    # s="select tbllabour.*,tblglobalid.* from tbllabour,tblglobalid where tbllabour.conEmail is null and tbllabour.labId=tblglobalid.labId"
    # c.execute(s)
    data=Labourreg.objects.filter(cid__isnull=True)
    return render(request,"contractorrequestlabor.html",{"data":data})

def contractorrequest(request):

    
    """ 
        The function to add labor request for contractors
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            labor details
    """
    id=request.session["id"]
    lid=request.GET.get("id")
    lab=Labourreg.objects.get(id=lid)
    con=Contractorreg.objects.get(id=id)
    # qry=f"insert into tbllaborrequest (labId,cEmail,reqDate,status) values('{lid}','{email}',(select sysdate()),'Requested')"
    c=Labourrequest.objects.create(lid=lab,conid=con,status='requested')
    return redirect("/contractorlabrequest")

def contractorlabrequest(request):

    
    """ 
        The function to request labor for contractors
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            labor details
    """
    id=request.session["id"]
    # s=f"select tbllabour.*,tbllaborrequest.reqDate,tbllaborrequest.status from tbllabour,tblglobalid,tbllaborrequest where tbllabour.labId=tbllaborrequest.labId and tbllabour.labId=tblglobalid.labId and tbllaborrequest.cEmail='{email}'"
    # c.execute(s)
    data=Labourrequest.objects.filter(conid=id)
    return render(request,"contractorlabrequest.html",{"data":data})

def contractorworkrequest(request):

    
    """ 
        The function to load work request for contractors 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            labor details
    """
    
    # s="select tbltender.*,tbluser.uName from tbltender,tbluser where tbltender.uEmail=tbluser.uEmail and tbltender.reqStatus='requested'"
    # c.execute(s)
    data=Tender.objects.filter(status='requested')
    return render(request,"contractorworkrequest.html",{"data":data})

def contractorviewworkplace(request):

    
    """ 
        The function to load work place for contractors 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            labor details
    """
    wid=request.GET.get("id")
    # s="select reqLat,reqLon from tbltender where reqId='"+wid+"'"
    # c.execute(s)
    d=Tender.objects.get(id=wid)
    return render(request,"contractorviewworkplace.html",{"d":d})

def contractoraddtender(request):

    
    """ 
        The function to add tender call for contractors 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            labor details
    """
    msg=""
    reqid=request.GET.get("id")
    id=request.session["id"]
    # s="select tenAmt from tbltendercall where reqId='"+reqid+"'"
    # c.execute(s)
    data=Tendercall.objects.filter(reqid=reqid)
    ten=Tender.objects.get(id=reqid)
    con=Contractorreg.objects.get(id=id)
    if(request.POST):
        amt=request.POST["Amount"]
        sdate=request.POST["Sdate"]
        edate=request.POST["Edate"]
        tender=request.POST["Tender"]
        # s="insert into tbltendercall (reqId,conEmail,tenAmt,tenSdate,tenEdate,tenDescription,tenStatus) values('"+reqid+"','"+email+"','"+amt+"','"+sdate+"','"+edate+"','"+tender+"','submitted')"
        try:
            c=Tendercall.objects.create(reqid=ten,conid=con,amount=amt,desc=tender,sdate=sdate,edate=edate,status='submitted')
            c.save
        except:
            messages.info(request,"some error occured")
        else:
            messages.info(request,"Tender Call Added Successfully")
    return render(request,"contractoraddtender.html",{"data":data})

def contractorwork(request):
    """ 
        The function to view work details of contractors 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            labor details
    """
    id=request.session["id"]
    # s="select tblworkdetails.wSdate,tblworkdetails.wEdate,tblworkdetails.workAmt,tblworkdetails.wStatus,tbltender.reqDescription,tbluser.uName,tbluser.uContact,tblworkdetails.workId from tbltender,tbltendercall,tbluser,tblworkdetails where tbltender.uEmail=tbluser.uEmail and tbltender.reqId=tbltendercall.reqId and tbltendercall.conEmail='"+email+"' and tblworkdetails.tcId=tbltendercall.tcId and tblworkdetails.wStatus<>'Completed'"
    # c.execute(s)
    data=Workdetails.objects.filter(tcid__conid=id).exclude(status='Completed')
    return render(request,"contractorwork.html",{"data":data})

def contractoraddlabors(request):

    
    """ 
        The function to add labours for a work by contractor
        --------------------------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            labor details
    """
    msg=""
    id=request.session["id"]
    wid=request.GET.get("id")
    wrkid=Workdetails.objects.get(id=wid)
    # s="select tbllabour.labName,tbllabour.labPhoto,tblworklabors.globalId from tbllabour,tblglobalid,tblworklabors where tbllabour.labId=tblglobalid.labId and tblworklabors.globalid=tblglobalid.globalId and tblworklabors.workId='"+wid+"'"
    # c.execute(s)
    data=Worklabors.objects.filter(wrkid=wid)
    # s="select tblglobalid.globalid,tbllabour.labName from tbllabour,tblglobalid where tbllabour.conEmail='"+email+"' and tbllabour.labId=tblglobalid.labId and tblglobalid.globalId not in(select globalId from tblworklabors where workId='"+wid+"')"
    c=Worklabors.objects.filter(wrkid=wid).values('glid')
    labors=Globalid.objects.filter(labid__cid=id).exclude(id__in=c)
    if(request.POST):
        gid=request.POST["GID"]
        glid=Globalid.objects.get(id=gid)
        # s="insert into tblworklabors (workId,globalId) values('"+wid+"','"+gid+"')"
        try:
            b=Worklabors.objects.create(wrkid=wrkid,glid=glid)
        except:
            messages.info(request,'sorry some error occured')
        else:
            messages.info(request,'Labour added Successfully')
            return redirect("/contractorwork")
    return render(request,"contractoraddlabors.html",{"data":data,"labors":labors})

def contractorupdatework(request):

    
    """ 
        The function to add update details of a work by contractor
        --------------------------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            labor details
    """
    msg=""
    wid=request.GET.get("id")
    # s="select * from tblworkdetails where workId='"+wid+"'"
    # c.execute(s)
    data=Workdetails.objects.filter(id=wid)
    if(request.POST):
        amt=request.POST["Amount"]
        # sdate=request.POST["Sdate"]
        edate=request.POST["Edate"]
        status=request.POST["Status"]
        # s="update tblWorkdetails set workAmt='"+amt+"', wEdate='"+edate+"',wStatus='"+status+"' where workId='"+wid+"'"
        try:
            Workdetails.objects.filter(id=wid).update(wrkamount=amt,wedate=edate,status=status)
        except:
            messages.info(request,'sorry some error occured')
        else:
            messages.info(request,'Details updated successfully')
            return redirect("/contractorwork")
    return render(request,"contractorupdatework.html",{"data":data,"msg":msg})

def contractorcompletedwork(request):

    
    """ 
        The function to view completed work details of contractors 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            labor details
    """
    id=request.session["id"]
    # s="select tblworkdetails.wSdate,tblworkdetails.wEdate,tblworkdetails.workAmt,tblworkdetails.wStatus,tbltender.reqDescription,tbluser.uName,tbluser.uContact,tblworkdetails.workId from tbltender,tbltendercall,tbluser,tblworkdetails where tbltender.uEmail=tbluser.uEmail and tbltender.reqId=tbltendercall.reqId and tbltendercall.conEmail='"+email+"' and tblworkdetails.tcId=tbltendercall.tcId and (tblworkdetails.wStatus='Completed' or tblworkdetails.wStatus='Incomplete')"
    # c.execute(s)
    data=Workdetails.objects.filter(tcid__conid=id,status__in=['Completed','Paid'])
    return render(request,"contractorcompletedwork.html",{"data":data})

def policeupdatecomplaint(request):

    
    """ 
        The function to add complaint update details
        --------------------------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            labor details
    """
    msg=""
    cid=request.GET.get("id")
    data=Complaint.objects.get(id=cid)
    if(request.POST):
        reply=request.POST["reply"]
        status=request.POST["Status"]
        # s="update tblWorkdetails set workAmt='"+amt+"', wEdate='"+edate+"',wStatus='"+status+"' where workId='"+wid+"'"
        try:
            
            Complaint.objects.filter(id=cid).update(reply=reply,status=status)
        
        except:
            messages.info(request,'sorry some error occured')
        else:
            messages.info(request,'Complaint updated successfully')
            return redirect("/policeviewcomplaint")
    return render(request,"policeupdatecomplaint.html",{"data":data})

def addpayment(request):

    
    """ 
        The function to add payment
        --------------------------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            labor details
    """
    msg=""
    cid=request.GET.get("id")
    data=Workdetails.objects.get(id=cid)
    if(request.POST):
        year=request.POST["year"]
        if(int(year)<2023 or int(year)>2032):
            messages.info(request,'invalid year')
            return redirect("/usercompletedwork")
        try:    
            Workdetails.objects.filter(id=cid).update(status='Paid')
        
        except:
            messages.info(request,'sorry some error occured')
        else:
            messages.info(request,'Paid Successfully')
            return redirect("/usercompletedwork")
    return render(request,"addpayment.html",{"data":data})


def adminupdatepolice(request):
    """ 
        The function to add labors
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    id=request.GET.get('id')
    police=Policestation.objects.get(id=id)
    if(request.POST):
        name=request.POST["Name"]
        address=request.POST["address"]
        stationcode=request.POST["StationCode"]
        circle=request.POST["Circle"]
        phone=request.POST["Phone"]
        status=request.POST["status"]
        try:
            Policestation.objects.filter(id=id).update(
                pscode=stationcode,pname=name,address=address,circle=circle,contact=phone)
        except:
            messages.info(request,'Sorry something went wrong')
            return redirect("/adminaddpolice")
        else:
            User.objects.filter(email=police.email).update(is_active=status)
            messages.info(request,'Updated Successfully')
            return redirect("/adminaddpolice")
    return render(request,"adminupdatepolice.html",{"msg":msg,"p":police})

def contractorprofile(request):
    """ 
        The function to register contractor
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    id=request.session['id']
    con=Contractorreg.objects.get(id=id)
    if(request.POST):
        name=request.POST["Name"]
        address=request.POST["address"]
        licenseno=request.POST["License"]
        phone=request.POST["Contact"]
        try:
            Contractorreg.objects.filter(id=id).update(
                name=name,address=address,phone=phone,license=licenseno)
        except:
            messages.info(request,'Something Went wrong')
            return redirect("/contractorprofile")
        else:
            messages.info(request,'Profile Updated Successfully')
            return redirect("/contractorprofile")
            
    return render(request,"contractorprofile.html",{"msg":msg,'c':con})

def updatelabourdetails(request):
    """ 
        The function to add labors
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    id=request.GET.get("id")
    labor=Labourreg.objects.get(id=id)
    police=Policestation.objects.all()
    if(request.POST):
        name=request.POST["Name"]
        address=request.POST["Address"]
        place=request.POST["Place"]
        phone=request.POST["Phone"]
        station=request.POST["station"]
        pl=Policestation.objects.get(id=station)
        try:
            r = Labourreg.objects.filter(id=id).update(
                name=name,pid=pl,address=address,place=place,contact=phone)
            
        except:
            messages.info(request,'Some Error Occured')
            return redirect("/contractorviewlabors")
        else:
            messages.info(request,'Updated Successfully')
            return redirect("/contractorviewlabors")

    return render(request,"updatelabourdetails.html",{"msg":msg,"police":police,"l":labor})


def userprofile(request):
    """ 
        The function to register user
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    id=request.session['id']
    us=Userreg.objects.get(id=id)
    if(request.POST):
        name=request.POST["Name"]
        phone=request.POST["Contact"]
        try:
            Userreg.objects.filter(id=id).update(
                name=name,contact=phone)
        except:
            messages.info(request, 'Sorry some error occured')
            return redirect("/userprofile")
        else:
            messages.info(request,'Updated Successfully')
            return redirect("/userprofile") 
               
    return render(request,"userprofile.html",{"msg":msg,'us':us})


def adminviewalllabor(request):

    
    """ 
        The function to load all registered labors 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            labor details
    """
    data=Labourreg.objects.all()
    return render(request,"adminviewalllabors.html",{"data":data})

def adminviewalluser(request):

    
    """ 
        The function to load all registered labors 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            labor details
    """
    data=Userreg.objects.all()
    return render(request,"adminviewalluser.html",{"data":data})



