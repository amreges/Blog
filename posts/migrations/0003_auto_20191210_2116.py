# Generated by Django 3.0 on 2019-12-11 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20191210_1927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='Pagamento',
            new_name='pagamento',
        ),
    ]