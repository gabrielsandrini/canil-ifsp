# Generated by Django 3.1.1 on 2020-09-19 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200918_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cachorro',
            name='pedigree',
            field=models.CharField(blank=True, max_length=45, null=True, unique=True),
        ),
    ]
