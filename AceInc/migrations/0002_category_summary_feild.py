# Generated by Django 3.2.5 on 2021-08-19 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AceInc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='summary_feild',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]