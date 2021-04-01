from django.shortcuts import render,redirect
from . models import Login_data
from . models import Tickets_data
from . models import Customfield_data
from . models import Departments_data
from . models import Knowledge_Base_data
from . models import Staffs_data
from . models import Users_data
from . models import Roles_data

import random
import easygui

# Create your views here.
#global variable for usernames
user_name=''
#global variable for remember me
remember_me=''

def start_page(request):
    global remember_me
    remember_me="False"
    return render(request,'index.html')

def login_page(request):
    if(remember_me=="True"):
        return redirect("Admin_Dashboard")
    else:
        return render(request,'Login_Page.html')

def register_page(request):
    if request.method == 'POST':
        login_data = Login_data(username=request.POST['username'], password=request.POST['password'],
                        email=request.POST['email'], country=request.POST['country'])
        login_data.save()
        #easygui.msgbox("your registrations has been completed successfully.")
        return redirect('Login_Page')
    else:
        return render(request,'Register_Page.html')


def admin_dashboard(request):
    if request.method == 'POST':
        if Login_data.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            login_data = Login_data.objects.get(username=request.POST['username'], password=request.POST['password'])
            t_data=Tickets_data.objects.all()
            global user_name
            user_name=login_data.username
            global remember_me
            remember_me=request.POST.get('remember_me',False)
            return render(request, 'Admin_Dashboard.html', {'user_name': user_name, 't_data':t_data})
        else:
            message={"error":"Invalid username or password!"}
            return render(request, 'Login_Page.html',{"message": message})
    else:
        t_data=Tickets_data.objects.all()
        return render(request,"Admin_Dashboard.html", {'user_name': user_name, 't_data':t_data})

def all_tickets(request):
    t_data=Tickets_data.objects.all()
    return render(request,'All_Tickets.html', {'user_name': user_name,"t_data":t_data})

def all_tickets_add(request):
    if request.method == 'POST':
        pid=randomid()
        tickets_data = Tickets_data(problemtitle=request.POST['problemtitle'], problemid=pid,
                        department=request.POST['department'], user=user_name,
                        priority=request.POST['priority'], message=request.POST['message'], website=request.POST['website'],
                        file=request.POST['file'], product=request.POST['product'])
        tickets_data.save()
        #easygui.msgbox("your ticket has been saved successfully.")
        return redirect('All_Tickets')
    else:
        return render(request,'All_Tickets_Add.html',{'user_name': user_name})

def custom_fields(request):
    if request.method == 'POST':
        customfield_data = Customfield_data(customfieldname=request.POST['customfieldname'], customfieldtype=request.POST['customfieldtype'],
                        customfieldplaceholder=request.POST['customfieldplaceholder'], customfieldfieldlength=request.POST['customfieldfieldlength'],
                        customfieldrequired=request.POST['customfieldrequired'], customfieldstatus=request.POST['customfieldstatus'])
        customfield_data.save()
        #easygui.msgbox("your custom field has been saved successfully.")
        cf_data=Customfield_data.objects.all()
        return render(request,'Custom_Fields.html', {'user_name': user_name,"cf_data":cf_data})
    else:
        cf_data=Customfield_data.objects.all()
        return render(request,'Custom_Fields.html', {'user_name': user_name,"cf_data":cf_data})

def custom_fields_edit(request,id):
    customfield_data= Customfield_data.objects.get(id=id)
    return render(request,"Custom_Fields_Edit.html",{'user_name': user_name,'cf_data':customfield_data})


def custom_fields_update(request,id):
    customfield_data_edit=Customfield_data(id=id, customfieldname=request.POST['customfieldname'], customfieldtype=request.POST['customfieldtype'],
                        customfieldplaceholder=request.POST['customfieldplaceholder'], customfieldfieldlength=request.POST['customfieldfieldlength'],
                        customfieldrequired=request.POST['customfieldrequired'], customfieldstatus=request.POST['customfieldstatus'])
    customfield_data_edit.save()
    #easygui.msgbox("your custom field has been edited successfully.")
    return redirect("Custom_Fields")
           

def custom_fields_delete(request,id):
    customfield_data= Customfield_data.objects.get(id=id)
    customfield_data.delete()
    #easygui.msgbox("your custom field has been deleted successfully.")
    return redirect("Custom_Fields")

