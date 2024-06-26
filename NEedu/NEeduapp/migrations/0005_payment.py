# Generated by Django 5.0.4 on 2024-05-01 12:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NEeduapp', '0004_usercourse_delete_category_course_mentor_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=50)),
                ('payment_id', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NEeduapp.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NEeduapp.usercourse')),
            ],
        ),
    ]
