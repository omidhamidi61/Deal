# Generated by Django 3.0.2 on 2020-03-12 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_messagestable_dealers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammemberstable',
            name='member',
            field=models.ManyToManyField(related_name='workersTable3', to='app1.WorkersTable'),
        ),
    ]