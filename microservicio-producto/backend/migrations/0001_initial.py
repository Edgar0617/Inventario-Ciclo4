# Generated by Django 3.2.9 on 2021-12-03 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=100, unique=True, verbose_name='Categoria')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_productos', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.IntegerField(default=0)),
                ('producto', models.CharField(max_length=100, verbose_name='producto')),
                ('stock', models.IntegerField(default=0)),
                ('precio_compra', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_venta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.categoria')),
            ],
        ),
    ]
