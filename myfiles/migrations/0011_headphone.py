# Generated by Django 4.1.1 on 2022-09-12 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0010_newproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Headphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=30)),
                ('rasm1', models.ImageField(upload_to='media')),
                ('rasm2', models.ImageField(upload_to='media')),
                ('rasm3', models.ImageField(upload_to='media')),
                ('rasm4', models.ImageField(upload_to='media')),
                ('narxi', models.CharField(max_length=30)),
                ('chegirma', models.CharField(max_length=30)),
                ('vaqt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
