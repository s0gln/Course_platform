# Generated by Django 4.2.16 on 2024-10-02 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('global_models', '0006_work_title_alter_dowork_file_alter_work_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='dowork',
            name='score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
