# Generated by Django 4.1.3 on 2022-12-25 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_chat', '0008_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
