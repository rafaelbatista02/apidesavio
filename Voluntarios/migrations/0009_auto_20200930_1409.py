# Generated by Django 3.1.1 on 2020-09-30 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Voluntarios', '0008_auto_20200930_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('Doação Verbas', 'DOAÇÃO DE VERBAS'), ('Doação de equipamentos', 'DOAÇÃO DE EQUIPAMENTOS')], max_length=100),
        ),
    ]