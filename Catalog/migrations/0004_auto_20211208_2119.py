# Generated by Django 3.2.9 on 2021-12-08 15:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0003_alter_bookinstance_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter the book's natural language (e.g. English, Hindi, French, etc.", max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('cef2958b-bca0-4534-8785-431d7bf4ff48'), help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
    ]
