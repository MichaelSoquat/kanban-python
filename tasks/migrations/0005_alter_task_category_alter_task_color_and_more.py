# Generated by Django 4.0.4 on 2022-06-09 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_category_task_color_task_urgency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='color',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='urgency',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
