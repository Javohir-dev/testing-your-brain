# Generated by Django 4.0 on 2023-08-01 11:46

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('maximum_attemps', models.PositiveIntegerField()),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=datetime.datetime(2023, 8, 11, 11, 46, 39, 943172, tzinfo=utc))),
                ('pass_percentage', models.PositiveIntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('a', models.CharField(max_length=150)),
                ('b', models.CharField(max_length=150)),
                ('c', models.CharField(max_length=150)),
                ('d', models.CharField(max_length=150)),
                ('true_answer', models.CharField(help_text='E.x: a', max_length=150)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.test')),
            ],
        ),
    ]