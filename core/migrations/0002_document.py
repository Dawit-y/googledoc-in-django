# Generated by Django 5.0.1 on 2024-01-13 22:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.FileField(upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authored', to=settings.AUTH_USER_MODEL)),
                ('collaborators', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='colaborate_on', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
