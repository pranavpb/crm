# Generated by Django 3.0.8 on 2020-08-25 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0012_auto_20200823_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='education_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=100, null=True)),
                ('qualification', models.CharField(max_length=100, null=True)),
                ('institute', models.CharField(max_length=100, null=True)),
                ('year', models.IntegerField(null=True)),
                ('percent', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='experience_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=100, null=True)),
                ('company', models.CharField(max_length=100, null=True)),
                ('from_date', models.CharField(max_length=100, null=True)),
                ('to_date', models.CharField(max_length=100, null=True)),
                ('position', models.CharField(max_length=100, null=True)),
                ('reason', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
