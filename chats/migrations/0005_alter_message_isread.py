# Generated by Django 3.2.7 on 2021-09-15 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0004_message_isread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='isRead',
            field=models.BooleanField(),
        ),
    ]
