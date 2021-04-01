from django.db import models
import datetime


# Create your models here.
class Login_data(models.Model):
    username= models.CharField(max_length=20)
    password= models.CharField(max_length=16)
    email= models.CharField(max_length=30)
    country= models.CharField(max_length=30)

    def __str__(self):
        return self.username

class Tickets_data(models.Model):
    problemtitle= models.CharField(max_length=40)
    problemid=models.CharField(max_length=10)
    date = models.DateField(("Date"), default=datetime.date.today)
    user = models.CharField(max_length=30)
    department= models.CharField(max_length=20)
    priority= models.CharField(max_length=20)
    message= models.CharField(max_length=400)
    website= models.CharField(max_length=20)
    file= models.FileField(blank=True, null=True, upload_to='Problem Files')
    product= models.CharField(max_length=20)

    def __str__(self):
        return self.problemtitle
    
class Customfield_data(models.Model):
    customfieldname= models.CharField(max_length=20)
    customfieldtype= models.CharField(max_length=20)
    customfieldplaceholder= models.CharField(max_length=30)
    customfieldfieldlength= models.CharField(max_length=15)
    customfieldrequired= models.CharField(max_length=20)
    customfieldstatus= models.CharField(max_length=20)

    def __str__(self):
        return self.customfieldname

class Departments_data(models.Model):
    departmenttitle= models.CharField(max_length=20)
    departmentdescription= models.CharField(max_length=100)

    def __str__(self):
        return self.departmenttitle

class Knowledge_Base_data(models.Model):
    knowlegebaseDepartment= models.CharField(max_length=20)
    knowlegebasetitle= models.CharField(max_length=20)
    knowlegebasedescription= models.CharField(max_length=100)
    knowlegebaserequired= models.CharField(max_length=20)

    def __str__(self):
        return self.knowlegebaseDepartment

class Staffs_data(models.Model):
    staffname= models.CharField(max_length=20)
    staffemail= models.CharField(max_length=40)
    staffdepartment= models.CharField(max_length=20)
    staffrole= models.CharField(max_length=20)
    staffstatus= models.CharField(max_length=20)
    staffpassword= models.CharField(max_length=16)

    def __str__(self):
        return self.staffname

class Users_data(models.Model):
    username= models.CharField(max_length=20)
    useremail= models.CharField(max_length=40)
    userstatus= models.CharField(max_length=20)
    userpassword= models.CharField(max_length=16)

    def __str__(self):
        return self.username

class Roles_data(models.Model):
    roletitle= models.CharField(max_length=20)
    settingsrole= models.CharField(max_length=200)
    frontendsettingsrole= models.CharField(max_length=200)
    departmentssettingsrole= models.CharField(max_length=200)
    knowledgesettingsrole= models.CharField(max_length=200)
    staffsettingsrole= models.CharField(max_length=200)
    usersettingsrole= models.CharField(max_length=200)

    def __str__(self):
        return self.roletitle