# Generated by Django 2.1.7 on 2019-04-09 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analis', '0002_proyek_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='perangkat',
            name='proyek',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='analis.proyek'),
            preserve_default=False,
        ),
    ]
