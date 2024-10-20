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

    def __str__(self):
        return str(self.email)


class Master(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    skill = models.ForeignKey(
        to="Skills", on_delete=models.PROTECT, blank=True, null=True
    )
    work_period = models.CharField(max_length=100)
    weekend = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    grade = models.ForeignKey(
        to="Grade", on_delete=models.CASCADE, blank=True, null=True
    )  # Оценка
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)  # Статус заявки

    def __str__(self):
        return str(self.name)


class Skills(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    cat_name = models.CharField(max_length=100) # Тоже что и name, но во множественном числе
    slug = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Grade(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.value)


class Feedback(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    discription = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    master = models.ForeignKey(Master, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.discription)
