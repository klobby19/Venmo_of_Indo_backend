from django.db import models

class Message(models.Model):
    message = models.CharField(max_length=120)
    is_read = models.BooleanField(default=False)

class Meta:
    db_table = 'message'

    def __str__(self):
        return self.message