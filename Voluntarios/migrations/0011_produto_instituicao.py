# Generated by Django 3.1.1 on 2020-09-30 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Voluntarios', '0010_produto_endereco'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='Instituicao',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
