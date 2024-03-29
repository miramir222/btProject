# Generated by Django 2.2.12 on 2020-05-04 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=16)),
                ('message', models.TextField(blank=True)),
                ('contact_date', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.IntegerField(blank=True)),
                ('listing_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.Listing')),
            ],
        ),
    ]
