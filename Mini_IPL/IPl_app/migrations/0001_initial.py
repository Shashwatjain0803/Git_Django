# Generated by Django 4.1.7 on 2023-03-13 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=25)),
                ('nick_name', models.CharField(max_length=5)),
            ],
        ),
    ]