def departments(request):
    d_data=Departments_data.objects.all()
    return render(request,'Departments.html', {'user_name': user_name,"d_data":d_data})

def departments_add(request):
    if request.method == 'POST':
        departments_data = Departments_data(departmenttitle=request.POST['departmenttitle'],
         departmentdescription=request.POST['departmentdescription'])
        departments_data.save()
        #easygui.msgbox("your department has been saved successfully.")
        return redirect('Departments')
    else:
        return render(request,'Departments_Add.html',{'user_name': user_name})

def departments_edit(request,id):
    departments_data=Departments_data.objects.get(id=id)
    return render(request,'Departments_Edit.html',{'user_name': user_name,"d_data":departments_data})

def departments_update(request,id):
    departments_data_edit=Departments_data(id=id, departmenttitle=request.POST['departmenttitle'],
         departmentdescription=request.POST['departmentdescription'])
    departments_data_edit.save()
    #easygui.msgbox("your department has been edited successfully.")
    return redirect("Departments")
    
def departments_delete(request,id):
    departments_data=Departments_data.objects.get(id=id)
    departments_data.delete()
    #easygui.msgbox("your department has been deleted successfully.")
    return redirect("Departments")

def knowledge_base(request):
    kb_data=Knowledge_Base_data.objects.all()
    return render(request,'Knowledge_Base.html', {'user_name': user_name,"kb_data":kb_data})

def knowledge_base_add(request):
    if request.method == 'POST':
        knowledge_Base_data = Knowledge_Base_data(knowlegebaseDepartment=request.POST['knowlegebaseDepartment'],
         knowlegebasetitle=request.POST['knowlegebasetitle'], knowlegebasedescription=request.POST['knowlegebasedescription'],
         knowlegebaserequired=request.POST['knowlegebaserequired'])
        knowledge_Base_data.save()
        #easygui.msgbox("your knowledge base has been saved successfully.")
        return redirect('Knowledge_Base')
    else:
        return render(request,'Knowledge_Base_Add.html',{'user_name': user_name})

def knowledge_base_edit(request, id):
    knowledge_Base_data=Knowledge_Base_data.objects.get(id=id)
    return render(request,'Knowledge_Base_Edit.html',{'user_name': user_name,"kb_data":knowledge_Base_data})

def knowledge_base_update(request, id):
    knowledge_Base_data_edit = Knowledge_Base_data(id=id, knowlegebaseDepartment=request.POST['knowlegebaseDepartment'],
         knowlegebasetitle=request.POST['knowlegebasetitle'], knowlegebasedescription=request.POST['knowlegebasedescription'],
         knowlegebaserequired=request.POST['knowlegebaserequired'])
    knowledge_Base_data_edit.save()
    #easygui.msgbox("your knowledge base has been edited successfully.")
    return redirect("Knowledge_Base")

def knowledge_base_delete(request, id):
    knowledge_Base_data=Knowledge_Base_data.objects.get(id=id)
    knowledge_Base_data.delete()
    #easygui.msgbox("your knowledge base has been deleted successfully.")
    return redirect("Knowledge_Base")

def staffs(request):
    s_data=Staffs_data.objects.all()
    return render(request,'Staffs.html', {'user_name': user_name,"s_data":s_data})

def staffs_add(request):
    if request.method == 'POST':
        staffs_data = Staffs_data(staffname=request.POST['staffname'],
         staffemail=request.POST['staffemail'], staffdepartment=request.POST['staffdepartment'],
         staffrole=request.POST['staffrole'], staffstatus=request.POST['staffstatus'],
         staffpassword=request.POST['staffpassword'])
        staffs_data.save()
        #easygui.msgbox("your staff data has been saved successfully.")
        return redirect('Staffs')
    else:
        return render(request,'Staffs_Add.html',{'user_name': user_name})

def staffs_edit(request,id):
    staffs_data=Staffs_data.objects.get(id=id)
    return render(request,'Staffs_Edit.html',{'user_name': user_name,"s_data":staffs_data})

