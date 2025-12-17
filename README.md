# Collectibles & Currency
Collectible's &amp; Currency for your ballsdex clone! If you are unaware of how to install 3rd party packages, please refer to this wiki page: 

[https://github.com/Ballsdex-Team/BallsDex-DiscordBot/pull/686] 

## What this contains

  - A currency system with /daily and /sell commands. Feel free to expand on the use of currency
  (Currency should be added to the Player model as an integer field. Below is an example you can use!)

```py
currency = models.PositiveIntegerField(default=1)
```
  
  - Collectible items to be purchased with said currency
  - A /store & /completion command for the collectibles

P.S. the collectibles dont rlly do anything else besides collecting them but again you can do whatever you want
