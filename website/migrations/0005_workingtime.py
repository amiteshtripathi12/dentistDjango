# Generated by Django 4.0.2 on 2022-04-22 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_service_image_alter_service_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkingTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.CharField(max_length=10)),
                ('Days', models.CharField(max_length=50)),
            ],
        ),
    ]