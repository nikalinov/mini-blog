# Generated by Django 4.2.2 on 2023-07-29 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0014_alter_contenttype_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenttype',
            name='color',
            field=models.CharField(choices=[('primary', 'primary'), ('info', 'info'), ('success', 'success'), ('light', 'light'), ('warning', 'warning'), ('danger', 'danger')], default=('danger', 'danger'), max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='feed/assets/img/profile-default.jpg', upload_to='feed/profile-pics/', width_field='img_width'),
        ),
    ]
