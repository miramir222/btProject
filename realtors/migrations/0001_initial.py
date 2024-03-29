# Generated by Django 2.2.12 on 2020-05-02 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('description', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=50)),
                ('is_mvp', models.BooleanField(default=False)),
                ('hire_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
