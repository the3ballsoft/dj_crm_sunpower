# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=b'250')),
                ('emails', models.EmailField(max_length=75)),
                ('direccion', models.CharField(max_length=b'250')),
                ('telefono', models.CharField(max_length=b'50')),
                ('asesor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Descuento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('porcentaje', models.DecimalField(max_digits=19, decimal_places=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Medio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=b'250')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mensaje', models.CharField(max_length=b'500')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=b'250')),
                ('descripcion', models.CharField(max_length=b'500')),
                ('stock', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicio', models.DateField(auto_now_add=True)),
                ('fecha_fin', models.DateField()),
                ('cliente', models.ForeignKey(to='crm.Cliente')),
                ('producto', models.ForeignKey(to='crm.Producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=b'250')),
                ('descripcion', models.CharField(max_length=b'500')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Solucion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=b'250')),
                ('descripcion', models.CharField(max_length=b'500')),
                ('productos', models.ManyToManyField(to='crm.Producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=b'250')),
                ('descripcion', models.CharField(max_length=b'250')),
                ('estado', models.CharField(max_length=b'30', choices=[(b'REALIZADA', b'REALIZADA'), (b'PENDIENTE', b'PENDIENTE'), (b'APLAZADA', b'APLAZADA'), (b'CANCELADA', b'CANCELADA')])),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_fin', models.DateField()),
                ('prioridad', models.CharField(max_length=b'10', choices=[(b'URGENTE', b'URGENTE'), (b'NORMAL', b'NORMAL'), (b'OPCIONAL', b'OPCIONAL')])),
                ('seguimiento', models.ForeignKey(related_name='TareaSeg', to='crm.Seguimiento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=b'250')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoTarea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=b'250')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='seguimiento',
            name='servicio',
            field=models.ForeignKey(to='crm.Servicio'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='seguimiento',
            name='solucion',
            field=models.ForeignKey(to='crm.Solucion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='seguimiento',
            name='tareas',
            field=models.ManyToManyField(related_name='TareaSeg', to='crm.Tarea'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo_producto',
            field=models.ForeignKey(to='crm.TipoProducto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='descuento',
            name='producto',
            field=models.ForeignKey(to='crm.Producto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='descuento',
            name='servicio',
            field=models.ForeignKey(to='crm.Servicio'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='descuento',
            name='solucion',
            field=models.ForeignKey(to='crm.Solucion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='medio',
            field=models.ForeignKey(to='crm.Medio'),
            preserve_default=True,
        ),
    ]
