# Generated by Django 3.0.3 on 2020-03-26 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id_name', models.AutoField(primary_key=True, serialize=False)),
                ('titel_name', models.CharField(max_length=30)),
                ('aticel', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'test',
                'managed': False,
            },
        ),
    ]
