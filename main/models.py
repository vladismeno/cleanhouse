from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tasks'


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date = models.DateField()
    feedback = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'reviews'
