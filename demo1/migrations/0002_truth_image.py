# Generated by Django 3.0.2 on 2020-03-03 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='truth',
            name='image',
            field=models.FileField(default='', upload_to='images/'),
        ),
    ]