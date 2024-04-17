# Generated by Django 4.2.10 on 2024-03-15 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brandauto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок меню')),
                ('url_name', models.CharField(max_length=255, verbose_name='URL меню')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
                'ordering': ['id'],
            },
        ),
    ]
