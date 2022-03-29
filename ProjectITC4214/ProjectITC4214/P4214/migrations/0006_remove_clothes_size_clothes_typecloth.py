# Generated by Django 4.0.3 on 2022-03-29 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('P4214', '0005_remove_clothes_cid_alter_clothes_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothes',
            name='size',
        ),
        migrations.AddField(
            model_name='clothes',
            name='typeCloth',
            field=models.CharField(choices=[('H', 'Hats'), ('D', 'Dresses'), ('S', 'Shoes'), ('B', 'Bags')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]