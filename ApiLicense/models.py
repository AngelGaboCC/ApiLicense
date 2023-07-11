from django.db import models

class License(models.Model):
    
    company_name = models.CharField(max_length=100, blank=False, null=False)
    user_full_name= models.CharField(max_length=100, null=False,blank=False)
    job_title = models.CharField(max_length=50,blank=False, null=False)
    user_email = models.EmailField(max_length=100, null=False, blank=False)
    software_name = models.CharField(max_length=50, blank=False, null=False,  default='software_name')
    software_user_name = models.CharField(max_length=50, blank=False, null=False)
    expiration_date = models.DateField(null=False, blank=False)
    version = models.CharField(max_length=10,null=False, blank=False)
    
    class Meta:
        unique_together = ('software_name', 'software_user_name', 'version')
        
    def __str__(self):
        return self.user_full_name + ' ' + self.job_title + ', user: ' + self.software_user_name
    
    
    