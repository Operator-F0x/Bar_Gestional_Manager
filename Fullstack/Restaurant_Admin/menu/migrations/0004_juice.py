# Generated by Django 5.1.1 on 2024-09-29 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_rename_menu_menucold'),
    ]

    operations = [
        migrations.CreateModel(
            name='juice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=120)),
                ('price', models.FloatField()),
            ],
        ),
    ]
