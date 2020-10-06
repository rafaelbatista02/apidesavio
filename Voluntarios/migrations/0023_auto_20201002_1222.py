# Generated by Django 3.1.1 on 2020-10-02 15:22

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('Voluntarios', '0022_auto_20201002_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Continente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('continente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Voluntarios.continente')),
                ('country', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='continent', chained_model_field='continent', on_delete=django.db.models.deletion.CASCADE, to='Voluntarios.cidade')),
            ],
        ),
        migrations.RemoveField(
            model_name='produto',
            name='Estado',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.AddField(
            model_name='cidade',
            name='continent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Voluntarios.continente'),
        ),
    ]