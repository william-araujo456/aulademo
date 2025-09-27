from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0002_album_music'),
    ]

    operations = [
        migrations.RunSQL("CREATE EXTENSION IF NOT EXISTS unaccent;"),
    ]
