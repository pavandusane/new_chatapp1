# Generated by Django 2.1.5 on 2019-02-02 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('confirm_password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RestRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('confirm_password', models.CharField(default='none', max_length=20)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=8)),
                ('open', models.CharField(max_length=20)),
                ('close', models.CharField(max_length=20)),
                ('volume', models.CharField(max_length=100)),
            ],
        ),
    ]
