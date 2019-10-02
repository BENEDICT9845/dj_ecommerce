# Generated by Django 2.2.5 on 2019-10-02 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_auto_20191001_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='social',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='social',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='social',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='social',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='social',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='social',
            name='youtube',
            field=models.URLField(blank=True, null=True),
        ),
    ]
