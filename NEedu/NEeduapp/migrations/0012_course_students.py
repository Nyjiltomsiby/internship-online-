# Generated by Django 5.0.4 on 2024-05-09 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NEeduapp', '0011_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(related_name='courses', to='NEeduapp.student'),
        ),
    ]