def staffs_update(request,id):
    staffs_data_edit= Staffs_data(id=id, staffname=request.POST['staffname'],
         staffemail=request.POST['staffemail'], staffdepartment=request.POST['staffdepartment'],
         staffrole=request.POST['staffrole'], staffstatus=request.POST['staffstatus'],
         staffpassword=request.POST['staffpassword'])
    staffs_data_edit.save()
    #easygui.msgbox("your staff has been edited successfully.")
    return redirect("Staffs")

def staffs_delete(request,id):
    staffs_data=Staffs_data.objects.get(id=id)
    staffs_data.delete()
    #easygui.msgbox("your staff has been deleted successfully.")
    return redirect("Staffs")   

def users(request):
    u_data=Users_data.objects.all()
    return render(request,'Users.html', {'user_name': user_name,"u_data":u_data})

def users_add(request):
    if request.method == 'POST':
        users_data = Users_data(username=request.POST['username'],
         useremail=request.POST['useremail'], userstatus=request.POST['userstatus'],
         userpassword=request.POST['userpassword'])
        users_data.save()
        #easygui.msgbox("your user data has been saved successfully.")
        return redirect('Users')
    else:
        return render(request,'Users_Add.html',{'user_name': user_name})

def users_edit(request,id):
    users_data=Users_data.objects.get(id=id)
    return render(request,'Users_Edit.html',{'user_name': user_name,"u_data":users_data})

def users_update(request,id):
    users_data_edit = Users_data(id=id, username=request.POST['username'],
         useremail=request.POST['useremail'], userstatus=request.POST['userstatus'],
         userpassword=request.POST['userpassword'])
    users_data_edit.save()
    #easygui.msgbox("your user has been edited successfully.")
    return redirect("Users")

def users_delete(request,id):
    users_data=Users_data.objects.get(id=id)
    users_data.delete()
    #easygui.msgbox("your user has been deleted successfully.")
    return redirect("Users")

def roles(request):
    r_data=Roles_data.objects.all()
    return render(request,'Roles.html', {'user_name': user_name,"r_data":r_data})

def roles_add(request):
    if request.method == 'POST':
        roles_data = Roles_data(roletitle=request.POST['roletitle'],
         settingsrole=request.POST['settingsrole'], frontendsettingsrole=request.POST['frontendsettingsrole'],
         departmentssettingsrole=request.POST['departmentssettingsrole'],
         knowledgesettingsrole=request.POST['knowledgesettingsrole'],
         staffsettingsrole=request.POST['staffsettingsrole'], 
         usersettingsrole=request.POST['usersettingsrole'])
        roles_data.save()
        #easygui.msgbox("your role data has been saved successfully.")
        return redirect('Roles')
    else:
        return render(request,'Roles_Add.html',{'user_name': user_name})

def roles_edit(request,id):
    roles_data=Roles_data.objects.get(id=id)
    return render(request,'Roles_Edit.html',{'user_name': user_name,"r_data":roles_data})

def roles_update(request,id):
    roles_data_edit = Roles_data(id=id, roletitle=request.POST['roletitle'],
         settingsrole=request.POST['settingsrole'], frontendsettingsrole=request.POST['frontendsettingsrole'],
         departmentssettingsrole=request.POST['departmentssettingsrole'],
         knowledgesettingsrole=request.POST['knowledgesettingsrole'],
         staffsettingsrole=request.POST['staffsettingsrole'], 
         usersettingsrole=request.POST['usersettingsrole'])
    roles_data_edit.save()
    #easygui.msgbox("your role has been edited successfully.")
    return redirect("Roles")

def roles_delete(request,id):
    roles_data=Roles_data.objects.get(id=id)
    roles_data.delete()
    #easygui.msgbox("your role has been deleted successfully.")
    return redirect("Roles")

def user_login_page(request):
    return render(request,"User_Login_Page.html")

def user_register_page(request):
    if request.method == 'POST':
        users_data = Users_data(username=request.POST['username'],
         useremail=request.POST['useremail'], userstatus='Active',
         userpassword=request.POST['userpassword'])
        users_data.save()
        #easygui.msgbox("your user data has been saved successfully.")
        return redirect('User_Login_Page')
    else:
        return render(request,'User_Register_Page.html')

