from django.db import models

# Create your models here.
class contests(models.Model):
    contest_id=models.IntegerField()
    hacker_id=models.IntegerField()
    name=models.CharField(max_length=10)
    sums_of_total_submissions=models.IntegerField()
    total_accepted_submssions=models.IntegerField()
    total_views=models.IntegerField()
    total_unique_views=models.IntegerField()

