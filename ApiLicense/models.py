from django.db import models

class License(models.Model):
    
    company_name = models.CharField(max_length=50, blank=False)
    user_full_name= models.CharField(max_length=50, null=False, unique=True,blank=False)
    job_title = models.CharField(max_length=20,blank=False)
    user_email = models.EmailField(max_length=50, null=False, unique=True, blank=False)
    software_user_name = models.CharField(max_length=50, unique=True, blank=False)
    expiration_date = models.DateField(null=False, blank=False)
    version = models.CharField(max_length=10,null=False, blank=False)
    
    def __str__(self):
        return self.user_full_name + ' ' + self.job_title + ', user: ' + self.software_user_name
    