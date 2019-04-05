# Generated by Django 2.2 on 2019-04-04 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nationalId', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('pokemonType', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
            ],
        ),
    ]