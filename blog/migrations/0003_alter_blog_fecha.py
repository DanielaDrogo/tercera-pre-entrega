# Generated by Django 5.0.6 on 2024-07-03 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_cuerpo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]