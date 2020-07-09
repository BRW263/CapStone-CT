# Generated by Django 3.0.6 on 2020-07-07 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rosies_customs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('08', '08oz'), ('16', '16oz'), ('20', '20oz'), ('32', '32oz'), ('40', '40oz')], default='T', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], default='P', max_length=1),
            preserve_default=False,
        ),
    ]
