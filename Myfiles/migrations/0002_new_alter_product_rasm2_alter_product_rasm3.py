# Generated by Django 4.0 on 2021-12-10 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myfiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=30)),
                ('malumot', models.TextField()),
                ('rasm', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='rasm2',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='product',
            name='rasm3',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
