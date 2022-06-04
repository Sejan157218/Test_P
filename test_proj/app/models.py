from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    image = models.FileField(upload_to='upload/', null=True, blank=True)

    def __str__(self):
        return self.name