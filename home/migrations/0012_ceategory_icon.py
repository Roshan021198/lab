# Generated by Django 3.1.5 on 2021-01-29 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='ceategory',
            name='icon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
