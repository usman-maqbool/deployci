# Generated by Django 3.1.4 on 2021-01-12 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]