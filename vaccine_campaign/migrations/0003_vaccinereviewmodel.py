# Generated by Django 5.0.6 on 2024-07-08 08:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_alter_patientmodel_nid_alter_patientmodel_phone_and_more'),
        ('vaccine_campaign', '0002_vaccinedosebookingmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='VaccineReviewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviews', models.TextField()),
                ('rating', models.CharField(choices=[('⭐', '⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')], max_length=20)),
                ('reviewd_at', models.DateField(auto_now_add=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patientmodel')),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccine_campaign.vaccinecampaignmodel')),
            ],
        ),
    ]
