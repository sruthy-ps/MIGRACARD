from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usertypes(models.Model):
    logid=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    utype=models.CharField(max_length=100)

class Policestation(models.Model):
    pscode=models.CharField(max_length=100)
    pname=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    circle=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    username=models.CharField(max_length=100)

class Userreg(models.Model):
    name=models.CharField(max_length=100)
    aadhar=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)

class Contractorreg(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    license=models.CharField(max_length=100)
    certificate=models.ImageField(null=True)

class Labourreg(models.Model):
    name=models.CharField(max_length=100)
    pid=models.ForeignKey(Policestation,on_delete=models.CASCADE,blank=True,null=True)
    cid=models.ForeignKey(Contractorreg,on_delete=models.CASCADE,blank=True,null=True)
    address=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    idmark1=models.CharField(max_length=100)
    idmark2=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    aadhar=models.CharField(max_length=100)
    aadharfile=models.ImageField(null=True)
    color=models.CharField(max_length=100)
    photo=models.ImageField(null=True)
    disease=models.CharField(max_length=100)
    sign=models.ImageField(null=True)
    status=models.CharField(max_length=100)
    height=models.CharField(max_length=100)
    weight=models.CharField(max_length=100)



class Globalid(models.Model):
    labid=models.ForeignKey(Labourreg,on_delete=models.CASCADE,blank=True,null=True)
    dateissue=models.DateField(auto_now=True)
    status=models.CharField(max_length=100)

class Tender(models.Model):
    uid=models.ForeignKey(Userreg,on_delete=models.CASCADE,blank=True,null=True)
    reqdesc=models.CharField(max_length=100)
    reqdate=models.DateField()
    place=models.CharField(max_length=100)
    lat=models.CharField(max_length=100)
    lon=models.CharField(max_length=100)
    status=models.CharField(max_length=100)

class Tendercall(models.Model):
    reqid=models.ForeignKey(Tender,on_delete=models.CASCADE,blank=True,null=True)
    conid=models.ForeignKey(Contractorreg,on_delete=models.CASCADE,blank=True,null=True)
    amount=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    sdate=models.DateField(max_length=100)
    edate=models.DateField(max_length=100)
    status=models.CharField(max_length=100)

class Workdetails(models.Model):
    tcid=models.ForeignKey(Tendercall,on_delete=models.CASCADE,blank=True,null=True)
    wrkamount=models.CharField(max_length=100)
    wsdate=models.CharField(max_length=100)
    wedate=models.DateField(max_length=100)
    status=models.CharField(max_length=100)

class Worklabors(models.Model):
    wrkid=models.ForeignKey(Workdetails,on_delete=models.CASCADE,blank=True,null=True)
    glid=models.ForeignKey(Globalid,on_delete=models.CASCADE,blank=True,null=True)

class Complaint(models.Model):
    uid=models.ForeignKey(Userreg,on_delete=models.CASCADE,blank=True,null=True)
    pid=models.ForeignKey(Policestation,on_delete=models.CASCADE,blank=True,null=True)
    complaint=models.CharField(max_length=100)
    reply=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=100)
    clheight=models.CharField(max_length=100)
    clweight=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    lat=models.CharField(max_length=100)
    lon=models.CharField(max_length=100)

class Feedback(models.Model):
    wid=models.ForeignKey(Workdetails,on_delete=models.CASCADE,blank=True,null=True)
    feedback=models.CharField(max_length=100)
    fdate=models.CharField(max_length=100)


class Labourrequest(models.Model):
    lid=models.ForeignKey(Labourreg,on_delete=models.CASCADE,blank=True,null=True)
    conid=models.ForeignKey(Contractorreg,on_delete=models.CASCADE,blank=True,null=True)
    reqdate=models.DateField(auto_now=True)
    status=models.CharField(max_length=100)