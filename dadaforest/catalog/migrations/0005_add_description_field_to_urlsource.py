# Generated by Django 5.0.3 on 2024-03-27 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_urlsource_identifier_alter_urlsource_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlsource',
            name='description',
            field=models.CharField(blank=True, max_length=2500),
        ),
    ]
