# Generated by Django 2.1.7 on 2019-04-09 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_user_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='syafiq', max_length=50),
            preserve_default=False,
        ),
    ]