# Generated by Django 3.2.9 on 2021-12-09 17:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0009_alter_bookinstance_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Catalog.language'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('9d589d7c-8fed-46ca-9da8-845ca30169d5'), help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
    ]
