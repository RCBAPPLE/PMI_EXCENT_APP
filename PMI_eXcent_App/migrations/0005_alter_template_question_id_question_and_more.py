# Generated by Django 5.1.4 on 2024-12-30 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMI_eXcent_App', '0004_template_question_remove_choice_question_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template_question',
            name='id_question',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='template_question',
            name='partie',
            field=models.CharField(max_length=100),
        ),
    ]
