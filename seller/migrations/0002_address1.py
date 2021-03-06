# Generated by Django 2.1.7 on 2020-04-17 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EcommerceApp', '0003_remove_profile_profile_pic'),
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=12)),
                ('pincode', models.IntegerField()),
                ('locality', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=30)),
                ('landmark', models.CharField(max_length=40)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EcommerceApp.Profile')),
            ],
        ),
    ]
