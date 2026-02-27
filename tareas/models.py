from django.db import models

class Tarea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    dateLimit = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title