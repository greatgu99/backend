# Generated by Django 3.1.4 on 2022-04-09 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diseaseName', models.CharField(max_length=40)),
                ('diseaseDescription', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]