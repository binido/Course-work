# Generated by Django 5.1.2 on 2024-10-31 14:46

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handyman', '0004_mastertasks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedbacks',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('feedback', models.TextField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
