# Generated by Django 4.0.4 on 2022-04-26 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='discussion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_discussion', models.CharField(default='NUEVA_DISCUSION', max_length=300)),
            ],
        ),
    ]
