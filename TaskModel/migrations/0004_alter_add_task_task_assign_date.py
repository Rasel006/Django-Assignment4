# Generated by Django 4.2.7 on 2023-12-09 05:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('TaskModel', '0003_rename_is_completed_add_task_is_completed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_task',
            name='Task_assign_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, help_text='You can Enter task assignment date or set it default now', null=True),
        ),
    ]
