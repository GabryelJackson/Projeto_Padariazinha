# Generated by Django 4.2.7 on 2023-11-27 01:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Produto",
            fields=[
                ("id_produto", models.AutoField(primary_key=True, serialize=False)),
                ("produto", models.TextField(max_length=255)),
                ("preco", models.IntegerField()),
            ],
        ),
    ]
