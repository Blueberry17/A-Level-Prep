# A dictionary corresponding each object to its use
# The effect of use is under the index of the situation it is used in
# The effect always contains: the description, the next index, the items gained, the gold gained,
# the change in state of the situation
# The effect possibly also contains: the index of another state changed, the change to that index

inventory_uses = {
    "lantern": {9: ["You pull out your lantern to reveal that this room has no floor, only a massive hole with no visible bottom. You leave this room at once.", 1, {}, 0, 0],
                34: ["You pull out your lantern to reveal a large, ornate chest sitting in the centre of small room. You heave the lid of the chest up to reveal a solitary emerald lying inside. You pick it up and place it in your rucksack before you leave the room.", 32, {"emerald"}, 0, 1]},
    "garlic": {18: ["You quickly pull out the garlic from your rucksack and extend your arm towards the vampire. It hisses in agony before transforming into a bat and flying away, into the darkness. For now, you are safe from the vampire.\n\nAs you look around this chamber, you catch sight of a fist-sized ruby, in the place where the vampire was standing. You pocket your incredible find. Seeing nothing else of use in this room, you leave by the exit you came in.", 15, {"ruby"}, 0, 1, 18, 1]},
    "healing potion": {44: ["Quickly, you retrieve the healing potion from your rucksack and help the warrior to drink it. After a few moments, he is clearly drastically healthier but still weak. He speaks to you in a stronger voice, 'thank you so much, generous adventurer. How can I possible repay you?'\n\nYou begin to explain your quest to him and he is soon nodding knowlingly. He tells you that he too had this quest but is in no fit state to continue. As a reward for your help, the man gives you a marvellous dimaond, which according to him is vital if you want to face the dragon.\n\nHe then wishes you good luck in your battle and tells you that he will find his own way back, a little later. You thank him for the diamond and leave the room.", 43, {"diamond"}, 0, 1, 0, 0]},
    "ruby": {46: ["You carefully retrieve the ruby from your rucksack and place it into the first slot. To your relief, it fits perfectly.", 49, {}, 0, 0]},
    "emerald": {49: ["You carefully retrieve the emerald from your rucksack and place it into the second slot. To your relief, it also fits perfectly.", 50, {}, 0, 0]},
    "diamond": {50: ["You carefully retrieve the diamond from your rucksack and place it into the last slot. To your relief, it too fits perfectly.", 51, {}, 0, 0]},
    "magical sword": {52: ["You brandish your mighty weapon, holding it aloft before the dragon. You believe you see a flicker of fear in the dragon's face before it roars with unrestrained rage. As it rears its head back, preparing to unleash a jet of flame at you, you sprint towards its belly screaming a battle cry. You pierce its hyde with ease, and the dragon roars in agony before thudding to the floor, causing the whole chamber to rumble as a result. You have killed the dragon and relieved Fallkirk of its misery!", -2, {}, 0, 0]}
}
