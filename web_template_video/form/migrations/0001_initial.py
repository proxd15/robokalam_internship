# Generated by Django 4.1.7 on 2023-04-27 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(default='', max_length=300)),
            ],
        ),
    ]
