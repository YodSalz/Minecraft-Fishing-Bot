# Minecraft-Fishing-Bot
Python Bot that fishes in Minecraft based on Pixel Colors (EXE included in the EXE Folder)

ATTENTION
----------------------------
Particles would conflict with pixel recognition so turn them to minimal
----------------------------

How To Use:
1. First start the bot (command Prompt if py file -- EXE File if exe file)
2. go into Minecraft (! do not left click !)
3. throw out your fishing rod and don´t move ur mouse afterwards
4. open the inventory
5. click on the start of the black line (next to the stick -- rod needs to be in right hand)
6. close inventory
7. bot starts searching in 2 seconds (inventory will then need to be closed)
8. Bot will fish
9. DO NOT MOVE THE MOUSE ANYMORE (u cannot do anything else with your computer that needs to be active 
-- but ntflx works thoug if u have 2 screens ;D)

It sometimes won´t work, just restart, the Bot is Beta, fixes come soon

ATTENTION
---------------------
The Bot here was created on a server system where u have to move every 7 fishes
so it will move every 7 fishes!!!! if u dont want this just remove the dowalk() function and the fishings system
------------------------------

The Concept behind:
The start of the black line is constant!!
so i decided to follow the black line from a point (sometimes here to bot fails if the end moves) --> trying to fix that
i took a screenshot after the 2 seconds where the User has time to close the inventory, so a fish biting the lure while searching wouldn´t cause
a failure
then whent he last black pixel is found i knew the area where the lure will always land in
so i´m taking screenshots as fast as i can, go a 1 pixel (width) line down (about 20 pixels down) and see how many reds are in there (red is when
the r value is at least 2g and 2b [rgb])
if this treshold drops to 0 a fish has bitten and the bot will fish

libraries are all imported at the top so if u plan on using the .py version u will need to check if u installed these
