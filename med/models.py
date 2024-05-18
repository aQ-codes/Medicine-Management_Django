from django.db import models


# Create your models here.
class Medicine(models.Model):
    CATEGORY = (
        ('Ayurveda', 'Ayurveda'),
        ('Allopathy', 'Allopathy'),
        ('Homeopathy', 'Homeopathy'),
        )
    name = models.CharField(max_length = 200, null = True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length = 200, null = True, choices = CATEGORY)
    description = models.TextField(max_length = 100, null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True) 
    def __str__(self):  
        return self.name 