def user_dashboard(request):
    if request.method == 'POST':
        if Users_data.objects.filter(username=request.POST['username'], userpassword=request.POST['userpassword']).exists():
            users_login_data = Users_data.objects.get(username=request.POST['username'], userpassword=request.POST['userpassword'])
            ut_data=Tickets_data.objects.all()
            global user_name
            user_name=users_login_data.username
            global remember_me
            remember_me=request.POST.get('remember_me',False)
            return render(request, 'User_Dashboard.html', {'user_name': user_name, 'ut_data':ut_data})
        else:
            message={"error":"Invalid username or password!"}
            return render(request, 'User_Login_Page.html',{"message": message})
    else:
        ut_data=Tickets_data.objects.all()
        return render(request,"User_Dashboard.html", {'user_name': user_name, 'ut_data':ut_data})

def user_add_ticket(request):
    if request.method == 'POST':
        pid=randomid()
        tickets_data = Tickets_data(problemtitle=request.POST['problemtitle'], problemid=pid,
                        department=request.POST['department'], user=user_name,
                        priority=request.POST['priority'], message=request.POST['message'], website=request.POST['website'],
                        file=request.POST['file'], product=request.POST['product'])
        tickets_data.save()
        #easygui.msgbox("your ticket has been saved successfully.")
        return redirect('User_Dashboard')
    else:
        return render(request,'User_Add_Ticket.html',{'user_name': user_name})

def user_edit_ticket(request,id):
    users_ticket_data=Tickets_data.objects.get(id=id)
    return render(request,'User_Edit_Ticket.html',{'user_name': user_name,"ut_data":users_ticket_data})

def user_update_ticket(request,id):
    pid=pid=randomid()
    users_ticket_edit = Tickets_data(id=id, problemtitle=request.POST['problemtitle'], problemid=pid,
                        department=request.POST['department'], user=user_name,
                        priority=request.POST['priority'], message=request.POST['message'], website=request.POST['website'],
                        file=request.POST['file'], product=request.POST['product'])
    users_ticket_edit.save()
    #easygui.msgbox("your user has been edited successfully.")
    return redirect("User_Dashboard")

def user_delete_ticket(request,id):
    users_ticket_data=Tickets_data.objects.get(id=id)
    users_ticket_data.delete()
    #easygui.msgbox("your role has been deleted successfully.")
    return redirect("User_Dashboard")

def forgot_password_page1(request):
    return render(request,'Forgot_Password_Page1.html')

def forgot_password_page2(request):
    if request.method == 'POST':
        if Login_data.objects.filter(email=request.POST['email']).exists():
            login_data = Login_data.objects.get(email=request.POST['email'])            
            return render(request, 'Forgot_Password_Page2.html', {'login_data': login_data})
        else:
            message={"error":"This email doesn't exist, create new user"}
            return render(request, 'Forgot_Password_Page1.html',{"message": message})

def update_password(request,id):
    other_data= Login_data.objects.get(id=id)
    login_data = Login_data(id=id, username=other_data.username ,password=request.POST['password'], 
        email=other_data.email, country=other_data.country)
    login_data.save()
    #easygui.msgbox("your Password has been edited successfully.")
    return redirect("Login_Page")

def user_forgot_password_page1(request):
    return render(request,'User_Forgot_Password_Page1.html')

def user_forgot_password_page2(request):
    if request.method == 'POST':
        if Users_data.objects.filter(useremail=request.POST['email']).exists():
            users_data = Users_data.objects.get(useremail=request.POST['email'])            
            return render(request, 'User_Forgot_Password_Page2.html', {'users_data': users_data})
        else:
            message={"error":"This email doesn't exist, create new user"}
            return render(request, 'User_Forgot_Password_Page1.html',{"message": message})

def user_update_password(request,id):
    other_data= Users_data.objects.get(id=id)
    users_data = Users_data(id=id, username=other_data.username ,userpassword=request.POST['password'], 
        useremail=other_data.useremail, userstatus=other_data.userstatus)
    users_data.save()
    #easygui.msgbox("your Password has been edited successfully.")
    return redirect("User_Login_Page")

    
##Mycode functions

def randomid():
    pid=''
    for i in range (0,7):
        x=random.randint(65,90)
        pid=pid+chr(x)
    return pid