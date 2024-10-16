from django.db import models
import uuid


class Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=100)
    tel = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)

    # Master group only
    skill = models.CharField(max_length=100, blank=True)
    work_period = models.CharField(max_length=100, blank=True)
    weekend = models.CharField(max_length=100, blank=True)
    salary = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.email)
