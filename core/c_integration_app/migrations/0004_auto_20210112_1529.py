# Generated by Django 3.1.4 on 2021-01-12 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('c_integration_app', '0003_auto_20210112_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ci_jobs',
            name='deploy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='c_integration_app.ci_deploy'),
        ),
    ]