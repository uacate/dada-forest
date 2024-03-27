from django.db import models

class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

class URLSource(BaseModel):
    identifier = models.CharField(max_length=1000, unique=True, help_text="Unique identifier found in metadata")
    url = models.CharField(max_length=1000, unique=True, help_text="The metadata source url")
    description = models.CharField(max_length=2500, blank=True, help_text="Metadata description")
    title = models.CharField(max_length=250, blank=True, help_text="Metadata title")

    def __str__(self):
        return self.identifier
    
    def __repr__(self) -> str:
        return super().__repr__()
