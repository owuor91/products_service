# Generated by Django 2.0.13 on 2019-03-25 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20190325_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='is_global',
            field=models.BooleanField(default=False, help_text='All organizations have access to global categories.'),
        ),
    ]
