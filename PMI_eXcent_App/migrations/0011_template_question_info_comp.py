# Generated by Django 5.1.4 on 2025-01-22 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMI_eXcent_App', '0010_causes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='template_question',
            name='info_comp',
            field=models.TextField(default=''),
        ),
    ]
