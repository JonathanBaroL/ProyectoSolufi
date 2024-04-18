# Generated by Django 3.2.12 on 2024-04-18 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListaCarros',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'ListaCarros',
                'managed': False,
            },
        ),
    ]
