# Generated by Django 4.2.1 on 2023-06-20 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='journaluseform',
            name='image',
            field=models.ImageField(blank=True, upload_to='picture/'),
        ),
    ]