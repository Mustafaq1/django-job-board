# Generated by Django 3.1.4 on 2020-12-02 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_auto_20201202_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
