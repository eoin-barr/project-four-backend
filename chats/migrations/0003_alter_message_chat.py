# Generated by Django 3.2.7 on 2021-09-10 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chats.chat'),
        ),
    ]
