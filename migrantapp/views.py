from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import pymysql
import cv2

db = pymysql.connect(host="localhost", user="root",
                     password="", database="dbmigrants")
c = db.cursor()

######################################################################
#                           LOAD INDEX PAGE
######################################################################


def index(request):
    """ 
        The function to load index page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    return render(request, "index.html")

######################################################################
#                           LOGIN PROCESS
######################################################################


def login(request):
    """ 
        The function to check login process 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        email = request.POST.get("Email")
        pwd = request.POST.get("Password")
        s = "select count(*) from tbllogin where username='"+email+"'"
        c.execute(s)
        i = c.fetchone()
        if(i[0] > 0):
            s = "select * from tbllogin where username='"+email+"'"
            c.execute(s)
            i = c.fetchone()
            if(i[1] == pwd):
                request.session['email'] = email
                if(i[3] == "1"):
                    if(i[2] == "admin"):
                        return HttpResponseRedirect("/adminhome")
                    elif(i[2] == "police"):
                        return HttpResponseRedirect("/policehome")
                    elif(i[2] == "contractor"):
                        return HttpResponseRedirect("/contractorhome")
                    elif(i[2] == "user"):
                        return HttpResponseRedirect("/userhome")
                else:
                    msg = "You are not authenticated to login"
            else:
                msg = "Incorrect password"
        else:
            msg = "User doesnt exist"
    return render(request, "index.html", {"msg": msg})

######################################################################
#                           LOAD ADMIN PAGE
######################################################################


def adminhome(request):
    """ 
        The function to load admin home page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    return render(request, "adminhome.html")
######################################################################
#                           LOAD ALL POLICE STATION
######################################################################


def viewpolice():
    """ 
        The function to load all registered police 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            police details
    """
    db.commit()
    s = "select * from tblpolicestation where pEmail in(select username from tbllogin where status='1')"
    c.execute(s)
    data = c.fetchall()
    return data
######################################################################
#                           ADD POLICE
######################################################################


def adminaddpolice(request):
    """ 
        The function to add labors
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    police = viewpolice()
    if(request.POST):
        name = request.POST["Name"]
        address = request.POST["address"]
        stationcode = request.POST["StationCode"]
        circle = request.POST["Circle"]
        email = request.POST["Email"]
        phone = request.POST["Phone"]

        s = "select count(*) from tbllogin where username='"+email+"'"
        c.execute(s)
        i = c.fetchone()
        if(i[0] > 0):
            msg = "Email already registered"
        else:
            s = "insert into tblpolicestation (pName,pStationCode,pAddress,pCircle,pContact,pEmail) values('" + \
                name+"','"+stationcode+"','"+address+"','"+circle+"','"+phone+"','"+email+"')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg = "Sorry registration error"
            else:
                s = "insert into tbllogin (username,password,utype,status) values('" + \
                    email+"','"+email+"','police','1')"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    msg = "Sorry login process error"
                else:
                    msg = "Police registered successfully"
    return render(request, "adminpolice.html", {"msg": msg, "police": police})
######################################################################
#                           DELETE POLICE STATION
######################################################################


def deletepolice(request):
    """ 
        The function to delete police 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            HTML page
    """
    email = request.GET.get("id")
    s = "update tbllogin set status='0' where username='"+email+"'"
    try:
        c.execute(s)
        db.commit
    except:
        msg = "Sorry some error occured"
    else:
        msg = "Account deleted"
    police = viewpolice()
    return render(request, "adminpolice.html", {"msg": msg, "police": police})
######################################################################
#                           CONTRACTORS FOR APPROVAL
######################################################################


def admincontractorrequest(request):
    """ 
        The function to load contractors for approval 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    data = adminselectcontractorrequest()
    data1 = adminselectcontractor()
    return render(request, "admincontractorsforapproval.html", {"data": data, "data1": data1})
######################################################################
#                           SELECT CONTRACTORS FOR APPROVAL
######################################################################


def adminselectcontractorrequest():
    """ 
        The function to load contractors for approval 
        -----------------------------------------------
        Parameters: 


        Returns: 
            contractor details
    """
    s = "select * from tblcontractor where conEmail in(select username from tbllogin where status='0')"
    c.execute(s)
    data = c.fetchall()
    return data
######################################################################
#                           SELECT CONTRACTORS FOR APPROVAL
######################################################################


def adminselectcontractor():
    """ 
        The function to load contractors for approval 
        -----------------------------------------------
        Parameters: 


        Returns: 
            contractor details
    """
    s = "select * from tblcontractor where conEmail in(select username from tbllogin where status='1')"
    c.execute(s)
    data = c.fetchall()
    return data
######################################################################
#                           APPROVE OR REJECT CONTRACTOR
######################################################################


def adminapprovecontractor(request):
    """ 
        The function to approve or reject contractors by admin
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    cid = request.GET.get("id")
    status = request.GET.get("status")
    s = "update tbllogin set status='"+status+"' where username='"+cid+"'"
    try:
        c.execute(s)
        db.commit()
    except:
        return HttpResponseRedirect("/admincontractorrequest")
    else:
        return HttpResponseRedirect("/admincontractorrequest")


