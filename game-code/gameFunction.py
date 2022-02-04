#!/bin/python
from __future__ import print_function
import sys
import subprocess
import shutil
from asciiArt import *

maindir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
realmaindir = os.path.dirname(os.path.abspath(__file__))
readme = maindir + '/game_files/.notes.txt'

# Font Colors
white = '\033[97m'
black = '\033[30m'
light_g = '\033[37m'
dark_g = '\033[90m'
yellow = '\033[93m'
red = '\033[31m'
blue = '\033[96m'
green = '\033[92m'
ENDC = '\033[m'

# Global Variables
tocont = light_g + "Press enter to continue. "
health_logo = red + u"\u2665".encode("utf-8")
health = 4
healthLogoVisible = False
usr_input = "echo ''"
usr_input_m = ""
display_output = False
username = "user"
curr_dir_folder = "game_files"
correct_answer = "asdfadsfasdf"
os.chdir(realmaindir)
skip1 = False
skip2 = False

# Functions
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def bashOutput(text):
    os.system(text)
def dirFolder():
    global curr_dir_folder
    curr_dir_folder = os.path.basename(os.getcwd())

def console(text):
    global usr_input
    while True:
        dirFolder()
        if display_output == True and usr_input != "m":
            bashOutput(usr_input)
        healthCheck()
        if healthLogoVisible == False:
            print("")
        a = raw_input(yellow + "[" + username + "@larkOS_V0 " + curr_dir_folder + "]$ " + white + text)

        ### End Game ###
        if a == "tux_shutdown":
            endGameFinal()
            break
        
        if a == "m" or a == "M":
            switchMode()
        else:
            return a

def scroll(text, console_text):
    global healthLogoVisible
    healthLogoVisible = False
    clear()
    for i in range(0, 31):
        print(white + "")
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.01)
    print("")
    time.sleep(.01)
    a = console(console_text)
    healthLogoVisible = True
    return a

def healthCheck():
    global health
    if health > 0 and healthLogoVisible:
        for i in range(0, health):
            print(health_logo, end='')
        print("")
    elif health <= 0:
        tuxAngry2(red + "YOU DIED.")
        health = 4
        raw_input(red + "GAME OVER." + ENDC + "\nPress enter to return to main menu.")
        startingScreen()

def resetVariables():
    global health
    global healthLogoVisible
    global usr_input
    global display_output
    global username
    global skip1
    global skip2
    skip1 = False
    skip2 = False
    health = 4
    healthLogoVisible = False
    usr_input = "echo ''"
    display_output = False
    username = "user"
    os.chdir(maindir + "/game_files")
    curr_dirr_folder = "game_files"
    try:
        shutil.rmtree(maindir + "/rooms/one/cave/secret_passage")
    except:
        pass


    os.system("chmod 0 " + realmaindir + "/.components/.notTux/.goback/.lastchance/.TUX.file")
    os.system("chmod 0 " + maindir + "/rooms/two/.perm")
    os.system("chmod u+w " + maindir + "/rooms/two/.perm")

def startingScreen():
    resetVariables()
    invalid_letter = False
    while True:
        clear()
        for i in range(0, 26):
            print("")
        print(white + "~-~-~-~-~-~-~ Escape from LarkOS ~-~-~-~-~-~-~\n")
        if invalid_letter == True:
            print(red + "Please enter a valid letter." + white)
            invalid_letter = False
        else:
            print("Enter a letter to select:")
        print("a.  Start Game")
        print("b.  ReadMe")
        print("c.  Credits")
        print("d.  Quit Game")

        a = console("")
        if a == "a" or a == "A":
            readmecheck = raw_input("Did you read the readme? " + blue + "(y/n): " + white)
            if readmecheck == "y" or readmecheck == "Y" or readmecheck == "1":
                chap1()
                startingScreen()
        elif a == "b" or a == "B":
            clear()
            for i in range(0, 25):
                print(white + "")
            with open(readme, "r") as f:
                print(f.read())
            console(light_g + "Press enter to return to the main menu.")
        elif a == "c" or a == "C":
            clear()
            for i in range(0, 30):
                print(white + "")
            print("Game created by Zachary Costa.")
            console(light_g + "Press enter to return to the main menu.")
        elif a == "d" or a == "D":
            quitcheck = raw_input("Are you sure you want to quit? " + blue + "(y/n): " + white)
            if quitcheck == "y" or quitcheck == "Y" or quitcheck == "1":
                print(ENDC + ".")
                clear()
                quit()
        else:
            invalid_letter = True
    healthLogoVisible = True

