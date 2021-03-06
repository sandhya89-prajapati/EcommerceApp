# Generated by Django 2.1.7 on 2020-01-16 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('EcommerceApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('qty', models.IntegerField()),
                ('desc', models.CharField(max_length=100)),
                ('pic', models.ImageField(blank=True, upload_to='proimage')),
                ('dated', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EcommerceApp.Profile')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Category')),
            ],
        ),
    ]
