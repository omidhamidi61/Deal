from django.db import models

# Create your models here.
class WorkersTable(models.Model):
    name = models.CharField(max_length = 50)
    username = models.CharField(max_length = 50)
    pssword = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
    
class MessagesTable(models.Model):
    sender = models.ForeignKey(WorkersTable,related_name='MessagesTable',on_delete = models.CASCADE)
    receiver = models.ForeignKey(WorkersTable, related_name='workersTable', on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    content = models.TextField(max_length = None)
    isUnread = models.BooleanField(null = False)
    isAccepted = models.BooleanField(null = False)
    dealers = models.ManyToManyField(WorkersTable, related_name='workersTable2')

class TeamMembersTable(models.Model):
    member = models.ForeignKey(WorkersTable, related_name='workersTable3', on_delete = models.CASCADE , null = True)
    teamnumber = models.IntegerField(null = False)
    supervisor = models.ForeignKey(WorkersTable,related_name='TeamMembersTable',on_delete = models.CASCADE)
    isRated = models.BooleanField(null = False)
    isSupervisor = models.BooleanField(null = False)

    