# Generated by Django 2.2.7 on 2019-11-22 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_machine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='woboteammember',
            name='teams',
            field=models.ManyToManyField(related_name='teams', to='mailing_machine.WoBoTeam', verbose_name='Teams'),
        ),
    ]
