# Generated by Django 5.0.3 on 2024-06-23 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0007_delete_creacionboleta'),
    ]

    operations = [
        migrations.AddField(
            model_name='boletamodel',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
