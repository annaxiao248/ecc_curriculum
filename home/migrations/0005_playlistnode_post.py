# Generated by Django 4.1.2 on 2022-12-16 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_playlistnode'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlistnode',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.post'),
        ),
    ]