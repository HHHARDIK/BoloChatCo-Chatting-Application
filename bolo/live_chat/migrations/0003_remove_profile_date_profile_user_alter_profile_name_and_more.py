# Generated by Django 4.1.3 on 2022-12-12 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('live_chat', '0002_remove_profile_user_profile_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='date',
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='live_chat.profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='ffriend',
            field=models.ManyToManyField(blank=True, null=True, related_name='my_friends', to='live_chat.friend'),
        ),
    ]
