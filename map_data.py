# Index 0 is the description of the situation
# Index 1 is the description of the possible options
# Index 2 is the indexes that the choices correspond to (the next situations) - if the index is a string, it means gold
# must be used for this choice (which is the following number after 'g')
# Index 3 is any items in that room to be added to the user's inventory
# Index 4 is the number of gold pieces to be added to the user's inventory
# Index 5 is the state that the situation is left in corresponding to the user's choice
# Index 6 denotes whether the user encounters the same options or those of another situation (False in many cases means
# that the situation is only reachable once
# Index 7 is the index of the alternate situation for a user who has already encountered the first options (can be N/A)

map_data = [
    [["Background\n\nYou are an adventurer looking for two glorious things: fame and fortune. You live in a humble cottage in the peaceful town of Fallkirk. One day, you wake up on a brisk spring morning just like any other. However this is not to be a normal morning at all...\n\nYou get out of bed and just as you are preparing a meal, you hear screams coming from the direction of the Town Hall! You run straight there. When you arrive you see destruction all around and the town mayor sobbing on the floor. Just as you are wondering what could have caused this, you look up to see a dragon flying across the sky at speed away from the town!\n\nIn between sobs, the mayor tells you what happened. The infamous ancient dragon that dwells in these lands came here, burnt down houses and ate townsfolk including his wife.\n\nYour town is devastated and you swear revenge upon the sinister dragon. You take it as your mission to venture to the foul dungeons of the dragon, and vanquish the beast before it strikes again.\n\nYou leave the mayor in a heap on the floor, and quickly gather a few essentials. The next morning you set off north for the dreaded dungeons.\n\nYour equipment: 2 gold pieces, an iron sword and a rucksack to hold any other possessions."],
     [], [1], {}, 2, [0], False],
    [["After a few days of walking, you have finally arrived at the dungeon entrance. You heave the thick metal door open and peer inside. You see nothing and can only smell decay inside. You gulp and take a step inside, fearing the worst.\n\nAs soon as you let go of the door, it slams shut behind you, leaving you in the flickering light of a torch, stuck in the back wall. Three doors surround you, they are all made of rotting wood and you will have to choose one.", "You are back in the first room. Three doors surround you."],
     ["The north door", "The east door", "The south door"], [2, 8, 9], {}, 0, [1, 1, 1], True],
    [["You open the door to a room full of treasure with piles upon piles of gold. However, you have not yet stepped foot inside the room, so you have a choice.", "This door is now firmly locked. You will have to choose a different door."],
     ["Leave the room and shut the door", "Step into this room, towards the door"], [1, 3], {}, 0, [1, 1], False],
    [["You step forth into the room and look at all the gold in front of you. But just as you are admiring it, something erupts out of the gold pieces! It is a fearsome goblin, preparing to attack you."],
     ["Attack the goblin", "Flee from this room"], [4, 1], {}, 0, [1, 1], False],
    [["Skillfully swinging your sword, the goblin is no match for you and it soon lies dead at your feet. You walk closer to the piles of gold pieces and spot a sign in front of you. It reads: 'Take no more than ten gold pieces'."],
     ["Take no gold pieces", "Take ten gold pieces", "Take as many gold pieces as you can"], [5, 6, 7], {}, 0, [1, 1, 1], False],
    [["You feel safer taking no gold pieces at all so you leave the room by the way you came in."],
     [], [1], {}, 0, [0], False],
    [["You take ten gold pieces as the sign advises and leave the room by the way you came in."],
     [], [1], {}, 10, [0], False],
    [["You ignore the sign and take as many gold pieces as you can fit in your bag. You walk around the pile and to the back of the room, looking for a door. However, there seems to be no exit apart from the door you came in by. You walk back over to the entrance to the room but there is no door in sight! You are trapped, and you will die a slow and painful death of thirst or starvation..."],
     [], [-1], {}, 0, [0], False],
    [["You enter an almost identical room, with three new doors surrounding you. This room is similarly illuminated by a torch set in the wall. You will have to choose one of the doors.", "You are in a room with rotting wooden in doors in every direction, illuminated by a torch set in the wall."],
     ["The north door", "The east door", "The south door", "The west door"], [11, 21, 22, 1], {}, 0, [1, 1, 1, 1], True],
    [["You open the door and see absolutely nothing and can smell only rotting flesh."],
     ["Take a step into this room", "Leave the room and try another door"], [10, 1], {}, 0, [0, 0], True],
    [["You put one foot forward but realise that there is no floor! You cannot regain your balance and you plummet down and down. A few seconds later, you join one of the many other unfortunate souls to lay victim to this brutal death trap..."],
     [], [-1], {}, 0, [0], False],
    [["You open the door and are immediately greeted by an angry ogre. And to your surprise, it hits you round the head with a club. You have been knocked out.\n\nAfter a while, you wake up in a large cavern. It is cold and dark inside. You see the ogre who knocked you out, eating in a corner away from you. It is eating another unfortunate adventurer who ended up in its cavern. You realise you will be its next meal if you don't escape."],
     ["Try to attack the almighty ogre", "Pretend that you are still knocked out and trick the ogre", "Try to escape by the door you came in by"], [12, 13, 14], {}, 0, [0, 0, 0], False, 15],
    [["You jump up and grab your sword which was laying beside you. You run fearlessly towards the ogre who sees you just in time to defend itself. It is a hard fought battle but ultimately the strength of the ogre overpowers you. At least you will make for a tasty meal..."],
     [], [-1], {}, 0, [0], False],
    [["You lie quietly for several hours, waiting until the ogre comes for you. When the ogre finally approaches you, you grip your sword tightly, ready to trick him. Just as it picks you up with its giant hands, you slash forcefully at its body with your sword. The ogre soon slumps to the ground, with you narrowly avoiding being crushed.\n\nYou breathe a sigh of relief and consider the three new exits, in the walls of the cavern."],
     ["The northern passageway", "The eastern passageway", "The south door", "The western passageway"], [16, 17, 8, 18], {}, 0, [0, 0, 0, 0], False],
    [["You make your way quietly towards the door. You are almost at the door, starting to ease up, when you trip on a stone which clatters noisily across the floor. The ogre is soon upon you and overpowers you with its immense strength. At least you will make for a tasty meal..."],
     [], [-1], {}, 0, [0], False],
    [["You are in the cavern where you slew the ogre. It lies motionless in the centre of its former den."],
     ["The northern passageway", "The eastern passageway", "The south door", "The western passageway"], [16, 17, 8, 18], {}, 0, [0, 0, 0, 0], True],
    [["You walk into a dim room with a large wooden chest lying on the centre of the floor. You walk over to it and lift up the heavy lid. Sitting on the base of the chest is a small golden key and a few gold pieces, which you pick up and put in your rucksack. Intrigued by your find, you leave the room by the way you came in.", "This is the room where you found the golden key. The chest now lies empty on. floor. Seeing nothing else of use in this room, you leave by the way you came in."],
     [], [15], {"golden key"}, 3, [1], True],
    [["You look around this desolate room but all to be seen is the scurrying of rats. You promptly exit by the way you came in."],
     [], [15], {}, 0, [0], True],
    [["You walk into a room with a small fire burning in a corner. However, what you are more concerned about is the menacing vampire advancing towards you. His eyes begin to hypnotise you and you must quickly decide on a plan of action. Do you have any items that could help?", "You are back in the room where you warded off the vampire and thankfully it is still not here. You sit and watch the fire for a bit before you leave."],
     ["Attack the vampire", "Flee from the vampire"], [19, 20], {}, 0, [0, 0], True, 15],
    [["You try to wound it with your sword but it is no use. The vampire is impervious to any blades not fashioned from silver. You soon drop your sword as the vampire fully hypnotises you, allowing it to bite your next without difficulty. By tomorrow, you too will be a vampire wandering the dungeons of the dragon..."],
     [], [-1], {}, 0, [0], False],
    [["You just about have the strength of willpower to turn your head and escape the vampire, sprinting down the passage that you came in by."],
     [], [15], {}, 0, [0], True],
    [["You enter a room with three rotting wooden doors, one in each wall except the north. This room is dimly lit by a torch set in the north wall, luckily you pick up a gold piece that lies forgotten beneath it.", "You are in a room with three rotting wooden doors, one in each wall except the north. The room is dimly lit by a torch set in the wall."],
     ["The east door", "The south door", "The west door"], [32, 33, 8], {}, 0, [1, 1, 1, 1], True],
    [["You enter a room that is full of smoke, with a hardened dwarf sat on a chair behind an intricately carved table. There is a small candle on the table that provides enough light for you to make out the interested look on the dwarf's face.\n\nHolding his pipe in one hand, he demands that you approach no further and tell him of your business in these dungeons. What will you do?", "This door is now firmly locked. You will have to choose a different door."],
     ["Refuse to speak and leave the room", "Attack the dwarf", "Tell the dwarf of your quest"], [8, 23, 24], {}, 0, [1, 1, 0], False],
    [["You hastily draw your sword from its scabbard, and dash towards the dwarf. Unfortunately, unnoticed by you, a tripwire runs across the floor in the middle of the room. As you approach the dwarf, you trigger the trap and a poison arrow is fired at you from beneath the table. Your death will be swift..."],
     [], [-1], {}, 0, [0], False],
    [["You tell the dwarf of your quest to slay the evil dragon that dwells deep within these dungeons and he lightly chuckles. 'Well I certainly admire your bravery, adventurer. However, I have seen many just like you, who pass through these dungeons aiming to kill the beast but none have returned.'\n\n'Nevertheless, I shall give you some advice that will aid your mission. The only way to get to the dragon is by collecting three gems, alas I only know the location of one. The ruby is in the clutches of a vampire that resides north from here. Of course, you will need garlic if you wish to reclaim the ruby. If you can solve my riddle, I'll give you some of mine for free.'\n\nHis riddle is thus: 'my weight is 100 pounds plus half my weight, how much do I weigh?'"],
     ["100 pounds", "150 pounds", "200 pounds"], [26, 26, 25], {}, 0, [0, 0, 0], False],
    [["The dwarf smiles and congratulates you for your correct answer. He gives you a large clove of garlic and bids you farewell.\n\nHowever, just as you are about to close the door of this room behind you, the dwarf tells you one more piece of information. 'If you do, by some miracle, kill the dragon, you will need the password to get out - it is 673. Good luck adventurer.' You leave the room."],
     [], [8], {"garlic", "code '673'"}, 0, [0], False],
    [["The dwarf looks disappointed and tells you that your answer is incorrect. What will you do now?"],
     ["Bride the dwarf for the garlic", "Leave the room", "Attack the dwarf"], [27, 8, 23], {}, 0, [0, 0, 0], False],
    [["How much will you bribe the dwarf?"],
     ["Nothing", "3 gold pieces", "5 gold pieces", "10 gold pieces"], [28, "29g3", "30g5", "31g10"], {}, 0, [0, 0, 0, 0], False],
    [["With nothing to give the dwarf, you leave the room."],
     [], [8], {}, 0, [0], False],
    [["The dwarf willingly pockets your gold and gives you a large clove of garlic before he bids you farewell."],
     [], [8], {"garlic"}, 0, [0], False],
    [["The dwarf willingly pockets the gold and gives you a large clove of garlic before he bids you farewell. He gives you a large clove of garlic and bids you farewell.\n\nHowever, just as you are about to close the door of this room behind you, the dwarf tells you one more piece of information. 'If you do, by some miracle, kill the dragon, you will need the password to get out - it is 673. Good luck adventurer.' You leave the room."],
     [], [8], {"garlic", "code '673'"}, 0, [0], False],
    [["The dwarf willingly pockets the gold and gives you a large clove of garlic before he bids you farewell. He gives you a large clove of garlic and bids you farewell.\n\nHowever, just as you are about to close the door of this room behind you, the dwarf tells you one more piece of information. 'If you do, by some miracle, kill the dragon, you will need the password to get out - it is 673. Good luck adventurer.' You leave the room."],
     [], [8], {"garlic", "code '673'"}, 0, [0], False],
    [["You walk into another dim room with three wooden doors and one archway in the east wall. A pale light is coming from this exit.", "You walk into a dim room with three wooden doors and one archway in the east wall. A pale light is coming from this exit."],
     ["The north door", "The eastern archway", "The south door", "The west door"], [34, 38, 33, 21], {}, 0, [1, 1, 1, 1], True],
    [["You walk into a small room, barely tall enough for you to stand in. In the middle of the room sits a small but bright lantern, which you put in your rucksack. There are two exits from this room, a door in the north wall and a passageway in the east wall.", "You walk into a small room, barely tall enough for you to stand in. This is the room where you found your lantern. There are two exits from this room, a door in the north wall and a passageway in the east wall."],
     ["The north door", "The eastern passageway"], [21, 36], {"lantern"}, 0, [1, 1], True],
    [["You open the door and look into a pitch dark room. You hear only a faint dripping coming from within.", "This is the room where you found an emerald inside a chest. Nothing has changed since, so you leave the room."],
     ["Leave the room and shut the door", "Walk into the room and explore in the darkness"], [32, 35], {}, 0, [0, 1], False],
    [["Bravely, or perhaps stupidly, you start to walk forwards into the darkness. Almost immediately, you walk straight into a large wooden chest. You heave the lid of the chest up and run your hand along its base. You come across a rock of some sort and pick it up.\n\nYou bring it over to the door for some dim light and realise that you have found an emerald, which you place in your rucksack before you leave the room."],
     [], [32], {"emerald"}, 0, [0], False],
    [["You walk into a large empty cavern. After examining more carefully for a little while, you find a small hole in the south wall, just large enough to fit your arm through. There is a door in the north wall and a passageway in the west wall."],
     ["Reach your arm through the hole", "Leave by the north door", "Leave by the western passageway"], [37, 32, 33], {}, 0, [0, 0, 0], True],
    [["You navigate your arm through the hole and feel around inside in. Suddenly, you scream in pain as you withdraw you arm as quick as you can. But it is no use, you will not survive the bite of the rattlesnake..."],
     [], [-1], {}, 0, [0], False],
    [["You walk into a huge chamber, with a decrepit chandelier hanging from the roof. There is an archway carved into the stone in the east and west wall.\n\nStanding behind a large wooden desk is a strange bearded old man holding a staff, who smiles at you cunningly. He is wrapped in filthy robes and offers to sell you a special magical sword for the high price of 8 gold pieces."],
     ["Attack this strange man", "Pay 8 gold pieces for his magic sword", "Leave by the eastern archway", "Leave by the western archway"], [39, "40g8", 43, 32], {}, 0, [0, 1, 0, 0], False, 42],
    [["You draw your sword against this stranger but he is too quick for you. He simply points his staff at you, causing a bolt of energy to shoot from it, fatally striking you in your chest. You should not have underestimated a wizard..."],
     [], [-1], {}, 0, [0], False],
    [["You hand over the 8 gold pieces to the stranger who looks almost surprised by your purchase. He brandishes a magnificent, polished iron sword and bestows it to you. You are amazed at how light it feels in your arms, while a sense of reinvigorating energy rushes through your body. You are impressed with your purchase.\n\nThe man, having observed your admiration, reveals himself to be a wizard and wishes you good luck with the rest of your quest. Furthermore, he offers you a healing potion for a 'discounted' 5 gold pieces."],
     ["Pay the 5 gold pieces for his healing potion", "Leave by the eastern archway", "Leave by the western archway"], ["41g5", 43, 32], {"magical sword"}, 0, [0, 0, 0], False],
    [["You pay the extra 5 gold pieces for the healing potion which the wizard pulls out from his robes and hands to you carefully. 'Use it well', he advises you as he says goodbye to you. You must now leave this chamber."],
     ["Leave by the eastern archway", "Leave by the western archway"], [43, 32], {"healing potion"}, 0, [0, 0], False],
    [["Incredibly, this room that was formerly occupied by the wizard is now completely empty, you must choose a way to leave by."],
     ["Leave by the eastern archway", "Leave by the western archway"], [43, 32], {}, 0, [0, 0], True],
    [["You walk into another dim room with a wooden door in the north, a passageway in the east wall and an archway in the west wall. A pale light is coming from the western archway.", "You walk into a dim room with a wooden door in the north, a passageway in the east wall and an archway in the west wall. A pale light is coming from the western archway."],
     ["The north door", "The eastern passageway", "The western archway"], [44, 46, 38], {}, 0, [1, 1, 1, 1], True],
    [["You walk into a small chamber where a man lays strewn on the floor, up against the north wall. He is clearly dying and begs for your help in a raspy voice. Do you have any items that could help?", "This door is now firmly locked. You will have to choose a different door."],
     ["Leave the room", "Attempt to talk to the man to find out what is wrong with him"], [43, 45], {}, 0, [1, 1], False],
    [["You attempt to talk further with the man but he cannot usher any further words. Not more than a minute later, he lies dead at your feet. You leave this room in sorrow."],
     [], [43], {}, 0, [0], False],
    [["You start to walk down the passageway and a few seconds later, you hear a loud clang behind you. You turn around to see that a portcullis has slammed to the ground, previously hidden in the roof of the passage. You try to move it to no avail, you are trapped! You are forced to continue eastwards.\n\nYou keep walking for several minutes in the darkness until you begin to see some light further on. After walking for another couple minutes, you enter a small cavern, lit by two small torches in the north and south walls. In front of you is a large oaken door with 3 circular slots.\n\nWritten at the top of this door in runes are instructions to open the door, telling you to place a gemstone in each of the slots. The runes instruct you to place a ruby in the first slot. What will you do?"],
     ["Try to break the door down", "Hope the door opens"], [47, 48], {}, 0, [0, 0], False],
    [["You charge at the door with all your might time and time again, but it is no use. The door will not budge. You are doomed to spend the last days of your life in this depressing passageway..."],
     [], [-1], {}, 0, [0], False],
    [["You see no point in trying to break down such a massive door so you simply wait, hoping that someone will open it for you. Unfortunately, it is not until long after you have perished that another adventurer manages to open this door..."],
     [], [-1], {}, 0, [0], False],
    [["The runes instruct you to place an emerald in the middle slot. What will you do now?"],
     ["Try to break the door down", "Hope the door opens"], [47, 48], {}, 0, [0, 0], False],
    [["The last of the runes instruct you to place a diamond in the final slot. What will you do?"],
     ["Try to break the door down", "Hope the door opens"], [47, 48], {}, 0, [0, 0], False],
    [["The runes glow magically as you listen to many strange clicking noises coming from behind the door. Eventually they stop and all falls silent again. You wait a few seconds before you push on the door, heaving it open with the help of your shoulder. The much brighter light on the other side of the door momentarily blinds you as you wearily step past the door."],
     [], [52], {}, 0, [0], False],
    [["Once your eyes have become accustomed to the light, you are amazed at what you see. Piles upon piles of gold surround you, laced with magnificent gems of every colour. However, more to your attention is the huge, green scaled dragon that looms over you, maliciously staring straight into your eyes. Steam is already funneling out of the side of its mouth and its nostrils.\n\n'I have been expecting you, foolhardy adventurer. I must say that I am surprised you have got this far, but unfortunately for you, this is where your journey ends', the dragon announces as a deep chuckles resonates from its immense belly. You can't help but tremble and you must quickly decide what to do, lest you be turned to ash."],
     ["Fight the dragon with your iron sword", "Try to talk to the dragon"], [53, 54], {}, 0, [0, 0], False],
    [["You dash towards the dragon's belly, hoping to pierce its hyde with your sword. Alas, it simply glances off the side, leaving nothing but a mere scratch. The dragon lets out a booming laugh as it burns you to a crisp..."],
     [], [-1], {}, 0, [0], False],
    [["'You are in no position to bargain, feeble human. I will enjoy ending you', the dragon lets out a booming laugh as it burns you to a crisp..."],
     [], [-1], {}, 0, [0], False]
]
