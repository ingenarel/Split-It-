```
 ________       ________    ___           ___      _________                ___      _________    ___
|\   ____\     |\   __  \  |\  \         |\  \    |\___   ___\             |\  \    |\___   ___\ |\  \
\ \  \___|_    \ \  \|\  \ \ \  \        \ \  \   \|___ \  \_|             \ \  \   \|___ \  \_| \ \  \
 \ \_____  \    \ \   ____\ \ \  \        \ \  \       \ \  \               \ \  \       \ \  \   \ \  \
  \|____|\  \    \ \  \___|  \ \  \____    \ \  \       \ \  \               \ \  \       \ \  \   \ \__\
    ____\_\  \    \ \__\      \ \_______\   \ \__\       \ \__\               \ \__\       \ \__\   \|__|
   |\_________\    \|__|       \|_______|    \|__|        \|__|                \|__|        \|__|       ___
   \|_________|                                                                                        |\__\
                                                                                                       \|__

    _                           _                              _                    _         _    _
   / \         ___  _   _  ___ | |_  ___   _ __ ___       ___ (_) _ __ ___   _   _ | |  __ _ | |_ (_)  ___   _ __
  / _ \       / __|| | | |/ __|| __|/ _ \ | '_ ` _ \     / __|| || '_ ` _ \ | | | || | / _` || __|| | / _ \ | '_ \
 / ___ \     | (__ | |_| |\__ \| |_| (_) || | | | | |    \__ \| || | | | | || |_| || || (_| || |_ | || (_) || | | |
/_/   \_\     \___| \__,_||___/ \__|\___/ |_| |_| |_|    |___/|_||_| |_| |_| \__,_||_| \__,_| \__||_| \___/ |_| |_|
                   _                            _  _  _    _                    __                   ____   _                        ___  _        _
  ___  __ _   ___ | |__    ___      ___  _ __  | |(_)| |_ | |_  ___  _ __      / _|  ___   _ __     / ___| | |__    ___   ___  _ __ |_ _|| |_     | |
 / __|/ _` | / __|| '_ \  / _ \    / __|| '_ \ | || || __|| __|/ _ \| '__|    | |_  / _ \ | '__|    \___ \ | '_ \  / _ \ / _ \| '_ \ | | | __|    | |
| (__| (_| || (__ | | | ||  __/    \__ \| |_) || || || |_ | |_|  __/| |       |  _|| (_) || |        ___) || | | ||  __/|  __/| |_) || | | |_     |_|
 \___|\__,_| \___||_| |_| \___|    |___/| .__/ |_||_| \__| \__|\___||_|       |_|   \___/ |_|       |____/ |_| |_| \___| \___|| .__/|___| \__|    (_)
                                        |_|                                                                                   |_|


 __  __               _            ____
|  \/  |   __ _    __| |   ___    | __ )   _   _
| |\/| |  / _` |  / _` |  / _ \   |  _ \  | | | |
| |  | | | (_| | | (_| | |  __/   | |_) | | |_| |
|_|  |_|  \__,_|  \__,_|  \___|   |____/   \__, |
                                           |___/
 ___   _   _    ____   _____   _   _      _      ____    _____   _
|_ _| | \ | |  / ___| | ____| | \ | |    / \    |  _ \  | ____| | |
 | |  |  \| | | |  _  |  _|   |  \| |   / _ \   | |_) | |  _|   | |
 | |  | |\  | | |_| | | |___  | |\  |  / ___ \  |  _ <  | |___  | |___
|___| |_| \_|  \____| |_____| |_| \_| /_/   \_\ |_| \_\ |_____| |_____|
```

```
Extract the zip, drag the exe in the same directory as your simulation folder. (NOT INSIDE THE SIMULATION FOLDER, BUT INSTEAD WHERE THE SIMULATION FOLDER IS!)
Then run the exe.
It will promt an installation folder.
Don't change it. install in the current directory. otherwise it won't work.
It's just a few bat files, a readme file and the license file. You can delete this later if you want to.
The password is split.
Why a password?
Because windows defender was flagging it as a virus. trojan to be exact.
However it's a false positive because I'm using a bat file to copy paste files.
So i password protected the exe and then put it in a zip and password protected it again.
PLEASE FOR GOD'S SAKE I DON'T RECCOMEND THIS IDEA FOR ANY OF YOUR PROJECTS AND IF SOMEONE USES THIS IDEA I CAN'T BE HELD ACCOUNTABLE! I'M JUST DESCRIBING WHAT I DID!
If somehow that's still gets flagged by defender, just go to defender, select the exe and allow threats.
If you don't trust the release tho, you can build it yourself. I showed that below.
```

```
________________________________________________________________________________________________________________________________________________________________________________
|:‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾:|
|: ██████╗ ██╗███████╗ ██████╗██╗      █████╗ ██╗███╗   ███╗███████╗██████╗ ██╗██╗██╗                                                                                         :|
|: ██╔══██╗██║██╔════╝██╔════╝██║     ██╔══██╗██║████╗ ████║██╔════╝██╔══██╗██║██║██║                                                                                         :|
|: ██║  ██║██║███████╗██║     ██║     ███████║██║██╔████╔██║█████╗  ██████╔╝██║██║██║                                                                                         :|
|: ██║  ██║██║╚════██║██║     ██║     ██╔══██║██║██║╚██╔╝██║██╔══╝  ██╔══██╗╚═╝╚═╝╚═╝                                                                                         :|
|: ██████╔╝██║███████║╚██████╗███████╗██║  ██║██║██║ ╚═╝ ██║███████╗██║  ██║██╗██╗██╗                                                                                         :|
|: ╚═════╝ ╚═╝╚══════╝ ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝╚═╝                                                                                         :|
|:                                                                                                                                                                            :|
|: THIS IS JUST A TEST PROJECT! I'M JUST AN AMATEUR PROGRAMMER! I LEARNED TO CODE THIS WHILE I WAS ALSO CODING IT SO THERE MAY BE STILL SOME BUGS LEFT!!!                     :|
|: THIS WILL ONLY WORK FOR FLUID CACHES ONLY! (As far as I know.. Haven't tested with others yet....)                                                                         :|
|: This is because I only know how fluid cache files works and i haven't really worked it other simulations yet such as smoke and fire, particle systems...                   :|
|: I'll eventually learn them too and then i'll try to upgrade it!                                                                                                            :|
|: I'll also try to make a smart cache splitter where it will split the files based on their sizes.                                                                           :|
|: But for now you will have to set how many splits you want to make.                                                                                                         :|
|: I'll also try to integrate 7-zip with this so it can automatically zip your project for you. but i'm dumb and it's too much for my brain so i'll do that in the future.    :|
|: If you have any suggestions and you know how to do it, I'll appreciate the help!                                                                                           :|
|: I'm just a member of the SheepIt community i'm not a dev so if i make any errors it's my fault not theirs!                                                                 :|
|:                                                                                                                                                                            :|
|:                                                                                                                                                                            :|
|:____________________________________________________________________________________________________________________________________________________________________________:|
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
```

introducing split it!

an auto cache splitter for sheepit!

Just download the release file. I created an sfx archive so you don't need to copy paste 17 bat files in your simulation cache directory for it to work lol.

Download the exe and move it to in the same directory as your simulation cache is. run the exe. it's pretty straighforward.

enjoy!

This is actually my first actual program that does anything so it's not that good.

```

________________________________________________________________________________________________________________________________________________
|:‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾:|
|:   Wanna support me?                                                                                                                        :|
|:                                                                                                                                            :|
|:   SUPPORT THE SHEEPIT DEVS!!!! -                                                 https://www.sheepit-renderfarm.com/donation               :|
|:                                                                                                                                            :|
|:   Follow me on Instagram -                                                       https://www.instagram.com/saad_abdullah999666/            :|
|:   Reddit account -                                                               https://reddit.com/user/INGENAREL                         :|
|:   Discord -                                                                      ingenarel#2846                                            :|
|:   My youtube channel -                                                           https://www.youtube.com/channel/UC90Tar8Bpx3Q8UqpM8qxWZw  :|
|:   Sponsor me on SheepIt -                                                        https://www.sheepit-renderfarm.com/user/ingenarel/profile :|
|:   Here's my public renderkey if you wanna connect a device to my account -       XQVDMUjdOKt7LBldxjuF0YERqLoGnExbeh8yUrce                  :|
|:                                                                                                                                            :|
|:____________________________________________________________________________________________________________________________________________:|
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
```

# How to create the sfx file yourself:
## Step 1: Download the source code
### 1. Go to releases
![image](https://github.com/ingenarel/Split-It/assets/145784829/8eea42f5-b9be-4f7c-a729-702a66b111b0)
### 2. Go to downloads
![image](https://github.com/ingenarel/Split-It/assets/145784829/d1b468ad-db29-44d0-9553-53895566ad27)
### 3. Then either download the zip file or tar.gz file
![image](https://github.com/ingenarel/Split-It/assets/145784829/a4675ce7-1b11-443e-8e20-abfddb6cfe86)

### Step 2: Make the sfx file (self extracting exe file) with winrar:
I know that you can use 7-zip to do this. But I find it complex so i'm just gonna use winrar.
### 1. Extract the source code.
### 2. Select all the files, left click, and create an archive with winrar.
![image](https://github.com/ingenarel/Split-It/assets/145784829/04b90897-873c-44b6-9887-85cc86b7719a)
### 3. Choose any type of archive method and check the "Create sfx archive box"
![image](https://github.com/ingenarel/Split-It/assets/145784829/68b5bd26-1c33-4000-8da0-469995e175da)
### 4. Go to the advanced tab and click the sfx options
![image](https://github.com/ingenarel/Split-It/assets/145784829/259bc31b-f3bb-4c58-aaf0-b9b05d6878f0)
### 5. Go to the setup tab an in the run after extraction menu, copy and paste this: "Split_It.bat" (Don't use qoutation marks)
![image](https://github.com/ingenarel/Split-It/assets/145784829/fdf78ca3-ae61-4fe3-a619-593cf264b579)
### 5. Then click ok. and click ok again.

Now whenever you need to split your caches. drag and drop it where your simulation cache folder is, 
(NOT INSIDE THE SIMULATION FOLDER, BUT INSTEAD WHERE THE SIMULATION FOLDER IS!) and then run and install it in the current directory. 
It will promt an installation folder.
Don't change it. install in the current directory. otherwise it won't work.
It's just a few bat files, a readme file and the license file. You can delete this later if you want to.
It will autorun the files that are necessary...
And if windows defender still blocks it, select it and allow threats.
