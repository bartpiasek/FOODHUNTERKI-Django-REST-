# Generated by Django 3.0.8 on 2020-07-16 20:19

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('address', models.CharField(max_length=100, unique=True)),
                ('city', models.CharField(default='Poznan', max_length=50)),
                ('prices', models.IntegerField(choices=[(0, 'Low price'), (1, 'Medium price'), (2, 'High price')], null=True)),
                ('image', models.ImageField(default='Image', upload_to='placesimage/')),
                ('contact', models.URLField(max_length=80, null=True, unique=True, verbose_name='Facebook link')),
                ('description', models.TextField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='foodhunterkiapi.Place')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodhunterkiapi.Place')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'place')},
                'index_together': {('user', 'place')},
            },
        ),
    ]