# Generated by Django 3.2.7 on 2021-09-09 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats_a', to=settings.AUTH_USER_MODEL)),
                ('user_b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats_b', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]