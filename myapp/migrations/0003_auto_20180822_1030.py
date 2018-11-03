# Generated by Django 2.0.6 on 2018-08-22 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20180821_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='tag_article',
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(through='myapp.Article_Tag', to='myapp.Tag'),
        ),
    ]
