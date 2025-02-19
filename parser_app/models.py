from django.db import models

class RezkaModel(models.Model):
    title = models.CharField(max_length=500)

    def str(self):
        return self.title



