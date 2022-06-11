# Generated by Django 4.0.4 on 2022-06-11 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_category_alter_task_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='urgency',
            field=models.CharField(choices=[('high', 'high'), ('medium', 'medium'), ('low', 'low')], default='low', max_length=512),
        ),
    ]
