# Generated by Django 3.0.4 on 2020-04-19 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Actor', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Movie', models.CharField(max_length=255)),
                ('Actor', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Movieapp.Actor')),
            ],
        ),
    ]
