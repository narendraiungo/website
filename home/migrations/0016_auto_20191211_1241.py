# Generated by Django 2.2.7 on 2019-12-11 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20191209_0825'),
    ]

    operations = [
        migrations.AddField(
            model_name='new_portfolio',
            name='child_sub_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.child_sub_category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deisgnuploads',
            name='design_images',
            field=models.FileField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='design',
            name='design_images',
            field=models.FileField(blank=True, null=True, upload_to='media/', verbose_name='Design Images'),
        ),
        migrations.AlterField(
            model_name='design',
            name='design_number',
            field=models.CharField(max_length=50, verbose_name='Design Number'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_number',
            field=models.CharField(max_length=50, verbose_name='project Number'),
        ),
    ]
