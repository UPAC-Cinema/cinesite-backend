# Generated by Django 2.2.6 on 2019-11-04 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imdb_id', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=2048)),
                ('year', models.CharField(max_length=16)),
                ('mpaa_rating', models.CharField(max_length=8)),
                ('runtime', models.CharField(max_length=16)),
                ('genre', models.CharField(max_length=2048)),
                ('actors', models.CharField(max_length=2048)),
                ('writers', models.CharField(max_length=2048)),
                ('directors', models.CharField(max_length=2048)),
                ('plot', models.CharField(max_length=4096)),
                ('poster_url', models.CharField(max_length=2048)),
                ('trailer_url', models.CharField(max_length=2048)),
                ('rotten_tomatoes_rating', models.CharField(max_length=32)),
                ('image_path', models.CharField(max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='Showings',
            fields=[
                ('showing_pkey', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='last time seen')),
                ('time', models.TimeField(verbose_name='time shown')),
                ('attendance', models.IntegerField()),
                ('showing_id', models.IntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Movie')),
            ],
        ),
    ]
