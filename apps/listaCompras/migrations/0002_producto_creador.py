# Generated by Django 3.0 on 2019-12-13 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
        ('listaCompras', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='creador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.perfilUsuario'),
        ),
    ]
