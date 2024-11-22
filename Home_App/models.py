from django.db import models

# Create your models here.
class Book_Table(models.Model):  # Changed class name to follow PEP 8
    name = models.CharField(max_length=55)  # Changed to lowercase
    email = models.EmailField(max_length=55)  # Changed to lowercase
    phone_number = models.IntegerField()  # Removed max_length
    date = models.DateField()  # Changed from Datefield to DateField
    person = models.IntegerField()  # Changed from Integerfield to IntegerField

    def __str__(self):
        return f"{self.name} - {self.date}"  # Optional string representation
