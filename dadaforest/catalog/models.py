from django.db import models

class URLSource(models.Model):
    identifier = models.CharField(max_length=1000, blank=True)
    url = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.identifier
    
    def __repr__(self) -> str:
        return super().__repr__()
