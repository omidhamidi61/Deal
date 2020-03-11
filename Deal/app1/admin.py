from django.contrib import admin
from app1 import models
# Register your models here.
admin.site.register(models.WorkersTable)
admin.site.register(models.MessagesTable)
admin.site.register(models.TeamMembersTable)