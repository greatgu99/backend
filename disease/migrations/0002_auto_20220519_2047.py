# Generated by Django 3.1.4 on 2022-05-19 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='disease',
            options={'ordering': ['diseaseName']},
        ),
    ]
