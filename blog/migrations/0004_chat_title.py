# Generated by Django 3.2.15 on 2022-08-10 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_chat_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='title',
            field=models.TextField(default=''),
        ),
    ]
