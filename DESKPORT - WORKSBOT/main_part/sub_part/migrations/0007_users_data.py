# Generated by Django 3.1.7 on 2021-03-17 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0006_staffs_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('useremail', models.CharField(max_length=40)),
                ('userstatus', models.CharField(max_length=20)),
                ('userpassword', models.CharField(max_length=16)),
            ],
        ),
    ]
