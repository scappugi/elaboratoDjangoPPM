# Generated by Django 4.2.1 on 2023-06-02 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_category_alter_recipe_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]