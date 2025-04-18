from django.db import models

# Create your models here.
class BookData(models.Model):

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()

    genre_choices = [  
        ('Fiction','Fiction'),
        ('Non-Fiction','Non-Fiction'),
        ('Science','Science'),
        ('Technology','Technology'),
        ('History','History'),
        ('Adventure','Adventure'),
        ('Horror','Horror'),
        ('Other','Other'),
    ]
    genre = models.CharField(max_length=50,choices=genre_choices)
    
    isbn = models.CharField(max_length=13, unique=True) 
    publication_data = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.title