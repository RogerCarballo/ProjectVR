# Generated by Django 2.2.5 on 2019-10-25 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VirtualReality', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='glasses',
            options={'verbose_name_plural': 'Glass'},
        ),
        migrations.AlterModelOptions(
            name='reservation',
            options={'verbose_name_plural': 'Room'},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name_plural': 'Room'},
        ),
    ]