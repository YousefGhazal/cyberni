# Generated by Django 4.1.5 on 2023-06-16 08:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_alter_profile_mobile"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Gender",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="email",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="gender",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="name",
        ),
    ]