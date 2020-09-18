# Generated by Django 3.1.1 on 2020-09-18 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200917_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cachorro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('raca', models.CharField(blank=True, max_length=45, null=True)),
                ('cor', models.CharField(max_length=80)),
                ('porte', models.CharField(max_length=45)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('pedigree', models.CharField(max_length=45, unique=True)),
                ('caracteristicas_extras', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Cachorros',
            },
        ),
        migrations.CreateModel(
            name='Medicacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_medicamento', models.CharField(max_length=100)),
                ('posologia', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Medicacoes',
            },
        ),
        migrations.CreateModel(
            name='Vacina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name_plural': 'Vacinas',
            },
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='pessoa',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='core.pessoa'),
        ),
        migrations.AlterField(
            model_name='veterinario',
            name='crmv',
            field=models.CharField(max_length=45, unique=True),
        ),
        migrations.CreateModel(
            name='Vacinacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('cachorro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cachorro')),
                ('vacina', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.vacina')),
            ],
            options={
                'verbose_name_plural': 'Vacinacoes',
            },
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('cachorro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cachorro')),
                ('medicacao', models.ManyToManyField(blank=True, null=True, to='core.Medicacao')),
                ('veterinario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.veterinario')),
            ],
            options={
                'verbose_name_plural': 'Consultas',
            },
        ),
        migrations.CreateModel(
            name='Adocao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('cachorro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.pessoa')),
                ('guardiao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.cachorro')),
            ],
            options={
                'verbose_name_plural': 'Adocoes',
            },
        ),
    ]
