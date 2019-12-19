# Generated by Django 3.0 on 2019-12-19 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_auto_20191219_0501'),
        ('listaCompras', '0010_remove_listadecompras_cantidad_productos'),
    ]

    operations = [
        migrations.AddField(
            model_name='listadecompras',
            name='cantidad_comprados',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listadecompras',
            name='cantidad_productos',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listadecompras',
            name='presupuesto_total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listadecompras',
            name='total_final',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='notas',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tienda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda.Tienda'),
        ),
    ]
