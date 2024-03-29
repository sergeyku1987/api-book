# Generated by Django 3.2.16 on 2024-03-06 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('year', models.PositiveSmallIntegerField()),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.category')),
            ],
        ),
    ]
