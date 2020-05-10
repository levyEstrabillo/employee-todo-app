from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class EmployeeInfo(models.Model):
    #thumb = models.ImageField(upload_to='media', blank=True)
    fullname = models.CharField(max_length=50)
    Employee_code = models.CharField(max_length=50)
    address = models.TextField(max_length=150)
    birth = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, default=None)