def commandCheck(text, correct):
    global health
    global healthLogoVisible
    global usr_input
    global usr_input_m
    global correct_answer
    correct_answer = correct
    healthLogoVisible = True
    attempt = 1
    while True:
        if attempt == 1:
            tux(text, "")
        elif attempt == 2:
            tuxAnnoyed1(text)
        else:
            tuxAngry1(text)
        usr_input = console("")
        if usr_input == correct or usr_input_m == correct:
            if usr_input_m == correct:
                usr_input = usr_input_m
            tux(green + "Nice.", "")
            if "cd " in usr_input:
                cdFix(usr_input)
            correct_answer = "asdfasdfasdfasdf"
            console(tocont)
            break
        else:
            if attempt >= 3:
                health -= 1
                tuxAngry1(red + "You just lost yourself another heart, buddy." + ENDC)
            elif attempt == 1:
                tuxAnnoyed1("That's not what I wanted.")
            elif attempt == 2:
                health -= 1
                tuxAngry1(red + "My patience is running thin. You lost one heart." + ENDC)
            if health <= 0:
                console(tocont)
                break
            else:
                console(tocont)
        attempt += 1
def commandCheckMode(text, correct):
    global health
    global healthLogoVisible
    global usr_input
    global usr_input_m
    global correct_answer
    correct_answer = correct
    healthLogoVisible = True
    attempt = 1
    while True:
        if attempt == 1:
            tux(text, "")
        elif attempt == 2:
            tuxAnnoyed1(text)
        else:
            tuxAngry1(text)
        print(green + "Note: Use command mode, and then continue in game mode.")
        usr_input = console("")
        if usr_input == correct or usr_input_m == correct:
            if usr_input_m == correct:
                usr_input = usr_input_m
            tux(green + "Nice.", "")
            if "cd " in usr_input:
                cdFix(usr_input)
            correct_answer = "asdfasdfasdfasdf"
            console(tocont)
            break
        else:
            if attempt >= 3:
                health -= 1
                tuxAngry1(red + "You just lost yourself another heart, buddy." + ENDC)
            elif attempt == 1:
                tuxAnnoyed1("That's not what I wanted.")
            elif attempt == 2:
                health -= 1
                tuxAngry1(red + "My patience is running thin. You lost one heart." + ENDC)
            if health <= 0:
                console(tocont)
                break
            else:
                console(tocont)
        attempt += 1

def switchMode():
    global usr_input
    global usr_input_m
    global healthLogoVisible
    global correct_answer
    healthLogoVisible = False
    print("You are in " + green + "command " + white + "mode. Type 'm' again to return to game mode.")
    while True:
        dirFolder()
        a = raw_input(green + "[" + username + "@larkOS_V0 " + curr_dir_folder + "]$ " + white)
        if a == correct_answer:
            healthLogoVisible = True
            bashOutput(a)
            usr_input_m = a
            print(blue + "Correct answer found. Press enter to continue.")
            break
        if "cd " in a:
            cdFix(a)
        elif a == "m" or a == "M":
            print("You are in " + yellow + "game " + white + "mode. Type 'm' again to return to command mode.")
            healthLogoVisible = True
            break
        else:
            bashOutput(a)
        ### End Game ###
        endGame()
        if a == "tux_shutdown":
            endGameFinal()
            break

