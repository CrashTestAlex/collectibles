from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("bd_models", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Collectible",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "requirement_type",
                    models.CharField(
                        max_length=50,
                        blank=True,
                        null=True,
                        choices=[
                            ("total", "Total Balls Owned"),
                            ("shiny", "Shiny Balls Owned"),
                            ("ball", "Specific Ball (1 required)"),
                            ("balls", "Specific Ball (X required)"),
                            ("special", "Special Card Ball"),
                        ],
                        help_text="Type of requirement necessary to obtain the collectible.",
                    ),
                ),
                (
                    "requirement_value",
                    models.CharField(
                        max_length=100,
                        blank=True,
                        null=True,
                        help_text="Requirement value (depends on requirement type).",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=50,
                        unique=True,
                        help_text="The name of the collectible",
                    ),
                ),
                (
                    "emoji",
                    models.BigIntegerField(
                        help_text="The emoji ID for this collectible"
                    ),
                ),
                (
                    "cost",
                    models.IntegerField(
                        help_text=(
                            "The cost of the collectible in currency "
                            "(MAKE SURE TO ADD THE CURRENCY FIELD IN THE Player MODEL)"
                        )
                    ),
                ),
                (
                    "bio",
                    models.TextField(
                        blank=True,
                        null=True,
                        help_text="The description of the Charm to be shown in the shop.",
                    ),
                ),
                (
                    "image_url",
                    models.CharField(
                        max_length=300,
                        blank=True,
                        null=True,
                        help_text="The image URL of the collectible, will be shown in the shop",
                    ),
                ),
            ],
            options={
                "db_table": "collectible",
                "verbose_name": "Collectible",
                "verbose_name_plural": "Collectibles",
            },
        ),
        migrations.CreateModel(
            name="PlayerCollectible",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "obtained_at",
                    models.DateTimeField(auto_now_add=True),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="collectibles",
                        to="bd_models.player",
                    ),
                ),
                (
                    "collectible",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="owners",
                        to="collect.collectible",
                    ),
                ),
            ],
            options={
                "db_table": "playercollectible",
                "unique_together": {("player", "collectible")},
            },
        ),
        migrations.AddIndex(
            model_name="playercollectible",
            index=models.Index(fields=["player"], name="player_idx"),
        ),
        migrations.AddIndex(
            model_name="playercollectible",
            index=models.Index(fields=["collectible"], name="collectible_idx"),
        ),
    ]