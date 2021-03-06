# Generated by Django 4.0.6 on 2022-07-18 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Germ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_name', models.CharField(max_length=100)),
                ('germ_name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('mode_of_trans', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tx', models.CharField(choices=[('M', 'Medication'), ('D', 'Diet'), ('S', 'Supplements'), ('L', 'Lifestyle Changes')], default='M', max_length=200)),
                ('vax_prevent', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('germ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.germ')),
            ],
        ),
    ]
