# Generated by Django 4.0 on 2021-12-16 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myfiles', '0004_comment_murojatlar'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='tur',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
