# Generated by Django 5.0.3 on 2025-06-06 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0010_productos'),
    ]

    operations = [
        migrations.CreateModel(
            name='proveedores',
            fields=[
                ('nombre', models.CharField(max_length=200)),
                ('id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=500)),
                ('numero', models.IntegerField()),
                ('fecha_contrato', models.ImageField(upload_to='')),
            ],
        ),
    ]
