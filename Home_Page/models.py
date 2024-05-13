from django.db import models

# Create your models here.
class Why_Selecting_US(models.Model):
    section_name = models.CharField(max_length=50)
    happy_Clients = models.IntegerField(max_length=5)
    happy_Clients_Title = models.CharField(max_length=40)
    happy_Clients_Desc = models.TextField(max_length=600)
    personal_Consultants = models.IntegerField(max_length=5)
    personal_Consultants_Title = models.CharField(max_length=40)
    personal_Consultants_Desc = models.TextField(max_length=600)
    custom_Services = models.IntegerField(max_length=5)
    custom_Services_Title = models.CharField(max_length=40)
    custom_Services_Desc = models.TextField(max_length=600)
    years_of_Experience = models.IntegerField(max_length=5)
    years_of_Experience_Title = models.CharField(max_length=40)
    years_of_Experience_Desc = models.TextField(max_length=600)
    def __str__(self):
        return self.section_name
    
class TeamMember(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    profile = models.ImageField(upload_to='teamMember/')
    facebook = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Review(models.Model):
    clients_name = models.CharField(max_length=40)
    clients_quote = models.TextField()
    def __str__(self):
        return self.clients_name