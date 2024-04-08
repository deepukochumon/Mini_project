# Generated by Django 4.0.1 on 2024-04-06 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkmodel', '0003_alter_class_section_advisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_diary',
            name='lab_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='diary', to='checkmodel.lab'),
        ),
        migrations.AlterUniqueTogether(
            name='course_diary',
            unique_together={('batches', 'lab_name')},
        ),
    ]