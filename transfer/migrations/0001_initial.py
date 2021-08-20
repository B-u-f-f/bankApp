# Generated by Django 3.2.6 on 2021-08-19 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.TextField()),
                ('customer_email', models.EmailField(max_length=254)),
                ('customer_balance', models.IntegerField()),
            ],
        ),
    ]