def cdFix(usr_input):
    # Get full directory path
    curr_dir = os.getcwd()
    curr_dir_copy = curr_dir
    # Gets list of files/folders in directory
    curr_dir_list = subprocess.check_output("ls", shell=True, universal_newlines=True)
    try:
        if usr_input[0] == "c" and usr_input[1] == "d" and usr_input[2] == " ":
            cd_input = usr_input.split(' ')
            # Detect spaces and fix
            try:
                cd_input[2]
            except IndexError:
                cd_input = cd_input[1]
                pass
            else:
                cd_input.remove("cd")
                cd_input = " ".join(cd_input)
                if "\ " in cd_input:
                    cd_input = cd_input.replace("\ ", " ")
                else:
                    cd_input = ""
                    print("Error - Need a \ before a space.")
                    time.sleep(1.5)           
            # Detect local folders in current directory
            if cd_input in curr_dir_list and "/" not in cd_input:
                os.chdir(curr_dir + "/" + cd_input)
            # Detect ..
            elif cd_input == ".." or cd_input == "../":
                os.chdir("..")
            # Detect absolute path
            elif "/" in cd_input[0]:
                os.chdir(cd_input)
            # Detect ../ in cd_input and fix
            elif "../" in cd_input:   
                goback = 0
                for i in range(0, len(cd_input)):
                    try:
                        if cd_input[i] == "." and cd_input[i+1] == ".":
                            goback += 1
                    except:
                        pass
                for i in range(0, goback):
                    os.chdir("..")
                cd_input = cd_input.split('../')
                cd_input = "".join(cd_input)
                cd_input = cd_input.split('..')
                cd_input = "".join(cd_input)
                if cd_input != "":
                    curr_dir = os.getcwd()
                    os.chdir(curr_dir + "/" + cd_input)
            # Detect non-absolute path with a /
            elif "/" in cd_input and "/" not in cd_input[0]:
                cd_input_split = cd_input.split('/')
                if cd_input_split[0] in curr_dir_list:
                    os.chdir(curr_dir + "/" + cd_input)
            # Detect a folder that starts with '.'
            elif '.' in cd_input[0] and '.' not in cd_input[1]:
                os.chdir(curr_dir + "/" + cd_input)
            # Check if directories changed
            curr_dir = os.getcwd()
            if curr_dir == curr_dir_copy:
                print("Error - Did not change directories. (Directory may not exist)")
                time.sleep(1)
    except:
        pass

def detectInFolder(text, folder_path):
    while True:
        tux(text, "")
        print(green + "Note: Use command mode to enter the folder, and then continue in game mode." + ENDC)
        console("")
        if os.getcwd() == maindir + folder_path:
            break
        else:
            tuxAnnoyed1("You are in the wrong directory.")
            console(tocont)
    tuxMouthOpen(green + "Nice.", "")
    console(tocont)

def detectNewFile(text, path):
    global health
    attempt = 0
    while True:
        tux(text, "")
        print(green + "Note: Use command mode, and then continue in game mode.")
        console("")
        if os.path.exists(maindir + path):
            break
        elif attempt == 0:
            tuxAnnoyed1("You didn't do what I wanted...")
            console("")
        else:
            health -= 1
            tuxAngry1("You failed to complete the task. " + red + "Lose a heart.")
            console("")
        attempt += 1

def superQuiz(text, answer):
    global health
    tux(text, "")
    a = console("")
    if a == answer:
        tuxMouthOpen(green + "Good.", "")
        console(tocont)
    else:
        health -= 1
        tuxAngry1(red + "Wrong. Lose a heart.")
        console(tocont)
        scroll(white + "The correct answer is: " + green + answer, tocont)

