# Generated by Django 3.0 on 2020-06-23 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='visitorquery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=150)),
                ('contactnumber', models.CharField(default='', max_length=20)),
                ('message', models.CharField(default='', max_length=500)),
                ('dateandtime', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
