# Generated by Django 4.0.5 on 2022-06-07 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('codigo', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('duracion', models.PositiveBigIntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('creditos', models.PositiveSmallIntegerField()),
                ('docente', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('ine', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('apPaterno', models.CharField(max_length=20)),
                ('apMaterno', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=20)),
                ('sexo', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='F', max_length=1)),
                ('vigencia', models.BooleanField(default=True)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fechaMatricula', models.DateField(auto_now_add=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.curso')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.estudiante')),
            ],
        ),
    ]