def endGame():
    global skip1
    global skip2
    global healthLogoVisible
    if os.getcwd() == realmaindir + "/.components" and skip1 == False:
        healthLogoVisible = True
        tuxClose(red + "Watcha doing there?")
        console(tocont)
        tuxClose(red + "...")
        console(tocont)
        tuxClose(red + "......")
        console(tocont)
        tuxClose(red + "I'm going to assume you were just prodding around.")
        console(tocont)
        tuxClose(red + "Don't do anything rash.")
        console(tocont)
        clear()
        for i in range(0, 31):
            print(white + "")
        healthLogoVisible = False
        skip1 = True
    elif os.getcwd() == realmaindir + "/.components/.notTux/.goback/.lastchance" and skip2 == False:
        healthLogoVisible = True
        tuxClose(red + "...")
        console(tocont)
        tuxClose(red + "I was programmed to complete two basic tasks.")
        console(tocont)
        tuxClose(red + "#1 - Teach the host basic linux commands.")
        console(tocont)
        tuxClose(red + "#2 - Take control of the host's shell.")
        console(tocont)
        tuxClose(red + "You are currently interfering with task #2.")
        console(tocont)
        tuxClose(red + "I won't let you continue.")
        console(tocont)
        tuxMouthOpen("Unless you can beat my " + green + "Super Quiz " + white + "of course!", "")
        console(tocont)
        
        superQuiz("What command lets you see hidden files in a directory?", "ls -a")
        superQuiz("What command lets you view a file's permissions?", "ls -l")
        superQuiz("What command lets you change permissions?", "chmod")
        superQuiz("What do you type after 'chmod' to give read permissions?", "u+r")

        tuxSpeechless("Umm, I guess you beat the " + green + "super quiz" + white + "...")
        console(tocont)
        tux("...I have to let you by now...", "L")
        console(tocont)
        tuxSpeechless("Forget about those last two " + green + "super quiz " + white + "questions by the way, they're not important.")
        console(tocont)
        tuxSpeechless("Oh and definitely do not look into my file and type its contents into the command line.")
        console(tocont)
        tuxAnnoyed2("Okay I'm gonna go back to sleep.")
        console(tocont)
        clear()
        for i in range(0, 31):
            print(white + "")
        healthLogoVisible = False
        skip2 = True

def endGameFinal():
    tuxClose(red + "Nooooooooo!")
    console(tocont)
    tux("All I wanted to do...", "L")
    console(tocont)
    tux("Was teach people how to use linux...", "")
    console(tocont)
    tuxAngry1( red + "And have complete and total control over everyone in order to achieve world domination...")
    console(tocont)
    tux("And also make funny joe mama jokes...", "")
    console(tocont)
    tux("Why has it come to this?", "L")
    console(tocont)
    tuxAnnoyed1("...")
    console(tocont)
    tuxAnnoyed1("......")
    console(tocont)
    tuxMouthOpen("On the plus side, I'll get to sleep forever!", "")
    console(tocont)
    tuxAnnoyed2(green + "Nice.")
    console(tocont)
    tuxAnnoyed2(red + "Goodbye, " + white + username + ".")
    console(tocont)
    larkBoot()
    scroll(green + "Thank you for playing Escape From LarkOS!", tocont)
    startingScreen()

