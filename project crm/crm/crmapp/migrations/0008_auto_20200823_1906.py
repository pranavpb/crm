# Generated by Django 3.0.8 on 2020-08-23 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0007_auto_20200804_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='basic_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, null=True)),
                ('lastname', models.CharField(max_length=100, null=True)),
                ('emailaddress', models.CharField(max_length=100, null=True)),
                ('mobilenumber', models.CharField(max_length=100, null=True)),
                ('DOB', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='other_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fathername', models.CharField(max_length=100, null=True)),
                ('mothername', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('pincode', models.CharField(max_length=100, null=True)),
                ('aadharnumber', models.CharField(max_length=100, null=True)),
                ('drivinglicencenumber', models.CharField(max_length=100, null=True)),
                ('emergencycontactnumber', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='salary1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Designation', models.CharField(max_length=100, null=True)),
                ('salary', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='salary2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Accountnumber', models.CharField(max_length=100, null=True)),
                ('Bankname', models.CharField(max_length=100, null=True)),
                ('Bankaddress', models.CharField(max_length=100, null=True)),
                ('IFSCcode', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='lead',
        ),
    ]