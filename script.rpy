# The script of the game goes in this file.

#placeholder name for MC:
mc = "MC"

#declaration of characters
define ATF = Character("")
define MC = Character(mc)
#declaration of backgrounds
image bg campus1 = "placeholder.png"
image blackscreen = "placeholder.png"
#declaration of character art
image ATF default = "placeholder.png"
# The game starts here.

label start:
    scene bg blackscreen
    "Never thought I’d make it back here in time."
    "It’s really been a while since I was here again, huh…and now I’m back again."
    "Oh look, a random guy screaming at nothing. I’m starting to miss Japan."
    "Well, whatever I don’t have to worry about that for now. I know that mom and dad really wanted me to go to college in the states, but I don’t know if this is the right choice."
    "I mean, the friendships that I have here are more than likely gone; I even lost track of my best friend."
    "I don’t think that coming from Japan will improve my chances of getting a girlfriend. At least in Japan some girls were interested in foreign guys."
    "Ah, whatever. I’m thinking too much into this. It’s not like anything major will happen. ( ͡° ͜ʖ ͡°) Just go through college and move right back after."
    "God, the jet lag must still be lingering. I wanna take a nap.]"
    #need to make this emphasized or something
    "open eyes"
    MC"SHIT!!"
    MC"Missed my damn stop! SIR CAN YOU  STOP!!"
    "Bus Driver" "I am sorry I can’t do that [mc]. I am legally not allowed to do that. You’ll have to wait until the next stop."
    MC"But I can’t be late for orientation!"
    #need to clean this up, add emphasis
    "Bus Driver" "sigh"
    "Bus Driver" "You know how many times I hear that this time of the year?"
    "Bus Driver" "Just settle in, kid. Next stop is only a five minute walk from the last."
    "Bus Driver" "kids these days can’t walk…"
    MC"But there’s surely something you can do, right?"
    "Bus Driver" "No now just sit your ass down and wait."
    "[mc] sighs and just sits down and shakes his head and waits for the next bus stop. He just hoped to make it in time"
    return
