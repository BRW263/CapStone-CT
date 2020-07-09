# Generated by Django 3.0.6 on 2020-07-09 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rosies_customs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=2)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='MyModels',
        ),
    ]
