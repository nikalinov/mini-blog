# Generated by Django 4.2.2 on 2023-07-25 11:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0008_alter_contenttype_color_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='followers',
            field=models.ManyToManyField(editable=False, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
