# Generated by Django 4.1.1 on 2022-09-10 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='murojaat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.CharField(max_length=10)),
                ('vaqt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
