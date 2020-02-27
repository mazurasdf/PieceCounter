from django.db import migrations

def create_data(apps, schema_editor):

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_data),
    ]