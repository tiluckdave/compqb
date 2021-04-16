# Generated by Django 3.2 on 2021-04-16 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.CharField(choices=[('IM', 'Information Management'), ('CN', 'Computer Networks'), ('RDBMS', 'Relational Database Management System')], default='IM', max_length=100),
            preserve_default=False,
        ),
    ]
