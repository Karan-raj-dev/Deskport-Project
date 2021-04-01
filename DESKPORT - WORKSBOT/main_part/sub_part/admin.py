from django.contrib import admin
from . models import Login_data
from . models import Tickets_data
from . models import Customfield_data
from . models import Departments_data
from . models import Knowledge_Base_data
from . models import Staffs_data
from . models import Users_data
from . models import Roles_data

# Register your models here.

admin.site.register(Login_data)
admin.site.register(Tickets_data)
admin.site.register(Customfield_data)
admin.site.register(Departments_data)
admin.site.register(Knowledge_Base_data)
admin.site.register(Staffs_data)
admin.site.register(Users_data)
admin.site.register(Roles_data)
