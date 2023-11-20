# Generated by Django 4.2.1 on 2023-11-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campo',
            name='opcoes_seletor',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='campo',
            name='valor_padrao',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='campo',
            name='tipo',
            field=models.CharField(choices=[('checkbox', 'Checkbox'), ('texto', 'Texto'), ('seletor', 'Seletor'), ('arquivo', 'Arquivo')], max_length=20),
        ),
    ]
