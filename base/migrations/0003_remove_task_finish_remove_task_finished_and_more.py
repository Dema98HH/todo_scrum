# Generated by Django 4.0 on 2022-06-02 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('base', '0002_alter_room_participants_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='finish',
        ),
        migrations.RemoveField(
            model_name='task',
            name='finished',
        ),
        migrations.AddField(
            model_name='task',
            name='hostroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.room'),
        ),
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='host',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user'),
        ),
    ]
