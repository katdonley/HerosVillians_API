# Generated by Django 4.0.2 on 2022-02-21 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0001_initial'),
        ('supers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='super',
            name='super_type',
        ),
        migrations.AddField(
            model_name='super',
            name='super_types',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='super_types.supertypes'),
        ),
    ]
