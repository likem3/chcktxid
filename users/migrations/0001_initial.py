# Generated by Django 4.2.2 on 2023-06-23 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(editable=False, unique=True)),
                ('user_id', models.IntegerField(unique=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('nonactive', 'Non-active'), ('suspended', 'Suspended')], default='nonactive', max_length=20)),
            ],
            options={
                'db_table': 'users_accounts',
            },
        ),
    ]