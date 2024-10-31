from django.db import models
import uuid

from django.urls import reverse


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

    def get_absolute_url(self):
        return reverse('master_page', args=[self.skill.slug, self.id])

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


class MasterTasks(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает выполнения'),
        ('in_progress', 'Выполняется'),
        ('completed', 'Выполнено'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    master_type = models.ForeignKey('Skills', on_delete=models.PROTECT)
    client_name = models.CharField(max_length=100)
    client_tel = models.CharField(max_length=100)
    client_adders = models.CharField(max_length=100)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
    )

    def set_in_progress(self):
        self.status = 'in_progress'
        self.save()

    def set_completed(self):
        self.status = 'completed'
        self.save()
