# Generated by Django 5.1.2 on 2024-11-02 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patrimoine', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pvrecensement',
            old_name='Chapitre_article',
            new_name='Designation_chapitre',
        ),
        migrations.RenameField(
            model_name='pvrecensement',
            old_name='Nom_et_qualite_du_recenseur',
            new_name='Designation_magasin_ou_materiels_service',
        ),
        migrations.RenameField(
            model_name='pvrecensement',
            old_name='imputation_administrative',
            new_name='Imputation_administrative',
        ),
        migrations.RenameField(
            model_name='pvrecensement',
            old_name='libelle_article',
            new_name='Libelle_article',
        ),
        migrations.RenameField(
            model_name='pvrecensement',
            old_name='Nom_et_qualite_du_depositaire_comptable',
            new_name='Nom_et_qualite_depositaire_comptable',
        ),
        migrations.AddField(
            model_name='pvrecensement',
            name='Nom_et_qualite_recenseur',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
