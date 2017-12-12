from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True) # the value of description field is optional

    def __str__(self): # este método tiene 0 parametros
        """
        Devuelve la representación de un objeto como un string

        """
        return self.name

class Movie(models.Model):

    title = models.CharField(max_length=150)
    sumary = models.TextField()
    director_name = models.CharField(max_length=100)
    release_date = models.DateField()
    image = models.URLField()
    rating = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True) # saves the date when the object is created
    modified_at = models.DateTimeField(auto_now_add=True) # saves the date when the object is update

    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):  # este método tiene 0 parametros

        return self.title


