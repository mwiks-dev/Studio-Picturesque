# Generated by Django 3.2.8 on 2021-11-27 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleria', '0002_rename_picture_pictures'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='pictures',
            options={'ordering': ['name']},
        ),
    ]
