# Generated by Django 2.2.dev20181222235254 on 2018-12-24 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.Store'),
            preserve_default=False,
        ),
    ]