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
    image = models.ImageField(upload_to='masters/images')
    experience = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_status(self):
        if self.experience < 3:
            return "Новичок"
        elif 3 <= self.experience < 7:
            return "Мастер"
        elif 7 <= self.experience < 15:
            return "Опытный мастер"
        else:
            return "Эксперт"

    def __str__(self):
        return str(self.name)


class Skills(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    cat_name = models.CharField(
        max_length=100
    )  # Тоже что и name, но во множественном числе
    slug = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='skills/images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Workarea(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class PortfolioImage(models.Model):
    master = models.ForeignKey(Master, related_name="portfolio_images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='masters/portfolio/')

    def __str__(self):
        return f"Image for {self.master.name}"
