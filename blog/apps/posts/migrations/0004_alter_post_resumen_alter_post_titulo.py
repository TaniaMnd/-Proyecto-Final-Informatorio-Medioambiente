# Generated by Django 5.1.1 on 2024-10-10 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_comentarios_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='resumen',
            field=models.TextField(max_length=500, verbose_name='resumen'),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Titulo'),
        ),
    ]