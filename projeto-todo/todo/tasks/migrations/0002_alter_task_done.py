# Generated by Django 3.2.19 on 2023-07-24 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done',
            field=models.CharField(choices=[('Doing', 'Doing'), ('Done', 'Done')], max_length=10),
        ),
    ]
