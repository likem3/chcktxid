# Generated by Django 4.2.2 on 2023-06-24 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.IntegerField()),
                ('blockchain', models.CharField(max_length=50)),
                ('network', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255, unique=True)),
                ('label', models.CharField(max_length=255, unique=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('nonactive', 'Non-Active')], default='nonactive', max_length=20)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallets', to='users.account')),
            ],
            options={
                'db_table': 'users_wallets',
            },
        ),
    ]
