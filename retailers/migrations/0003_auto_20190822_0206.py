# Generated by Django 2.2.4 on 2019-08-22 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retailers', '0002_auto_20190822_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailer',
            name='contacts',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='link',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='rating',
            field=models.IntegerField(blank=True, default=2.5),
        ),
    ]