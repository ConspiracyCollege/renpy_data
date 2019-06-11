# The script of the game goes in this file.

#placeholder name for MC:
mc = "MC"

#declaration of characters
define ATF = Character("Andy")
define MC = Character(mc)
#declaration of backgrounds
image bg campus1 = "placeholder.png"
image blackscreen = "placeholder.png"
#declaration of character art
image ATF default = "placeholder.png"
# The game starts here.

label 1.1_intro:
    scene bg blackscreen
    "{i}Never thought I’d make it back here in time.{\i}"
    "{i}It’s really been a while since I was here again, huh…and now I’m back again.{\i}"
    "{i}Oh look, a random guy screaming at nothing. I’m starting to miss Japan.{\i}"
    "{i}Well, whatever I don’t have to worry about that for now. I know that mom and dad really wanted me to go to college in the states, but I don’t know if this is the right choice.{\i}"
    "{i}I mean, the friendships that I have here are more than likely gone; I even lost track of my best friend.{\i}"
    "{i}I don’t think that coming from Japan will improve my chances of getting a girlfriend. At least in Japan some girls were interested in foreign guys.{\i}"
    "{i}Ah, whatever. I’m thinking too much into this. It’s not like anything major will happen. ( ͡° ͜ʖ ͡°) Just go through college and move right back after.{\i}"
    "{i}God, the jet lag must still be lingering. I wanna take a nap.{\i}"
    #need to make this emphasized or something
    "open eyes"
    MC "{b}SHIT!!{\b}"
    MC "Missed my damn stop! {b}SIR CAN YOU  STOP!?!{\b}"
    "Bus Driver" "I am sorry I can’t do that. I am legally not allowed to do that. You’ll have to wait until the next stop."
    MC "But I can’t be late for orientation!"
    #need to clean this up, add emphasis
    "Bus Driver" "{i}sigh{\i}"
    "Bus Driver" "You know how many times I hear that this time of the year?"
    "Bus Driver" "Just settle in, kid. Next stop is only a five minute walk from the last."
    "Bus Driver" "{size=-20}kids these days can’t walk…{/size}"
    MC"But there’s surely something you can do, right?"
    "Bus Driver" "No now just sit your ass down and wait."
    "[mc] sighs and just sits down and shakes his head and waits for the next bus stop. He just hoped to make it in time"

    jump 1.1_transition

label 1.1_transition:
    scene bg school
    MC "Well, shit, this school looks really nice, better than I was expecting."
    "{i}Huh. There is a girl there reading a shiny book...{\i}"
    
return
