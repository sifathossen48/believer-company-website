from django.contrib import admin

from Home_Page.models import Review, TeamMember, Why_Selecting_US, C_Level_Person

# Register your models here.
admin.site.register(C_Level_Person)
admin.site.register(Why_Selecting_US)
admin.site.register(TeamMember)
admin.site.register(Review)