######################################################################
#                           ADD LABOUR
######################################################################
def adminaddlabor(request):
    """ 
        The function to add labors
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    police = viewpolice()
    if(request.POST):
        name = request.POST["Name"]
        address = request.POST["Address"]
        place = request.POST["Place"]
        id1 = request.POST["Id1"]
        id2 = request.POST["Id2"]
        phone = request.POST["Phone"]
        aadhar = request.POST["Aadhar"]
        work = request.POST["work"]

        img = request.FILES["Photo"]
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        uploaded_file_url = fs.url(filename)

        sign = request.FILES["Sign"]
        fs1 = FileSystemStorage()
        filename1 = fs1.save(sign.name, sign)
        uploaded_file_url1 = fs1.url(filename1)

        afile = request.FILES["Afile"]
        fs2 = FileSystemStorage()
        filename2 = fs2.save(afile.name, afile)
        uploaded_file_url2 = fs2.url(filename2)

        height = request.POST["Height"]
        weight = request.POST["Weight"]
        color = request.POST["Color"]
        disease = request.POST["Disease"]
        station = request.POST["Station"]
        s = "select count(*) from tbllabour where labAadhar='"+aadhar+"'"
        c.execute(s)
        i = c.fetchone()
        if(i[0] > 0):
            msg = "Aadhar already registered"
        else:
            s = "insert into tbllabour (pEmail,labName,labAddress,labPlace,labIdMark1,labIdMark2,labPhone,labAadhar,labPhoto,labHeight,labWeight,labColor,labDisease,status,signature,aadharfile,work) values('"+station+"','"+name+"','" + \
                address+"','"+place+"','"+id1+"','"+id2+"','"+phone+"','"+aadhar+"','"+uploaded_file_url+"','"+height+"','" + \
                weight+"','"+color+"','"+disease+"','registered','" + \
                uploaded_file_url1+"','"+uploaded_file_url2+"','"+work+"')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg = "Sorry some error occured"
            else:
                msg = "Labor registered successfully"
    return render(request, "adminlabor.html", {"msg": msg, "police": police})
######################################################################
#                           LOAD ALL REGISTERED LABORS
######################################################################


def adminviewreglabors(request):
    """ 
        The function to load all registered labors 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            labor details
    """
    s = "select * from tbllabour where labId not in(select labId from tblglobalid)"
    c.execute(s)
    data = c.fetchall()
    return render(request, "adminviewreglabor.html", {"data": data})
######################################################################
#                           LOAD ALL REGISTERED LABORS
######################################################################


def adminviewlabordetails(request):
    """ 
        The function to load details of a particular registered labors 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            labor details
    """
    lid = request.GET.get("id")
    s = "select tbllabour.*,tblpolicestation.pName from tbllabour,tblpolicestation where tbllabour.labId ='" + \
        lid+"' and tbllabour.pEmail=tblpolicestation.pEmail"
    c.execute(s)
    data = c.fetchall()
    return render(request, "adminviewreglabordetails.html", {"data": data})
######################################################################
#                           LOAD LABORS WITH NOC
######################################################################


def adminlaborwithnoc(request):
    """ 
        The function to load details of labors with noc
        --------------------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            labor details
    """
    s = "select * from tbllabour where status='approved' and labId not in(select labId from tblglobalid)"
    c.execute(s)
    data = c.fetchall()
    return render(request, "adminlaborwithnoc.html", {"data": data})
######################################################################
#                           LOAD LABORS WITH NOC
######################################################################


def adminchoosecontractor(request):
    """ 
        The function to load details of labors with noc
        --------------------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            labor details
    """
    lid = request.GET.get("id")
    request.session["lid"] = lid
    data = adminselectcontractor()
    return render(request, "adminchoosecontractor.html", {"data": data})
######################################################################
#                           GENRATE JOB CARD
######################################################################


def admingeneratecard(request):
    """ 
        The function to generate job card
        --------------------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    lid = request.session["lid"]
    cont = request.POST["contractor"]
    s = "update tbllabour set conEmail='"+cont+"' where labId='"+lid+"'"
    try:
        c.execute(s)
        db.commit()
    except:
        msg = "Sorry  error occured"
    else:
        s = "insert into tblglobalid (labId,dateIssue,idStatus) values('" + \
            str(lid)+"',(select sysdate()),'active')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Sorry some error occured"
        else:
            msg = "ID generated"
            s = "select max(globalid) from tblglobalid"
            c.execute(s)
            i = c.fetchone()
            count = i[0]
            request.session["gid"] = count
            return HttpResponseRedirect("/jobcard")

    return render(request, "adminlaborwithnoc.html", {"msg": msg})
