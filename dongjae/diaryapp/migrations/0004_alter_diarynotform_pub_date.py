# Generated by Django 4.2.1 on 2023-06-20 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaryapp', '0003_alter_diarynotform_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diarynotform',
            name='pub_date',
            field=models.DateTimeField(verbose_name='data published'),
        ),
    ]
