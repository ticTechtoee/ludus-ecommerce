# Generated by Django 4.2.7 on 2024-03-09 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0004_color_color_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='homeApp.category'),
            preserve_default=False,
        ),
    ]
