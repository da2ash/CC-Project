# Generated by Django 2.0.2 on 2018-04-15 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appoint', '0003_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='report_image',
            field=models.FileField(upload_to='report/'),
        ),
    ]