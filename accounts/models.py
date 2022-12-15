from django.db import models

# Create your models here.
group = (
    ('1','A+'),
    ('2','O+'),
    ('3','B+'),
    ('4','AB+'),
    ('5','A-'),
    ('6','O-'),
    ('7','B-'),
    ('8','AB-'),
)
class Employee(models.Model):
    Employee_name = models.CharField(max_length = 30,blank = True)
    Email = models.EmailField()
    Contact_Number = models.IntegerField()
    Emergency_ContactNumber = models.IntegerField()
    Position = models.CharField(max_length=100,blank=True)
    MaritalStatus = models.CharField(max_length=100,blank=True)
    Blood_Group = models.CharField(max_length=50,choices=group)
    JobTitle = models.CharField(max_length=100, blank=True)
    WorkLocation = models.CharField(max_length=150, blank=True)
    DateOfJoining = models.DateField()
    Reporting_to = models.CharField(max_length =100, blank=True)
    Linkedin_link = models.URLField()
    profile_pic = models.ImageField(upload_to='images')
    

    def __str__(self):
        return self.Employee_name
