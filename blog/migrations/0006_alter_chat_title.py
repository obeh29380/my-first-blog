# Generated by Django 3.2.15 on 2022-08-10 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_chat_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]