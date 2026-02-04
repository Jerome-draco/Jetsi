from django.db import models

# Create your models here.
class Response(models.Model):
    answer = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"She said {self.answer} at {self.created_at}"