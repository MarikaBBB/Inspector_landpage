# Generated by Django 4.1.7 on 2023-04-01 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('last_name', 'first_name')},
        ),
    ]
