# Generated by Django 4.2.13 on 2024-05-31 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soc', '0002_alter_odbor_nazov'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dostupnost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazov', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Dostupnosť',
                'verbose_name_plural': 'Dostupnosť',
            },
        ),
    ]
