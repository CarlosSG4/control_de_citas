# Generated by Django 2.1.7 on 2019-03-10 02:10

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
            name='perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellidos', models.CharField(max_length=200)),
                ('edad', models.CharField(max_length=200)),
                ('curp', models.CharField(max_length=200)),
                ('sexo', models.CharField(max_length=200)),
                ('celular', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('municipio', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=200)),
                ('consultorio', models.CharField(max_length=200)),
                ('medico', models.CharField(max_length=200)),
                ('turno', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
