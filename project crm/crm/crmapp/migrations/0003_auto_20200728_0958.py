# Generated by Django 3.0.8 on 2020-07-28 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0002_auto_20200728_0913'),
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formerid', models.CharField(max_length=100, null=True)),
                ('firstname', models.CharField(max_length=100, null=True)),
                ('lastname', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='submit',
        ),
    ]