######################################################################
#                           JOB CARD
######################################################################


def jobcard(request):
    """ 
        The function to print job card
        --------------------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    gid = request.session["gid"]
    s = "select tbllabour.*,tblglobalid.globalId,tblcontractor.conName,tblcontractor.conPhone from tbllabour,tblcontractor,tblglobalid where tbllabour.labId=tblglobalid.labId and tblcontractor.conEmail=tbllabour.conEmail and tblglobalid.globalId='" + \
        str(gid)+"'"
    print(s)
    c.execute(s)
    i = c.fetchall()
    return render(request, "jobcard.html", {"data": i})
######################################################################
#                           ADMIN SEARCH LABOR BY GID
######################################################################


def adminsearchlabor(request):
    """ 
        The function to search labor by global id
        --------------------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    if(request.POST):
        gid = request.POST["Gid"]
        request.session["gid"] = gid
        return HttpResponseRedirect("/jobcard")
    return render(request, "adminsearchlabor.html")
######################################################################
#                           LOAD POLICE PAGE
######################################################################


def policehome(request):
    """ 
        The function to load police home page . 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    email = request.session["email"]
    s = "select * from tblpolicestation where pEmail='"+email+"'"
    c.execute(s)
    data = c.fetchall()
    msg = ""
    if(request.POST):
        name = request.POST["Name"]
        address = request.POST["address"]
        stationcode = request.POST["StationCode"]
        circle = request.POST["Circle"]
        email = request.POST["Email"]
        phone = request.POST["Phone"]

        s = "update tblpolicestation set pName='"+name+"',pStationCode='"+stationcode + \
            "',pAddress='"+address+"',pCircle='"+circle + \
            "',pContact='"+phone+"' where pEmail='"+email+"'"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Sorry some error occured"
        else:
            msg = "Data updated successfully"
    return render(request, "policehome.html", {"details": data, "msg": msg})
######################################################################
#                           CHANGE PASSWORD
######################################################################


def policechangepwd(request):
    """ 
        The function to load index page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        email = request.session["email"]
        current = request.POST["Current"]
        new = request.POST["New"]
        s = "select * from tbllogin where username='"+email+"'"
        c.execute(s)
        i = c.fetchone()
        if(i[1] == current):
            s = "update tbllogin set password='"+new+"' where username='"+email+"'"
            try:
                c.execute(s)
                db.commit()
            except:
                msg = "Sorry some error occured"
            else:
                msg = "Data updated successfully"
        else:
            msg = "Incorrect password"
    return render(request, "policechangepwd.html", {"msg": msg})
######################################################################
#                           LOAD ALL REGISTERED LABORS FOR POLICE
######################################################################


def policeviewreglabors(request):
    """ 
        The function to load all registered labors for police
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            labor details
    """
    email = request.session["email"]
    s = "select * from tbllabour where labId not in(select labId from tblglobalid) and pEmail='" + \
        email+"' and status='registered'"
    c.execute(s)
    data = c.fetchall()
    result = ''
    if "result" in request.GET:
        result = request.GET["result"]
        if result != "unknown":
            qry = f"SELECT person, mid from tblcriminal where mid='{result}'"
            c.execute(qry)
            result = c.fetchone()
        else:
            result = "unknown"
    return render(request, "policelabor.html", {"data": data, "result": result})


