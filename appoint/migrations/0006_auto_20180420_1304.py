# Generated by Django 2.0.2 on 2018-04-20 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appoint', '0005_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_query', to='appoint.SignUp'),
        ),
    ]
