# Generated by Django 3.0 on 2019-12-18 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listaCompras', '0009_auto_20191218_1413'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='perfilUsuario',
            new_name='RegistroUsuario',
        ),
    ]
