# Generated by Django 3.0.2 on 2020-03-12 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20200312_0346'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagestable',
            name='dealers',
            field=models.ManyToManyField(related_name='workersTable2', to='app1.WorkersTable'),
        ),
    ]