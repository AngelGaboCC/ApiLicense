# Generated by Django 4.2.3 on 2023-07-10 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiLicense', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='license',
            name='software_name',
            field=models.CharField(default='software_name', max_length=50),
        ),
        migrations.AlterField(
            model_name='license',
            name='company_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='license',
            name='job_title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='license',
            name='software_user_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='license',
            name='user_email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='license',
            name='user_full_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='license',
            unique_together={('software_name', 'software_user_name', 'version')},
        ),
    ]