# Generated by Django 3.2.15 on 2022-08-10 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
