# Generated by Django 4.0.3 on 2022-03-26 17:22

from django.apps.registry import Apps
from django.db import migrations, models
from django.db.backends.base.schema import BaseDatabaseSchemaEditor


def migrate_add_name(apps: Apps, schema_editor: BaseDatabaseSchemaEditor):
    db_alias = schema_editor.connection.alias

    Invitation = apps.get_model("authentik_stages_invitation", "invitation")

    for invite in Invitation.objects.using(db_alias).all():
        invite.name = invite.pk.hex
        invite.save()


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_stages_invitation", "0005_auto_20210901_1211"),
    ]

    operations = [
        migrations.AddField(
            model_name="invitation",
            name="name",
            field=models.SlugField(default=""),
            preserve_default=False,
        ),
        migrations.RunPython(migrate_add_name),
        migrations.AlterField(
            model_name="invitation",
            name="name",
            field=models.SlugField(),
            preserve_default=False,
        ),
    ]