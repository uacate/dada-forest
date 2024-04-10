from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Document(BaseModel):
    identifier = models.CharField(max_length=250, null=False, unique=True)
    url = models.CharField(max_length=250, null=True, unique=True)
    description = models.CharField(max_length=2500, null=True, unique=False)

    def __str__(self) -> str:
        return self.id
        # return super().__str__()
