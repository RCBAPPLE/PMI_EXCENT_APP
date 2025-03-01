# Generated by Django 5.1.4 on 2025-01-22 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMI_eXcent_App', '0009_rename_id_question_suivante_oui_template_question_id_question_suivante_1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Causes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Partie', models.CharField(default='Mise en sécurité', max_length=100)),
                ('Indice', models.CharField(max_length=10)),
                ('cause_racine_1_FR', models.CharField(blank=True, max_length=100, null=True)),
                ('cause_racine_2_FR', models.CharField(blank=True, max_length=100, null=True)),
                ('resolution_1_FR', models.CharField(blank=True, max_length=100, null=True)),
                ('resolution_2_FR', models.CharField(blank=True, max_length=100, null=True)),
                ('cause_racine_1_EN', models.CharField(blank=True, max_length=100, null=True)),
                ('cause_racine_2_EN', models.CharField(blank=True, max_length=100, null=True)),
                ('resolution_1_EN', models.CharField(blank=True, max_length=100, null=True)),
                ('resolution_2_EN', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='template_question',
            name='id_question_suivante_3',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='template_question',
            name='id_question_suivante_4',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='template_question',
            name='id_question_suivante_5',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='template_question',
            name='partie_question_suivante_3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='template_question',
            name='partie_question_suivante_4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='template_question',
            name='partie_question_suivante_5',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
