from django.db import models
# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk},{self.name},{self.age},{self.date}"