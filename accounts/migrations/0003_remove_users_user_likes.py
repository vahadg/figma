# Generated by Django 4.0.3 on 2022-04-09 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_orders_alter_users_user_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='user_likes',
        ),
    ]
