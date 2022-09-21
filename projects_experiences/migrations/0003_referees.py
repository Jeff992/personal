# Generated by Django 4.1.1 on 2022-09-21 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_experiences', '0002_project_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Referees',
                'ordering': ['name'],
            },
        ),
    ]
