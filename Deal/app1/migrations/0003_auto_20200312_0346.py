# Generated by Django 3.0.2 on 2020-03-12 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_teammemberstable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammemberstable',
            name='member',
        ),
        migrations.AddField(
            model_name='teammemberstable',
            name='member',
            field=models.ManyToManyField(to='app1.WorkersTable'),
        ),
    ]
