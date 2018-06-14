# Generated by Django 2.0.5 on 2018-06-14 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0002_biography_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='biography',
            options={'ordering': ''},
        ),
        migrations.AddField(
            model_name='biography',
            name='backgound_pic',
            field=models.ImageField(default='background_pic/default.png', null=True, upload_to='background_pic', verbose_name='BACKGROUND_PICTURE'),
        ),
        migrations.AlterField(
            model_name='biography',
            name='profile_pic',
            field=models.ImageField(default='profile_pic/anonymous.png', null=True, upload_to='profile_pic', verbose_name='PROFILE_PICTURE'),
        ),
    ]