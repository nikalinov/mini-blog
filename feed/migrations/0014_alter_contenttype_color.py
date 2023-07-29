# Generated by Django 4.2.2 on 2023-07-28 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0013_userprofile_image_alter_contenttype_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenttype',
            name='color',
            field=models.CharField(choices=[('primary', 'primary'), ('info', 'info'), ('success', 'success'), ('light', 'light'), ('warning', 'warning'), ('danger', 'danger')], default=('primary', 'primary'), max_length=20),
        ),
    ]
