# Generated by Django 4.0.1 on 2024-04-06 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkmodel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_record',
            name='viva_mark',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='course_record',
            name='attendance',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='course_record',
            name='output',
            field=models.BooleanField(default=True),
        ),
    ]
