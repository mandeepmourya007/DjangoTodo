# Generated by Django 3.2.7 on 2022-11-19 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('task_status', models.PositiveIntegerField(choices=[(10, 'Pending'), (20, 'Completed'), (30, 'Cancelled')], default=10, verbose_name='task status')),
                ('detail', models.TextField()),
            ],
            options={
                'verbose_name': 'task',
                'verbose_name_plural': 'tasks',
            },
        ),
    ]