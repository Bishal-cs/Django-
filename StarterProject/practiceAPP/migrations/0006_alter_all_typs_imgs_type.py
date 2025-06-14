# Generated by Django 5.2.2 on 2025-06-09 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practiceAPP', '0005_image_review_imageprofile_specific_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_typs_imgs',
            name='type',
            field=models.CharField(choices=[('gaming', 'Gaming'), ('nature', 'Nature & Landscapes'), ('urban', 'Urban'), ('abstract', 'Abstract'), ('portrait', 'Portrait'), ('technology', 'Technology'), ('fashion', 'Fashion'), ('architecture', 'Architecture'), ('wildlife', 'Wildlife'), ('sports', 'Sports'), ('travel', 'Travel'), ('food', 'Food & Cuisine'), ('macro', 'Macro'), ('aerial', 'Aerial'), ('cinematic', 'Cinematic'), ('fantasy', 'Fantasy'), ('vintage', 'Vintage')], max_length=20),
        ),
    ]
