from django.db import models
from bd_models.models import Player

class Collectible(models.Model):
    REQUIREMENT_TYPES = [
        ("total", "Total Balls Owned"),
        ("shiny", "Shiny Balls Owned"),
        ("ball", "Specific Ball (1 required)"),
        ("balls", "Specific Ball (X required)"),
        ("special", "Special Card Ball"),
    ]

    requirement_type = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=REQUIREMENT_TYPES,
        help_text="Type of requirement necessary to obtain the collectible."
    )

    requirement_value = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Requirement value (depends on requirement type)."
    )

    name = models.CharField(max_length=50, unique=True, help_text="The name of the collectible")
    emoji = models.BigIntegerField(help_text="The emoji ID for this collectible")
    cost = models.IntegerField(help_text="The cost of the collectible in currency (MAKE SURE TO ADD THE CURRENCY FIELD IN THE Player MODEL)")
    bio = models.TextField(blank=True, null=True, help_text="The description of the Charm to be shown in the shop.")
    image_url = models.CharField(max_length=300, blank=True, null=True, help_text="The image URL of the collectible, will be shown in the shop")

    def __str__(self):
        return f"{self.emoji} {self.name}"
    
    class Meta:
        db_table = "collectible"
        verbose_name = "Collectible"
        verbose_name_plural = "Collectibles"
        indexes = [
            models.Index(fields=["requirement_type", "requirement_value"]),
        ]

class PlayerCollectible(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="collectibles")
    collectible = models.ForeignKey("Collectible", on_delete=models.CASCADE, related_name="owners")
    obtained_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "playercollectible"
        unique_together = ("player", "collectible")
        indexes = [
            models.Index(fields=["player"]),
            models.Index(fields=["collectible"]),
        ]

    def __str__(self):

        return f"{self.player} owns {self.collectible}"