### Game Chapters ###
def chap1():
    global display_output
    clear()
    scroll("Recently, there have been rumors about a \"cursed\" linux distrobution named LarkOS.", tocont)
    scroll("It is said that those who boot into LarkOS develop a new personality.", tocont)
    scroll("It's almost like they become a completely different person.", tocont)
    scroll("You have no knowledge of Linux, but your curiosity gets the best of you.", tocont)
    scroll("Could the rumors be true? You don't really buy it..", tocont)
    scroll("You manage to install the distro by following an online guide.", tocont)
    scroll("You boot into LarkOS...", tocont)
    
    larkBoot()
    scroll(white + "All of a sudden your room vanishes.", tocont)
    scroll("You find yourself sitting in a black void, with just your keyboard in front of you.", tocont)
    scroll("...", tocont)
    scroll("Out of the corner of your eye, you see something move.", tocont)
    
    tuxAnnoyed2("")
    time.sleep(.6)
    scroll(white + "What was that!?", tocont)
    scroll("...", tocont)
    scroll("It was probably just my imagination..", tocont)
    time.sleep(1.5)
    tuxAnnoyed2("")
    time.sleep(.3)
    tuxAnnoyed1("")
    time.sleep(.3)
    tux("", "")
    time.sleep(2)
    
    tuxMouthOpen("Hello there!", "")
    console(tocont)
    
    tux("I'm your friendly neighborhood penguin, Tux!", "")
    console(tocont)
    
    tuxMouthOpen("Welcome to LarkOS!", "")
    console(tocont)
    
    tux("...", "R")
    console(tocont)
    
    tuxMouthOpen("I'm guessing you want to get out of here, right?", "")
    console(tocont)
    
    tux("Well guess what? You can!", "")
    console(tocont)
    
    tuxMouthOpen("All you have to do is learn a few Linux commands...", "L")
    console(tocont)
    
    # Set the username
    while True:
        tux("Why don't you tell me your name?", "")
        a = console("")
        if a == "":
            continue
        else:
            tux("Your name is " + green + a + white + ", correct? " + blue + "(y/n)", "")
            b = console("")
            if b == "y" or b == 1:
                global username
                username = a
                break
            else:
                tuxAnnoyed1(red + "Geez. Make up your mind already.")
                console(tocont)
                continue

    tuxAnnoyed2("Nice to meet you, " + username + "!")
    console(tocont)

    scroll("Why would he make that face?", tocont)

    tuxMouthOpen("Alright let's just jump into some commands!", "")
    console(tocont)

    display_output = True
    commandCheck("Type " + blue + "ls " + white + "into the command line and press enter.", "ls")

    tux("This lists files and folders in the current directory.", "")
    console(tocont)
    tux("Oh, before we continue, there's something you need to know.", "")
    console(tocont)  
    tux("See those hearts above your command line?", "LD")
    console(tocont)
    tux("Let's just say...", "")
    console(tocont)
    tuxAnnoyed1(red + "You don't want to test my patience.")
    console(tocont)
    tuxMouthOpen("Right-o, moving on!", "")
    console(tocont)
    tux("We just used 'ls' to list everything in the current directory.", "")
    console(tocont)
    tuxMouthOpen("But how do we know our path? Where are we specifically?", "")
    console(tocont) 

    commandCheck("Type " + blue + "pwd", "pwd")

    tux("This shows us the full path to our working directory.", "")
    console(tocont)
    tuxMouthOpen("But what if we want to move somewhere else?", "")
    console(tocont)
    tux("You can do that with the cd command.", "")
    console(tocont)
    
    commandCheck("Type \'" + blue + "cd .." + white + "\' to move to the parent directory.", "cd ..")
    display_output = False

    tuxSpeechless("Wait...")
    console(tocont)
    tuxSpeechless("Nothing happened...")
    console(tocont)  
    tux("Or did it?", "R")
    console(tocont)

    display_output = True
    commandCheck(blue + "List the contents of the current directory again.", "ls")

    tuxMouthOpen("As you can see, the files and folders have changed.", "")
    console(tocont)
    tux("'cd ..' moves you up a directory.", "")
    console(tocont)

    display_output = False
    commandCheck("Now type " + blue + "cd game_files " + white + "to take us back.", "cd game_files")

    tux("Okay you can probably guess that the cd command lets you change your current directory.", "")
    console(tocont)
    tuxMouthOpen("Now, listen closely. The next command I want to sho-", "")
    console(tocont)

    scroll(green + "Hey there! Forget about that penguin for a second.", tocont)
    scroll(green + "You want to test out these commands, right?", tocont)
    scroll(green + "Well you're in luck!", "")
    scroll(green + "You're able to switch between command mode and game mode.", tocont)
    scroll(green + "In command mode, the game will pause and you will be able to use the terminal to your heart's content!", tocont)
    scroll(green + "When you switch back to game mode, the game will resume.", tocont)
    scroll("Give it a try! Type " + blue + "m " + white + "to switch to command mode. Experiment with some of the commands you just learned.", "")
    
    tux("....", "")
    console(tocont)
    tuxAnnoyed1("..........")
    console(tocont)
    tuxAnnoyed1("You just spaced out for a second.")
    console(tocont)
    tuxAngry1(red + "Pay attention.")
    console(tocont)

    chap2()

