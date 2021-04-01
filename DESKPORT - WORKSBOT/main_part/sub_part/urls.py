from django.urls import path
from . import views

urlpatterns = [
    path('',views.start_page, name="start_page"),
    path('Login_Page',views.login_page, name="Login_Page"),
    path('Register_Page',views.register_page, name="Register_Page"),
    path('Admin_Dashboard',views.admin_dashboard, name="Admin_Dashboard"),
    path('All_Tickets',views.all_tickets, name="All_Tickets"),
    path('All_Tickets_Add',views.all_tickets_add, name="All_Tickets_Add"),
    path('Custom_Fields',views.custom_fields, name="Custom_Fields"),
    path('Custom_Fields_Edit/<int:id>',views.custom_fields_edit, name="Custom_Fields_Edit"),
    path('Custom_Fields_Update/<int:id>',views.custom_fields_update, name="Custom_Fields_Update"),
    path('Custom_Fields_Delete/<int:id>',views.custom_fields_delete, name="Custom_Fields_Delete"),
    path('Departments',views.departments, name="Departments"),
    path('D_add',views.departments_add, name="Departments_Add"),
    path('Departments_Edit/<int:id>',views.departments_edit, name="Departments_Edit"),
    path("Departments_Update/<int:id>",views.departments_update, name="Departments_Update"),
    path("Departments_Delete/<int:id>",views.departments_delete, name="Departments_Delete"),
    path('Knowledge_Base',views.knowledge_base, name="Knowledge_Base"),
    path('K_add',views.knowledge_base_add, name="Knowledge_Base_Add"),
    path('Knowledge_Base_Edit/<int:id>',views.knowledge_base_edit, name="Knowledge_Base_Edit"),
    path("Knowledge_Base_Update/<int:id>",views.knowledge_base_update, name="Knowledge_Base_Update"),
    path("Knowledge_Base_Delete/<int:id>",views.knowledge_base_delete, name="Knowledge_Base_Delete"),
    path('Staffs',views.staffs, name="Staffs"),
    path('S_add',views.staffs_add, name="Staffs_Add"),
    path('Staffs_Edit/<int:id>',views.staffs_edit, name="Staffs_Edit"),
    path('Staffs_Update/<int:id>',views.staffs_update, name="Staffs_Update"),
    path('Staffs_Delete/<int:id>',views.staffs_delete, name="Staffs_Delete"),
    path('Users',views.users, name="Users"),
    path('U_add',views.users_add, name="Users_Add"),
    path('Users_Edit/<int:id>',views.users_edit, name="Users_Edit"),
    path('Users_Update/<int:id>',views.users_update, name="Users_Update"),
    path('Users_Delete/<int:id>',views.users_delete, name="Users_Delete"),
    path('Roles',views.roles, name="Roles"),
    path('R_add',views.roles_add, name="Roles_Add"),
    path('Roles_Edit/<int:id>',views.roles_edit, name="Roles_Edit"),
    path('Roles_Update/<int:id>',views.roles_update, name="Roles_Update"),
    path('Roles_Delete/<int:id>',views.roles_delete, name="Roles_Delete"),
    path('User_Login_Page',views.user_login_page, name="User_Login_Page"),
    path('User_Register_Page',views.user_register_page, name="User_Register_Page"),
    path('User_Dashboard',views.user_dashboard, name="User_Dashboard"),
    path('User_Add_Ticket',views.user_add_ticket, name="User_Add_Ticket"),
    path('User_Edit_Ticket/<int:id>',views.user_edit_ticket, name="User_Edit_Ticket"),
    path('User_Update_Ticket/<int:id>',views.user_update_ticket, name="User_Update_Ticket"),
    path('User_Delete_Ticket/<int:id>',views.user_delete_ticket, name="User_Delete_Ticket"),
    path('Forgot_Password_Page1',views.forgot_password_page1,name="Forgot_Password_Page1"),
    path('Forgot_Password_Page2',views.forgot_password_page2,name="Forgot_Password_Page2"),
    path('Update_Password/<int:id>',views.update_password,name="Update_Password"),
    path('User_Forgot_Password_Page1',views.user_forgot_password_page1,name="User_Forgot_Password_Page1"),
    path('User_Forgot_Password_Page2',views.user_forgot_password_page2,name="User_Forgot_Password_Page2"),
    path('User_Update_Password/<int:id>',views.user_update_password,name="User_Update_Password"),







]