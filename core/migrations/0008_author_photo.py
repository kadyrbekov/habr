# Generated by Django 3.1.7 on 2021-03-29 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_article_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo', verbose_name='Photo name'),
        ),
    ]