# Generated by Django 4.0.1 on 2024-04-06 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkmodel', '0002_course_record_viva_mark_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class_section',
            name='advisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advising_class', to='checkmodel.faculty'),
        ),
    ]