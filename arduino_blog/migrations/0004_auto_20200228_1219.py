# Generated by Django 3.0.3 on 2020-02-28 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arduino_blog', '0003_auto_20200228_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposal',
            name='creation_date',
        ),
        migrations.AlterField(
            model_name='proposal',
            name='approval_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='completion_date',
            field=models.DateTimeField(),
        ),
    ]
