# Generated by Django 4.1.6 on 2023-02-16 10:39

from django.db import migrations

import gnosis.eth.django.models


class Migration(migrations.Migration):
    dependencies = [
        ("history", "0071_alter_ethereumblock_confirmed_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="erc20transfer",
            name="unique_hash",
            field=gnosis.eth.django.models.Keccak256Field(null=True, unique=True),
        ),
        migrations.AddField(
            model_name="erc721transfer",
            name="unique_hash",
            field=gnosis.eth.django.models.Keccak256Field(null=True, unique=True),
        ),
        migrations.AddField(
            model_name="internaltx",
            name="unique_hash",
            field=gnosis.eth.django.models.Keccak256Field(null=True),
        ),
    ]