from django.db import models
import uuid


class Master(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    skill = models.ForeignKey(
        to="Skills", on_delete=models.PROTECT, blank=True, null=True
    )
    workarea = models.ForeignKey(
        to="Workarea", on_delete=models.PROTECT, blank=True, null=True
    )
    image = models.ImageField(upload_to='masters/images', height_field=None, width_field=None, max_length=None)
    experience = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Skills(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    cat_name = models.CharField(
        max_length=100
    )  # Тоже что и name, но во множественном числе
    slug = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Workarea(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
