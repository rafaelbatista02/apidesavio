# Generated by Django 3.1.1 on 2020-09-30 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Voluntarios', '0017_auto_20200930_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('Doação Verbas', 'VERBAS'), ('Doação de equipamentos', 'EQUIPAMENTOS')], max_length=100),
        ),
    ]
