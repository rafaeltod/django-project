# Generated by Django 4.2.7 on 2024-07-12 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_alter_produto_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='produto',
            name='Produto',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='produto',
            name='msgPromocao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]