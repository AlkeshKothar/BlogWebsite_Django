# Generated by Django 3.2.5 on 2021-08-19 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AceInc', '0002_category_summary_feild'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(null=True, upload_to='upload'),
        ),
    ]