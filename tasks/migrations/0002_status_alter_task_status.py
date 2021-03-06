# Generated by Django 4.0.4 on 2022-05-04 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.CharField(max_length=128, unique='todo')),
                ('working', models.CharField(max_length=128, unique='working')),
                ('done', models.CharField(max_length=128, unique='done')),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.status'),
        ),
    ]
