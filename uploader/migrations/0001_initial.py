# Generated by Django 4.2.7 on 2023-11-07 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_uploaded', models.FileField(null=True, upload_to='./uploads/')),
            ],
        ),
    ]
