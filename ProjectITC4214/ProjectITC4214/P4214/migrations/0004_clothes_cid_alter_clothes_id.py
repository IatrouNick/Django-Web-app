# Generated by Django 4.0.3 on 2022-03-26 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('P4214', '0003_alter_clothes_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='cid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clothes',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
