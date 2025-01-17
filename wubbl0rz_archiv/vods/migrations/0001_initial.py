# Generated by Django 4.0.2 on 2022-02-03 17:33

from django.db import migrations, models
import vods.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vod',
            fields=[
                ('uuid', models.SlugField(default=vods.models.gen_id, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.TextField()),
                ('duration', models.PositiveIntegerField()),
                ('date', models.DateTimeField()),
                ('filename', models.SlugField()),
                ('resolution', models.TextField(blank=True, null=True)),
                ('fps', models.FloatField(blank=True, null=True)),
                ('size', models.PositiveBigIntegerField(blank=True, null=True)),
                ('publish', models.BooleanField(default=True)),
            ],
        ),
    ]
