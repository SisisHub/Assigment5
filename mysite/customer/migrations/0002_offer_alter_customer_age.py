# Generated by Django 4.1.2 on 2022-10-30 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=255)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.FloatField(),
        ),
    ]
