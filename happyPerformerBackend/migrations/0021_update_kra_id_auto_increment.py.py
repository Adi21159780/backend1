from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('happyPerformerBackend', '0020_alter_kra_kra_id'),  # Ensure this references your latest migration
    ]

    operations = [
        migrations.RunSQL("""
            ALTER TABLE happyPerformerBackend_kra 
            ALTER COLUMN kra_id TYPE INTEGER USING kra_id::INTEGER;

            ALTER TABLE happyPerformerBackend_kra 
            ALTER COLUMN kra_id SET DEFAULT nextval('happyPerformerBackend_kra_kra_id_seq');

            CREATE SEQUENCE IF NOT EXISTS happyPerformerBackend_kra_kra_id_seq 
            OWNED BY happyPerformerBackend_kra.kra_id;
        """)
    ]
