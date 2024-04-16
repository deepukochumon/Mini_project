# Generated by Django 5.0.3 on 2024-03-31 05:55

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_academics_students_acad_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Calender',
            fields=[
                ('i', models.AutoField(primary_key=True, serialize=False)),
                ('dates', models.DateField()),
                ('day', models.CharField(choices=[('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday')], default=None, max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('total_students', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=50)),
                ('credits', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('period_id', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)])),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('fac_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('f_password', models.CharField(max_length=30)),
                ('f_name', models.CharField(max_length=20)),
                ('l_name', models.CharField(max_length=20)),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.department')),
            ],
        ),
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.class')),
                ('fac_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stud_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('s_password', models.CharField(max_length=30)),
                ('in_out', models.CharField(max_length=5)),
                ('f_name', models.CharField(max_length=20)),
                ('l_name', models.CharField(max_length=20)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.class')),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.department')),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=100)),
                ('leave_type', models.CharField(choices=[('ml', 'Medical Leave'), ('od', 'On Duty')], default=None, max_length=9)),
                ('approved', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('stud_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.student')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('presence', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('periods', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)])),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.course')),
                ('fac_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.faculty')),
                ('stud_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.student')),
            ],
            options={
                'unique_together': {('stud_id', 'course_id', 'date')},
            },
        ),
        migrations.CreateModel(
            name='Teache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.class')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.course')),
                ('fac_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.faculty')),
            ],
            options={
                'unique_together': {('course_id', 'class_id')},
            },
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday')], default=None, max_length=9)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.class')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.course')),
                ('periods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.slot')),
            ],
            options={
                'unique_together': {('class_id', 'course_id', 'day', 'periods')},
            },
        ),
    ]
