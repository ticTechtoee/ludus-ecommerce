# Generated by Django 4.2.7 on 2024-03-09 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0005_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homeApp.maincategory')),
            ],
            options={
                'verbose_name_plural': 'MainCategory Categories',
            },
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
    ]
