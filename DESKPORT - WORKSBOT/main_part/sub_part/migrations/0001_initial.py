# Generated by Django 3.1.7 on 2021-03-14 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
    ]
