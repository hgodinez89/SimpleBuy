# Generated by Django 3.0.1 on 2020-03-22 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_language_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='language_code',
        ),
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('es', 'Español')], default='en', max_length=5),
        ),
    ]
