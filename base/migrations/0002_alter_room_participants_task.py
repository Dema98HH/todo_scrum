# Generated by Django 4.0 on 2022-06-02 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='participants',
            field=models.ManyToManyField(related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(null=True)),
                ('finish', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('finished', models.DateTimeField(auto_now=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