def verifylabor(request):
    """ 
        The function to verify labor
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    img = request.GET["img"]
    qry = "SELECT person from tblcriminal"
    c.execute(qry)
    data = c.fetchall()
    from . import facetraining, final
    result = final.fun2(data, img)

    return HttpResponseRedirect(f"/policeviewreglabors?result={result}")


def policeaddcriminals(request):
    """ 
        The function to add criminals
        -----------------------------------------------
        Parameters: 
            HTTP reques(t 

        Returns: 
            html page
    """
    email = request.session["email"]
    msg = ''
    if(request.POST):
        person = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        height = request.POST['height']
        weight = request.POST['weight']
        complex = request.POST['complex']
        place = request.POST['place']
        imark = request.POST['imark']
        phone = request.POST['contactno']
        uname = request.POST['uname']
        casedetails = request.POST['casedetails']

        person_insert = f"INSERT INTO `tblcriminal`(`station`,`person`,`age`,`gender`,`height`,`weight`,`complexion`,`place`,`imark`,`phone`,`uname`,`case`)VALUES('{email}','{person}','{age}','{gender}','{height}','{weight}','{complex}','{place}','{imark}','{phone}','{uname}','{casedetails}')"
        c.execute(person_insert)
        print(person_insert)
        db.commit()

        w = "select max(mid) from tblcriminal "
        c.execute(w)
        data = c.fetchone()
        mid = data[0]
        msg = "Added Successfully"
        from . import fd
        fd.fun(mid)
    return render(request, "policeaddcriminals.html", {"msg": msg})


def policeviewcriminals(request):
    """ 
        The function to view criminals
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    s = "select * from tblcriminal order by mid desc"
    c.execute(s)
    data = c.fetchall()
    return render(request, "policeviewcriminals.html", {"data": data})
######################################################################
#                   LOAD LABOR DETAILS FOR POLICE
######################################################################


def policeviewlabordetails(request):
    """ 
        The function to load details of a particular registered labors 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            labor details
    """
    lid = request.GET.get("id")
    s = "select tbllabour.*,tblpolicestation.pName from tbllabour,tblpolicestation where tbllabour.labId ='" + \
        str(lid)+"' and tbllabour.pEmail=tblpolicestation.pEmail"
    c.execute(s)
    data = c.fetchall()
    return render(request, "policeviewreglabordetails.html", {"data": data})
######################################################################
#                   POLICE APPROVE LABORS
######################################################################


def policeapprovelabors(request):
    """ 
        The function to approve or reject registered labors 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            Html page
    """
    lid = request.GET.get("id")
    status = request.GET.get("status")
    s = "update tbllabour set status='"+status+"' where labId='"+lid+"'"
    try:
        c.execute(s)
        db.commit()
    except:
        msg = "Sorry some error occured"
    else:
        msg = "Status updated"
        return HttpResponseRedirect("policeviewlabordetails")
    return render(request, "policeviewreglabordetails.html", {"msg": msg})
######################################################################
#                      VIEW COMPLAINT FOR POLICE
######################################################################


def policeviewcomplaint(request):
    """ 
        The function to load all complaints for police
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            complaint details
    """
    email = request.session["email"]
    s = "select tblcomplaint.*,tbluser.* from tblcomplaint,tbluser where tblcomplaint.pEmail='" + \
        email+"' and tblcomplaint.uEmail=tbluser.uEmail"
    c.execute(s)
    data = c.fetchall()
    return render(request, "policeviewcomplaint.html", {"data": data})
######################################################################
#                      VIEW COMPLAINT SEARCH RESULT
######################################################################


def policesearchsimilarlabor(request):
    """ 
        The function to load search result for complaints
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            labor details
    """
    height = request.GET.get("height")
    h1 = int(height)-10
    h2 = int(height)+10

    weight = request.GET.get("weight")
    w1 = int(weight)-10
    w2 = int(weight)+10
    s = "select tbllabour.*,tblglobalid.globalId,tblcontractor.conName,tblcontractor.conPhone from tbllabour,tblcontractor,tblglobalid where tbllabour.labId=tblglobalid.labId and tblcontractor.conEmail=tbllabour.conEmail and tbllabour.labHeight between '" + \
        str(h1)+"' and '"+str(h2)+"' and tbllabour.labWeight between '" + \
        str(w1)+"' and '"+str(w2)+"'"
    c.execute(s)
    data = c.fetchall()
    return render(request, "policesearchsimilarlabor.html", {"data": data})
######################################################################
#                      VIEW WORK DETAILS
######################################################################


def policeworkdetails(request):
    """ 
        The function to load search result for complaints
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            complaint details
    """
    lid = request.GET.get("id")
    s = "select tbltender.reqDescription,tbltender.reqPlace,tblworkdetails.wSdate,tblworkdetails.wEdate from tbltender,tbltendercall,tblworkdetails,tblworklabors where tbltender.reqId=tbltendercall.reqId and tbltendercall.tcId=tblworkdetails.tcId and tblworkdetails.workId=tblworklabors.workId and tblworklabors.globalid='"+lid+"'"
    c.execute(s)
    data = c.fetchall()
    return render(request, "policeworkdetails.html", {"data": data})
######################################################################
#                           CONTRACTOR REGISTRATION
######################################################################


def contractorreg(request):
    """ 
        The function to register contractor
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""

    if(request.POST):
        name = request.POST["Name"]
        address = request.POST["address"]
        licenseno = request.POST["License"]
        email = request.POST["Email"]
        phone = request.POST["Contact"]
        pwd = request.POST["Password"]
        img = request.FILES["File"]
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        uploaded_file_url = fs.url(filename)
        s = "select count(*) from tbllogin where username='"+email+"'"
        c.execute(s)
        i = c.fetchone()
        if(i[0] > 0):
            msg = "Email already registered"
        else:
            s = "insert into tblcontractor (conName,conAddress,conPhone,conEmail,conLicense,conCertificate) values('" + \
                name+"','"+address+"','"+phone+"','"+email + \
                "','"+licenseno+"','"+uploaded_file_url+"')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg = s
            else:
                s = "insert into tbllogin (username,password,utype,status) values('" + \
                    email+"','"+pwd+"','contractor','0')"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    msg = "Sorry login process error"
                else:
                    msg = "Registered successfully"
                    return HttpResponseRedirect("/")
    return render(request, "index.html", {"msg": msg})
######################################################################
#                           LOAD CONTRCTOR PAGE
######################################################################


def contractorhome(request):
    """ 
        The function to load contractor home page . 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    email = request.session["email"]
    s = "select * from tblcontractor where conEmail='"+email+"'"
    c.execute(s)
    data = c.fetchall()
    msg = ""
    if(request.POST):
        name = request.POST["Name"]
        address = request.POST["address"]
        clicense = request.POST["License"]
        email = request.POST["Email"]
        phone = request.POST["Phone"]

        s = "update tblcontractor set conName='"+name+"',conLicense='"+clicense + \
            "',conAddress='"+address+"',conPhone='"+phone+"' where conEmail='"+email+"'"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Sorry some error occured"
        else:
            msg = "Data updated successfully"
    return render(request, "contractorhome.html", {"details": data, "msg": msg})
######################################################################
#                           LOAD ALL LABORS FOR CONTRACTOR
######################################################################


def contractorviewlabors(request):
    """ 
        The function to load all labors for contractors
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            labor details
    """
    email = request.session["email"]
    s = "select tbllabour.*,tblglobalid.* from tbllabour,tblglobalid where tbllabour.conEmail='" + \
        email+"' and tbllabour.labId=tblglobalid.labId"
    c.execute(s)
    data = c.fetchall()
    return render(request, "contrctorviewlabor.html", {"data": data})
######################################################################
#                   LOAD LABOR DETAILS FOR CONTRACTOR
######################################################################


def contractorviewlabordetails(request):
    """ 
        The function to load details of a particular registered labors 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            labor details
    """
    lid = request.GET.get("id")
    s = "select tbllabour.*,tblglobalid.* from tbllabour,tblglobalid where tbllabour.labId='" + \
        lid+"' and tbllabour.labId=tblglobalid.labId"
    c.execute(s)
    data = c.fetchall()
    return render(request, "contractorviewlabordetails.html", {"data": data})
######################################################################
#                   WORK REQUEST FOR CONTRACTOR
######################################################################


def contractorworkrequest(request):
    """ 
        The function to load work request for contractors 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            labor details
    """

    s = "select tbltender.*,tbluser.uName from tbltender,tbluser where tbltender.uEmail=tbluser.uEmail and tbltender.reqStatus='requested'"
    c.execute(s)
    data = c.fetchall()
    return render(request, "contractorworkrequest.html", {"data": data})
    ######################################################################
#                   LOCATION OF WORK FOR CONTRACTOR
######################################################################


def contractorviewworkplace(request):
    """ 
        The function to load work place for contractors 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            labor details
    """
    wid = request.GET.get("id")
    s = "select reqLat,reqLon from tbltender where reqId='"+wid+"'"
    c.execute(s)
    d = c.fetchall()
    return render(request, "contractorviewworkplace.html", {"d": d})
######################################################################
#                   ADD TENDER CALL
######################################################################


def contractoraddtender(request):
    """ 
        The function to add tender call for contractors 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            labor details
    """
    msg = ""
    reqid = request.GET.get("id")
    email = request.session["email"]
    s = "select tenAmt from tbltendercall where reqId='"+reqid+"'"
    c.execute(s)
    data = c.fetchall()
    if(request.POST):
        amt = request.POST["Amount"]
        sdate = request.POST["Sdate"]
        edate = request.POST["Edate"]
        tender = request.POST["Tender"]
        s = "insert into tbltendercall (reqId,conEmail,tenAmt,tenSdate,tenEdate,tenDescription,tenStatus) values('" + \
            reqid+"','"+email+"','"+amt+"','"+sdate + \
            "','"+edate+"','"+tender+"','submitted')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Sorry some error occured"
        else:
            msg = "Tender call added successfully"
    return render(request, "contractoraddtender.html", {"data": data, "msg": msg})
######################################################################
#                   VIEW CONTRACTOR'S WORK
######################################################################


def contractorwork(request):
    """ 
        The function to view work details of contractors 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            labor details
    """
    email = request.session["email"]
    s = "select tblworkdetails.wSdate,tblworkdetails.wEdate,tblworkdetails.workAmt,tblworkdetails.wStatus,tbltender.reqDescription,tbluser.uName,tbluser.uContact,tblworkdetails.workId from tbltender,tbltendercall,tbluser,tblworkdetails where tbltender.uEmail=tbluser.uEmail and tbltender.reqId=tbltendercall.reqId and tbltendercall.conEmail='" + \
        email+"' and tblworkdetails.tcId=tbltendercall.tcId and tblworkdetails.wStatus<>'Completed'"
    c.execute(s)
    data = c.fetchall()
    return render(request, "contractorwork.html", {"data": data})
######################################################################
#                   ADD LABOR FOR A WORK
######################################################################


def contractoraddlabors(request):
    """ 
        The function to add labours for a work by contractor
        --------------------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            labor details
    """
    msg = ""
    email = request.session["email"]
    wid = request.GET.get("id")
    s = "select tbllabour.labName,tbllabour.labPhoto,tblworklabors.globalId from tbllabour,tblglobalid,tblworklabors where tbllabour.labId=tblglobalid.labId and tblworklabors.globalid=tblglobalid.globalId and tblworklabors.workId='"+wid+"'"
    c.execute(s)
    data = c.fetchall()
    s = "select tblglobalid.globalid,tbllabour.labName from tbllabour,tblglobalid where tbllabour.conEmail='"+email + \
        "' and tbllabour.labId=tblglobalid.labId and tblglobalid.globalId not in(select globalId from tblworklabors where workId='"+wid+"')"
    c.execute(s)
    labors = c.fetchall()
    if(request.POST):
        gid = request.POST["GID"]
        s = "insert into tblworklabors (workId,globalId) values('" + \
            wid+"','"+gid+"')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Sorry some error occured"
        else:
            msg = "Labor added successfully"
            return HttpResponseRedirect("/contractorwork")
    return render(request, "contractoraddlabors.html", {"data": data, "labors": labors, "msg": msg})
######################################################################
#                   ADD UPDATE OF WORK
######################################################################


def contractorupdatework(request):
    """ 
        The function to add update details of a work by contractor
        --------------------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            labor details
    """
    msg = ""
    wid = request.GET.get("id")
    s = "select * from tblworkdetails where workId='"+wid+"'"
    c.execute(s)
    data = c.fetchall()
    if(request.POST):
        amt = request.POST["Amount"]
        # sdate=request.POST["Sdate"]
        edate = request.POST["Edate"]
        status = request.POST["Status"]
        s = "update tblWorkdetails set workAmt='"+amt+"', wEdate='" + \
            edate+"',wStatus='"+status+"' where workId='"+wid+"'"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Sorry some error occured"
        else:
            msg = "Details updated successfully"
            return HttpResponseRedirect("/contractorwork")
    return render(request, "contractorupdatework.html", {"data": data, "msg": msg})
######################################################################
#                   VIEW CONTRACTOR'S COMPLETED WORK
######################################################################


def contractorcompletedwork(request):
    """ 
        The function to view completed work details of contractors 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            labor details
    """
    email = request.session["email"]
    s = "select tblworkdetails.wSdate,tblworkdetails.wEdate,tblworkdetails.workAmt,tblworkdetails.wStatus,tbltender.reqDescription,tbluser.uName,tbluser.uContact,tblworkdetails.workId from tbltender,tbltendercall,tbluser,tblworkdetails where tbltender.uEmail=tbluser.uEmail and tbltender.reqId=tbltendercall.reqId and tbltendercall.conEmail='" + \
        email + \
        "' and tblworkdetails.tcId=tbltendercall.tcId and (tblworkdetails.wStatus='Completed' or tblworkdetails.wStatus='Incomplete')"
    c.execute(s)
    data = c.fetchall()
    return render(request, "contractorcompletedwork.html", {"data": data})
######################################################################
#                   VIEW FEEDBACK
######################################################################


def contractorfeedback(request):
    """ 
        The function to add feedback  of users 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            labor details
    """
    wid = request.GET.get("id")
    s = "select * from tblfeedback where workId='"+wid+"'"
    c.execute(s)
    i = c.fetchall()
    return render(request, "contractorfeedback.html", {"data": i})
######################################################################
#                           CHANGE PASSWORD
######################################################################


def contractorchangepwd(request):
    """ 
        The function to load chnge password for contractor. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        email = request.session["email"]
        current = request.POST["Current"]
        new = request.POST["New"]
        s = "select * from tbllogin where username='"+email+"'"
        c.execute(s)
        i = c.fetchone()
        if(i[1] == current):
            s = "update tbllogin set password='"+new+"' where username='"+email+"'"
            try:
                c.execute(s)
                db.commit()
            except:
                msg = "Sorry some error occured"
            else:
                msg = "Data updated successfully"
        else:
            msg = "Incorrect password"
    return render(request, "contractorchangepwd.html", {"msg": msg})
######################################################################
#                           USER REGISTRATION
######################################################################


def userreg(request):
    """ 
        The function to register user
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""

    if(request.POST):
        name = request.POST["Name"]
        aadhar = request.POST["Aadhar"]
        email = request.POST["Email"]
        phone = request.POST["Contact"]
        pwd = request.POST["Password"]
        s = "select count(*) from tbllogin where username='"+email+"'"
        c.execute(s)
        i = c.fetchone()
        if(i[0] > 0):
            msg = "Email already registered"
        else:
            s = "insert into tblUser (uName,uContact,uEmail,uAadhar) values('" + \
                name+"','"+phone+"','"+email+"','"+aadhar+"')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg = s
            else:
                s = "insert into tbllogin (username,password,utype,status) values('" + \
                    email+"','"+pwd+"','user','1')"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    msg = "Sorry login process error"
                else:
                    msg = "Registered successfully"
                    return HttpResponseRedirect("/")
    return render(request, "index.html", {"msg": msg})

######################################################################
#                           LOAD USER PAGE
######################################################################


def userhome(request):
    """ 
        The function to load user home page . 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    email = request.session["email"]
    s = "select * from tbluser where uEmail='"+email+"'"
    c.execute(s)
    data = c.fetchall()
    msg = ""
    if(request.POST):
        name = request.POST["Name"]
        aadhar = request.POST["Aadhar"]
        email = request.POST["Email"]
        phone = request.POST["Phone"]
        s = "update tbluser set uName='"+name+"',uAadhar='" + \
            aadhar+"',uContact='"+phone+"' where uEmail='"+email+"'"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Sorry some error occured"
        else:
            msg = "Data updated successfully"
    return render(request, "userhome.html", {"details": data, "msg": msg})
######################################################################
#                           USER WORK REQUEST
######################################################################


def userworkrequest(request):
    """ 
        The function to load work request page for user . 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    email = request.session["email"]
    msg = ""
    if(request.POST):
        work = request.POST["Work"]
        wdate = request.POST["Wdate"]
        place = request.POST["Place"]
        l1 = request.POST["l1"]
        l2 = request.POST["l2"]
        s = "insert into tbltender(uEmail,reqDescription,reqDate,reqPlace,reqLat,reqLon,reqStatus) values('" + \
            email+"','"+work+"','"+wdate+"','"+place+"','"+l1+"','"+l2+"','requested')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Sorry some error occured"
        else:
            msg = "Data updated successfully"
    today = date.today()
    return render(request, "userrequest.html", {"msg": msg, "today": today})
######################################################################
#                   VIEW TENDER CALLS
######################################################################


def usertendercalls(request):
    """ 
        The function to load all tender calls for users 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    email = request.session["email"]
    s = "select tbltendercall.*,tbltender.reqDescription,tblcontractor.conName,conPhone from tbltender,tbltendercall,tblcontractor where tbltendercall.conEmail=tblcontractor.conEmail and tbltender.reqId=tbltendercall.reqId and tbltender.reqStatus='requested' and tbltender.uEmail='"+email+"'"
    c.execute(s)
    data = c.fetchall()
    return render(request, "usertendercalls.html", {"data": data})
######################################################################
#                   TENDER APPROVAL
######################################################################


def userapprovetender(request):
    """ 
        The function to approve tender calls for users 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    tid = request.GET.get("id")

    s = "select * from tbltendercall where tcId='"+tid+"'"
    c.execute(s)
    i = c.fetchone()
    sDate = i[4]
    eDate = i[5]
    tenAmt = i[3]
    reqid = i[1]
    s = "update tbltendercall set tenStatus='accepted' where tcId='"+tid+"'"
    try:
        c.execute(s)
        db.commit()
    except:
        #msg="Sorry some error occured"
        return HttpResponseRedirect("/usertendercalls")
    else:
        s = "update tbltendercall set tenStatus='rejected' where tcId<>'" + \
            str(tid)+"' and reqId ='"+str(reqid)+"'"
        try:
            c.execute(s)
            db.commit()
        except:
            # msg="Sorry some error occured"
            return HttpResponseRedirect("/usertendercalls")
        else:
            s = "update tbltender set reqStatus='set' where reqId ='" + \
                str(reqid)+"'"
            try:
                c.execute(s)
                db.commit()
            except:
                # msg="Sorry some error occured"
                return HttpResponseRedirect("/usertendercalls")
            else:

                s = "insert into tblworkdetails (tcId,workAmt,wSdate,wEdate,wStatus) values('"+str(
                    tid)+"','"+str(tenAmt)+"','"+str(sDate)+"','"+str(eDate)+"','commited')"
                try:
                    c.execute(s)
                    db.commit()
                except:
                    # msg="Sorry some error occured"
                    return HttpResponseRedirect("/usertendercalls")
                else:
                    return HttpResponseRedirect("/userwork")
    # return render(request,"contractorworkrequest.html",{"msg":msg})
######################################################################
#                   VIEW WORK FOR USERS
######################################################################


def userwork(request):
    """ 
        The function to load all work for users 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    email = request.session["email"]
    s = "select tblworkdetails.wSdate,tblworkdetails.wEdate,tblworkdetails.workAmt,tblworkdetails.wStatus,tbltender.reqDescription,tblcontractor.conName,tblcontractor.conPhone,tblworkdetails.workId from tbltender,tbltendercall,tblcontractor,tblworkdetails where tbltendercall.conEmail=tblcontractor.conEmail and tbltender.reqId=tbltendercall.reqId and tbltender.uEmail='"+email+"' and tblworkdetails.tcId=tbltendercall.tcId"
    c.execute(s)
    data = c.fetchall()
    return render(request, "userwork.html", {"data": data})
######################################################################
#                   VIEW WORKERS FOR A WORK BY USERS
######################################################################


def userviewlabors(request):
    """ 
        The function to load all workers for a work 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    wid = request.GET.get("id")
    s = "select tbllabour.labName,tbllabour.labPhoto,tblworklabors.globalId from tbllabour,tblglobalid,tblworklabors where tbllabour.labId=tblglobalid.labId and tblworklabors.globalid=tblglobalid.globalId and tblworklabors.workId='"+wid+"'"
    c.execute(s)
    data = c.fetchall()
    return render(request, "userviewlabors.html", {"data": data})
######################################################################
#                   VIEW USER'S COMPLETED WORK
######################################################################


def usercompletedwork(request):
    """ 
        The function to view completed work details of users 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            labor details
    """
    email = request.session["email"]
    s = "select tblworkdetails.wSdate,tblworkdetails.wEdate,tblworkdetails.workAmt,tblworkdetails.wStatus,tbltender.reqDescription,tblcontractor.conName,tblcontractor.conPhone,tblworkdetails.workId from tbltender,tbltendercall,tblcontractor,tblworkdetails where tbltendercall.conEmail=tblcontractor.conEmail and tbltender.reqId=tbltendercall.reqId and tbltender.uEmail='" + \
        email+"' and tblworkdetails.tcId=tbltendercall.tcId and tblworkdetails.wStatus='Completed'"
    c.execute(s)
    data = c.fetchall()
    return render(request, "usercompletedwork.html", {"data": data})
######################################################################
#                   ADD FEEDBACK
######################################################################


def useraddfeedback(request):
    """ 
        The function to add feedback  of users 
        --------------------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            labor details
    """
    msg = ""
    wid = request.GET.get("id")
    s = "select count(*) from tblfeedback where workId='"+wid+"'"
    c.execute(s)
    i = c.fetchone()
    if(i[0] > 0):
        return HttpResponseRedirect("/usercompletedwork")
    else:
        if(request.POST):
            feedback = request.POST["Feedback"]
            s = "insert into tblfeedback(workId,fdate,feedback) values('" + \
                wid+"',(select sysdate()),'"+feedback+"')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg = "Sorry some error occured"
            else:
                return HttpResponseRedirect("/usercompletedwork")
    return render(request, "useraddfeedback.html", {"msg": msg})
######################################################################
#                          USER COMPLAINT
######################################################################


def usercomplaint(request):
    """ 
        The function to add complaint for user. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    police = viewpolice()
    if(request.POST):
        email = request.session["email"]
        pol = request.POST["Police"]
        complaint = request.POST["Complaint"]
        height = request.POST["Height"]
        weight = request.POST["Weight"]
        place = request.POST["Place"]
        l1 = request.POST["l1"]
        l2 = request.POST["l2"]
        s = "insert into tblcomplaint(uEmail,pEmail,compDetails,culpritHeight,culpritWeight,compPlace,compLat,compLon,compStatus) values('" + \
            email+"','"+pol+"','"+complaint+"','"+height+"','" + \
            weight+"','"+place+"','"+l1+"','"+l2+"','Submitted')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Sorry some error occured"
        else:
            msg = "Complaint added successfully"

    return render(request, "usercomplaint.html", {"msg": msg, "police": police})

######################################################################
#                           CHANGE PASSWORD
######################################################################


def userchangepwd(request):
    """ 
        The function to load chnge password for user. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        email = request.session["email"]
        current = request.POST["Current"]
        new = request.POST["New"]
        s = "select * from tbllogin where username='"+email+"'"
        c.execute(s)
        i = c.fetchone()
        if(i[1] == current):
            s = "update tbllogin set password='"+new+"' where username='"+email+"'"
            try:
                c.execute(s)
                db.commit()
            except:
                msg = "Sorry some error occured"
            else:
                msg = "Data updated successfully"
        else:
            msg = "Incorrect password"
    return render(request, "userchangepwd.html", {"msg": msg})
