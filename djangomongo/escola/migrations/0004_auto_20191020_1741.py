# Generated by Django 2.2.6 on 2019-10-20 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_auto_20191020_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='professor',
            name='cpf',
            field=models.BigIntegerField(),
        ),
    ]
