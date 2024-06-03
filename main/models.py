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

    def user_directory_path(self, filename=None):
        return f'reviews/user_{self.id}.png'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date = models.DateField()
    feedback = models.TextField()
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'reviews'
