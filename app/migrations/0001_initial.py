# Generated by Django 3.0.2 on 2020-03-05 23:30

import app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Locataire',
            fields=[
                ('numLocataire', models.AutoField(primary_key=True, serialize=False)),
                ('nomLocataire', models.CharField(max_length=150)),
                ('prenomLocataire', models.CharField(max_length=150)),
                ('telephoneLocataire', models.IntegerField()),
                ('mailLocataire', models.EmailField(max_length=150)),
                ('profession', models.CharField(max_length=150)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'locataire',
            },
        ),
        migrations.CreateModel(
            name='Logement',
            fields=[
                ('numLogement', models.AutoField(primary_key=True, serialize=False)),
                ('typeL', models.CharField(choices=[('T1 avec cuisine non séparée', 'Studio'), ('1 pièce principale (à la fois chambre et salon) + 1 cuisine + 1 salle de bains (avec WC séparés ou inclus)', 'T1'), ('2 pièces (1 chambre + 1 salon) + 1 cuisine + 1 salle de bains (avec WC séparés ou inclus)', 'T2'), ('2 pièces (1 chambre + 1 salon) dont l’une est suffisamment grande pour être séparée en deux zones distinctes + 1 cuisine + 1 salle de bains (avec WC séparés ou inclus)', 'T2 Bis'), ('3 pièces (2 chambres + 1 salon) + 1 cuisine + 1 salle de bains (avec WC séparés ou inclus)', 'T3'), (' 3 pièces (2 chambres + 1 salon) dont l’une est suffisamment grande pour être séparée en deux zones distinctes + 1 cuisine + 1 salle de bains (avec WC séparés ou inclus)', 'T3 Bis'), ('4 pièces (3 chambres + 1 salon/séjour OU 2 chambres + 1 salon + 1 salle à manger) + 1 cuisine + 1 salle de bains (avec WC séparés ou inclus)', 'T4'), (' T4 transformé en T3 en réunissant deux pièces pour en faire 1 grande', 'T3 T4'), (' 5 pièces (4 chambres + 1 salon/séjour OU 3 chambres + 1 salon + 1 salle à manger) + 1 cuisine + 1 salle de bains ou + (avec WC séparés ou inclus)', 'T5')], max_length=200)),
                ('superficie', models.IntegerField()),
                ('loyer', models.IntegerField()),
                ('photoL1', models.FileField(blank=True, null=True, upload_to=app.models.Logement.upload_path)),
                ('photoL2', models.FileField(blank=True, null=True, upload_to=app.models.Logement.upload_path)),
                ('photoL3', models.FileField(blank=True, null=True, upload_to=app.models.Logement.upload_path)),
            ],
            options={
                'db_table': 'logement',
            },
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('idPaiement', models.AutoField(primary_key=True, serialize=False)),
                ('montantP', models.IntegerField()),
                ('datePaie', models.DateTimeField(auto_now_add=True)),
                ('numLocataire', models.ForeignKey(db_column='numLocataire', on_delete=django.db.models.deletion.CASCADE, to='app.Locataire')),
                ('numLogement', models.ForeignKey(db_column='numLogement', on_delete=django.db.models.deletion.CASCADE, to='app.Logement')),
            ],
            options={
                'db_table': 'paiement',
            },
        ),
        migrations.CreateModel(
            name='Maison',
            fields=[
                ('numM', models.AutoField(primary_key=True, serialize=False)),
                ('nomM', models.CharField(blank=True, max_length=150)),
                ('numRueM', models.IntegerField()),
                ('adresseM', models.CharField(max_length=150)),
                ('codePostalM', models.CharField(max_length=5)),
                ('villeM', models.CharField(max_length=150)),
                ('photoM1', models.FileField(blank=True, null=True, upload_to=app.models.Maison.upload_path)),
                ('photoM2', models.FileField(blank=True, null=True, upload_to=app.models.Maison.upload_path)),
                ('photoM3', models.FileField(blank=True, null=True, upload_to=app.models.Maison.upload_path)),
                ('numP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'maison',
            },
        ),
        migrations.AddField(
            model_name='logement',
            name='numM',
            field=models.ForeignKey(db_column='numM', on_delete=django.db.models.deletion.CASCADE, to='app.Maison'),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('idLocation', models.AutoField(primary_key=True, serialize=False)),
                ('dateDebut', models.DateField()),
                ('dateFin', models.DateField()),
                ('numLocataire', models.ForeignKey(db_column='numLocataire', on_delete=django.db.models.deletion.CASCADE, to='app.Locataire')),
                ('numLogement', models.ForeignKey(db_column='numLogement', on_delete=django.db.models.deletion.CASCADE, to='app.Logement')),
            ],
            options={
                'db_table': 'location',
            },
        ),
        migrations.CreateModel(
            name='Depenser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montantD', models.IntegerField()),
                ('dateD', models.DateTimeField(auto_now_add=True)),
                ('descriptionD', models.CharField(max_length=300)),
                ('numLogement', models.ForeignKey(db_column='numLogement', on_delete=django.db.models.deletion.CASCADE, to='app.Logement')),
                ('numP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'depenser',
            },
        ),
    ]