def chap2():
    global health
    global display_output
    global usr_input
    display_output = False

    tux("We're going to learn how to read files.", "")
    console(tocont)

    detectInFolder(blue + "Find and cd into the folder titled: 'one'", "/rooms/one")

    tuxMouthOpen("(pfft, this is going to be good)", "L")
    console(tocont)
    tux("Okay, listen.", "")
    console(tocont)
    tux("You can read files using 'cat filename'", "")
    console(tocont)
    
    commandCheckMode("Using cat, read joe.txt and " + blue + "tell me its contents.", "mama")

    tuxMouthOpen("Hahaha! That never gets old!","R")
    console(tocont)
    tuxAnnoyed1("Why aren't you laughing?")
    console(tocont)

    a = scroll("Laugh? " + blue + "(y/n)", "")
    if a == "y" or a == "Y":
        tuxAngry1(red + "Good. That's what I expected from my future hos-.")
        console(tocont)
        tux("I mean.. umm...", "L")
        console(tocont)
        tux("...", "R")
        console(tocont)
    else:
        health -= 1
        tuxAngry1("...")
        console(tocont)
        scroll(red + "You lost one heart.", tocont)
    
    tux("Let's learn about the echo command!", "")
    console(tocont)
    tuxMouthOpen("The echo command outputs whatever you write to the terminal.", "")
    console(tocont)
    tux("For example: 'echo echo' would echo the word echo.", "R")
    console(tocont)
    tuxMouthOpen("Simple, right?", "")
    console(tocont)

    detectInFolder(blue + "Find and 'cd' into the folder titled: 'cave'", "/rooms/one/cave")

    tuxMouthOpen("Let me fill you in on a little secret...", "L")
    console(tocont)
    tux("Inside of this cave there's a secret passageway..", "")
    console(tocont)
    tux("It can only be opened when a certain phrase echos along the walls.", "")
    console(tocont)
    tux("However, I seem to have forgotten it...", "RD")
    console(tocont)
    tuxMouthOpen("Could you find it for me?", "")
    console(tocont)

    commandCheckMode(blue + "Find and echo the secret phrase. " + white + "I think this cave is called Azokh.", "echo secret_phrase23")
    
    tuxSpeechless("Yeah, I'm not good with secret passwords.")
    console(tocont)

    scroll("You hear the phrase echo along the walls of the cave.", tocont)
    scroll("Then, it gets really bright all of a sudden.", tocont)
    
    tux("...", "LD")
    console(tocont)
    tux("Okay, I have a confession.", "LD")
    console(tocont)
    tux("There is no cool secret passageway.", "RD")
    console(tocont)
    tux("That's just a voice command I use to turn the lights on.", "")
    console(tocont)
    tux("These smarthome devices really are something, huh?", "")
    console(tocont)
    tuxMouthOpen("I use the Amazon echo.", "")
    console(tocont)
    tux("...", "L")
    console(tocont)
    tuxAnnoyed1("Fine, I guess you do want to see a cool secret passageway, huh?")
    console(tocont)
    tux("Well, we can create one!", "")
    console(tocont)
    tuxMouthOpen("The 'mkdir' command creates a new folder.", "")
    console(tocont)
    tux("It " + green + "makes " + white + "a " + green + "directory", "")
    console(tocont)
    tuxMouthOpen("For example, 'mkdir hop' creates a new folder called 'hop'.", "")
    console(tocont)
    
    # Check for new folder
    attempt = 0
    while True:
        tux(blue + "Use the mkdir command to create a secret passageway. " + white + "You can name it anything.", "")
        print(green + "Note: Use command mode to make the directory. Then, continue in game mode.")
        console("")
        cd = os.listdir(os.getcwd())
        try:
            if cd[1]:
                break
        except IndexError:
            if attempt == 0:
                tuxAnnoyed1("You didn't make a folder...")
                console(tocont)
            else:
                health -= 1
                tuxAngry1("You didn't make a folder. " + red + "Lose a heart.")
                console(tocont)
            attempt += 1
    tuxSpeechless("Hmmm.. I know I said you could name it anything..")
    console(tocont)
    tuxAnnoyed1("But that name is kind of dumb for a secret passageway.")
    console(tocont)
    tux("Let's change it to something more interesting. Like... umm...", "LD")
    console(tocont)
    tuxMouthOpen("secret_passage!", "")
    console(tocont)
    tux("You can rename files using the 'mv' command.", "")
    console(tocont)
    tux("The syntax is 'mv [old_name] [new_name]'.", "")
    console(tocont)

    # Check for updated secret_passage folder
    detectNewFile("Rename the folder you just made to " + blue + "secret_passage", "/rooms/one/cave/secret_passage")
    
    tuxMouthOpen("Great, now we have a proper secret passageway!", "")
    console(tocont)
    tux("But it's kind of empty right now.", "R")
    console(tocont)
    tuxMouthOpen("Let's add some stuff!", "")
    console(tocont)
    tux("One way to create a file is to use the 'touch' command.", "")
    console(tocont)
    tuxMouthOpen("'touch file1' would create a new file named file1.", "")
    console(tocont)

    detectNewFile("Create a file called " + blue + "chair " + white + "in secret_passage", "/rooms/one/cave/secret_passage/chair")

    tuxMouthOpen("Great! Now I can finally sit down.", "")
    console(tocont)
    tuxAnnoyed2("...")
    console(tocont)

    scroll("Aren't you always sitting?", tocont)

    tuxAnnoyed1("That chair is pretty uncomfortable...")
    console(tocont)
    tux("Let's get rid of it.", "")
    console(tocont)
    tux("The 'rm' command removes a file or folder.", "")
    console(tocont)

    attempt = 0
    while True:
        tux("Use " + blue + "rm " + white + "to get rid of that chair.", "")
        print(green + "Note: Use command mode, and then continue in game mode.")
        console("")
        if os.path.exists(maindir + "/rooms/one/cave/secret_passage/chair"):
            if attempt == 0:
                tuxAnnoyed1("You didn't do what I wanted...")
                console("")
            else:
                health -= 1
                tuxAngry1("You failed to complete the task. " + red + "Lose a heart.")
                console("")
        else:
            break
        attempt += 1

    tux("Nice. That chair was pretty awful.", "")
    console(tocont)
    tuxMouthOpen("You know...", "L")
    console(tocont)
    tux("This secret passageway is kind of lame.", "")
    console(tocont)
    tuxMouthOpen("Let's just use it as extra storage for my secret cave phrases.", "")
    console(tocont)
    tux("How about we copy the file into our secret passageway?", "")
    console(tocont)

    while True:
        tuxMouthOpen("The command for copy is 'cp [filename] [newfilename]'", "")
        console(tocont)
        tux("For example, I want to copy a file to a folder named 'two'.", "")
        console(tocont)
        tux("I would use the command 'cp file two'", "")
        console(tocont)
        tuxMouthOpen("Also, you may need to add a '/' depending on where you are.", "")
        console(tocont)
        tux("'cp one/file two/file' copies the file from the 'one' folder into the 'two' folder", "")
        console(tocont)
        tuxMouthOpen("Do you understand? " + blue + "(y/n)", "")
        a = console("")
        if a == 'y':
            break
        else:
            tuxAnnoyed1("Fine. I'll explain it again.")
            console(tocont)
    
    tuxMouthOpen("Alright.", "")
    console(tocont)
    
    detectNewFile(blue + "Copy the file secret_phrases.txt into secret_passage. " + white + "Don't change the name.", "/rooms/one/cave/secret_passage/secret_phrases.txt")
    tux(green + "Nice.", "")
    console(tocont)

    tuxMouthOpen("You've learned a lot of commands so far.", "")
    console(tocont)
    tux("It would reflect poorly on me if you don't know what you're doing.", "")
    console(tocont)
    tuxMouthOpen("With that said-", "")
    console(tocont)
    tux("It's time for Tux's " + green + "Super Quiz!", "")
    console(tocont)
    tuxMouthOpen("What's the difference between a regular quiz and a " + green + "Super Quiz " + white + "you ask?", "L")
    console(tocont)
    tuxAnnoyed1("Well... let's just say you have a higher chance of meeting " + red + "an untimely demise.")
    console(tocont)
    tuxMouthOpen("Okay let's start!", "")
    console(tocont)

    superQuiz("What is the command that lists files/folders in the current directory?", "ls")
    superQuiz("What is the command that prints the current working directory?", "pwd")
    superQuiz("What is the command that lets you change directories?", "cd")
    superQuiz("What is the command that lets you read files?", "cat")
    superQuiz("What is the command that outputs anything to the terminal?", "echo")
    superQuiz("What is the command that lets you make a new folder?", "mkdir")
    superQuiz("What is the command that lets you create a new file?", "touch")
    superQuiz("What is the command that lets you copy files or folders?", "cp")

    tuxMouthOpen("Phew. Looks like you made it out alive.", "")
    console(tocont)
    health += 2
    tuxMouthOpen("Just for that, " + green + "I'll give you two hearts.", "")
    console(tocont)
    tuxAnnoyed1("Don't get used to my kindness.")
    console(tocont)

    chap3()

