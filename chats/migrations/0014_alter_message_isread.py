# Generated by Django 3.2.7 on 2021-09-15 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0013_alter_message_isread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='isRead',
            field=models.BooleanField(default=False),
        ),
    ]
