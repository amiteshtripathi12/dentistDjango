# Generated by Django 4.0.2 on 2022-04-24 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_chefs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testmonials',
            fields=[
                ('Testmonials_id', models.AutoField(primary_key=True, serialize=False)),
                ('Testmonialsname', models.CharField(max_length=50)),
                ('Testmonialstitle', models.CharField(max_length=50)),
                ('Testmonialsdesc', models.CharField(max_length=200)),
            ],
        ),
    ]
