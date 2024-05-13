from django.contrib import admin

from Home_Page.models import Review, TeamMember, Why_Selecting_US

# Register your models here.
admin.site.register(Why_Selecting_US)
admin.site.register(TeamMember)
admin.site.register(Review)