from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from datetime import datetime, date

from listings.models import Listing

# Create your models here.
class Rating(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField('message')
    star = models .IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    date_comment = models.DateField(default = date.today)
    proid = models.ForeignKey(Listing, on_delete = models.CASCADE, related_name= "id+")
    
