# Generated by Django 5.0.7 on 2024-08-10 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_staff_address_staff_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=20)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, max_length=200)),
            ],
        ),
    ]
