# Generated by Django 5.1.4 on 2025-01-22 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMI_eXcent_App', '0011_template_question_info_comp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template_question',
            name='info_comp',
            field=models.TextField(blank=True, default=''),
        ),
    ]