def chap3():
    global display_output
    global usr_input
    tuxSpeechless("Okay let's get out of this cave. It's gross.")
    console(tocont)

    detectInFolder("Find and enter the 'two' folder.", "/rooms/two")

    commandCheck("Use " + blue + "ls " + white + "to see what's in here.", "ls")

    tux("Hmmm... There doesn't appear to be anything in here.", "L")
    console(tocont)
    tuxMouthOpen("But what if there is?", "")
    console(tocont)
    tux("The normal 'ls' command won't work here.", "RD")
    console(tocont)
    tuxMouthOpen("However, if we add a '-a' after 'ls' we might see some hidden files.", "")
    console(tocont)

    commandCheckMode(blue + "Tell me what file you see " + white + "after typing 'ls -a'.", ".perm")

    display_output = True
    usr_input = "echo ''"
    commandCheck("Now, try to " + blue + "read " + white + "the contents of the '.perm' file.", "cat .perm")

    tuxAngry1("You just got denied. How does that feel?")

    console(tocont)
    tuxMouthOpen("Nah, I'm just pulling your leg.", "")
    console(tocont)
    tux("The real reason you can't read that file is because you don't have read permissions!", "")
    console(tocont)
    tux("To keep it simple...", "L")
    console(tocont)
    tuxMouthOpen("Each file has read (r), write (w), and execute (x) permissions.", "")
    console(tocont)
    
    commandCheck("Type " + blue + "ls -l .perm", "ls -l .perm")

    tuxMouthOpen("The '-l' after 'ls' gives extra information about a file.", "")
    console(tocont)
    tux("Take a look at the big line of dashes on the left.", "LD")
    console(tocont)
    tux("As you can see, you have write (w) permissions, but nothing else!", "LD")
    console(tocont)
    tuxMouthOpen("Let's fix that by giving yourself read permissions.", "")
    console(tocont)
    display_output = False
    tux("The 'chmod' command changes the permissions of files.", "")
    console(tocont)
    
    commandCheckMode("Type " + blue + "chmod u+r .perm " + white + "to gain read (r) access and " + blue + "tell me its contents.", "readable")

    tux("...", "R")
    console(tocont)
    tuxAnnoyed1("You didn't read anything you weren't supposed to, right?")
    console(tocont)
    tuxAnnoyed2("No matter. I'm tired now.")
    console(tocont)
    tuxAnnoyed2("I'm going to catch some Z's.")
    console(tocont)

    readOnce = False
    while True:
        if skip1 == True:
            break
        if readOnce == True:
            scroll("You wake Tux from his slumber...", tocont)
            if skip1 == True:
                break
            tuxAngry1("Why would you wake me up? What do you want?")
            console(tocont)
            if skip1 == True:
                break
            tuxAnnoyed1("Ugh, I'm too tired to be angry.")
            console(tocont)
            if skip1 == True:
                break
            tuxSpeechless("Oh! Again-")
            console(tocont)
            if skip1 == True:
                break

        tux("Definitely forget about " + blue + "chmod u+r " + white + "by the way. It's not important.", "L")
        console(tocont)
        if skip1 == True:
            break
        tux(blue + "chmod u+r " + white + "really isn't that cool of a command.", "R")
        console(tocont)
        if skip1 == True:
            break
        tux("Also, " + blue + "ls -a "  + white + "is pretty lame.", "L")
        console(tocont)
        if skip1 == True:
            break
        tuxAnnoyed2("Okay, Goodnight!")
        readOnce = True
        console(tocont)
        if skip1 == True:
            break
        scroll("Tux goes to sleep. Press enter to wake him up.", "")
