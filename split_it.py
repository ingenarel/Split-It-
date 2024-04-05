#Importing Modules
import ctypes, os, shutil, zipfile, requests

#The Software startup and telling what is needed.
def start(**kwargs):
    ctypes.windll.kernel32.SetConsoleTitleW(kwargs["title"])
    print("""
________       ________    ___           ___      _________                ___      _________    ___
|\\   ____\\     |\\   __  \\  |\\  \\         |\\  \\    |\\___   ___\\             |\\  \\    |\\___   ___\\ |\\  \\
\\ \\  \\___|_    \\ \\  \\|\\  \\ \\ \\  \\        \\ \\  \\   \\|___ \\  \\_|             \\ \\  \\   \\|___ \\  \\_| \\ \\  \\
 \\ \\_____  \\    \\ \\   ____\\ \\ \\  \\        \\ \\  \\       \\ \\  \\               \\ \\  \\       \\ \\  \\   \\ \\  \\
  \\|____|\\  \\    \\ \\  \\___|  \\ \\  \\____    \\ \\  \\       \\ \\  \\               \\ \\  \\       \\ \\  \\   \\ \\__\\
    ____\\_\\  \\    \\ \\__\\      \\ \\_______\\   \\ \\__\\       \\ \\__\\               \\ \\__\\       \\ \\__\\   \\|__|
   |\\_________\\    \\|__|       \\|_______|    \\|__|        \\|__|                \\|__|        \\|__|       ___ 
   \\|_________|                                                                                        |\\__\\
                                                                                                       \\|__|

    _                           _                              _                    _         _    _
   / \\         ___  _   _  ___ | |_  ___   _ __ ___       ___ (_) _ __ ___   _   _ | |  __ _ | |_ (_)  ___   _ __
  / _ \\       / __|| | | |/ __|| __|/ _ \\ | '_ ` _ \\     / __|| || '_ ` _ \\ | | | || | / _` || __|| | / _ \\ | '_ \\
 / ___ \\     | (__ | |_| |\\__ \\| |_| (_) || | | | | |    \\__ \\| || | | | | || |_| || || (_| || |_ | || (_) || | | |
/_/   \\_\\     \\___| \\__,_||___/ \\__|\\___/ |_| |_| |_|    |___/|_||_| |_| |_| \\__,_||_| \\__,_| \\__||_| \\___/ |_| |_|
                   _                            _  _  _    _                    __                   ____   _                        ___  _        _
  ___  __ _   ___ | |__    ___      ___  _ __  | |(_)| |_ | |_  ___  _ __      / _|  ___   _ __     / ___| | |__    ___   ___  _ __ |_ _|| |_     | |
 / __|/ _` | / __|| '_ \\  / _ \\    / __|| '_ \\ | || || __|| __|/ _ \\| '__|    | |_  / _ \\ | '__|    \\___ \\ | '_ \\  / _ \\ / _ \\| '_ \\ | | | __|    | |
| (__| (_| || (__ | | | ||  __/    \\__ \\| |_) || || || |_ | |_|  __/| |       |  _|| (_) || |        ___) || | | ||  __/|  __/| |_) || | | |_     |_|
 \\___|\\__,_| \\___||_| |_| \\___|    |___/| .__/ |_||_| \\__| \\__|\\___||_|       |_|   \\___/ |_|       |____/ |_| |_| \\___| \\___|| .__/|___| \\__|    (_)
                                        |_|                                                                                   |_|""")

    print("""
________________________________________________________________________________________________________________________________________________________________________________
|:‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾:|
|: ██████╗ ██╗███████╗ ██████╗██╗      █████╗ ██╗███╗   ███╗███████╗██████╗ ██╗██╗██╗                                                                                         :|
|: ██╔══██╗██║██╔════╝██╔════╝██║     ██╔══██╗██║████╗ ████║██╔════╝██╔══██╗██║██║██║                                                                                         :|
|: ██║  ██║██║███████╗██║     ██║     ███████║██║██╔████╔██║█████╗  ██████╔╝██║██║██║                                                                                         :|
|: ██║  ██║██║╚════██║██║     ██║     ██╔══██║██║██║╚██╔╝██║██╔══╝  ██╔══██╗╚═╝╚═╝╚═╝                                                                                         :|
|: ██████╔╝██║███████║╚██████╗███████╗██║  ██║██║██║ ╚═╝ ██║███████╗██║  ██║██╗██╗██╗                                                                                         :|
|: ╚═════╝ ╚═╝╚══════╝ ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝╚═╝                                                                                         :|
|:                                                                                                                                                                            :|
|: THIS IS JUST A TEST PROJECT! SO THERE MAY BE STILL SOME BUGS LEFT!!!                                                                                                       :|
|: THIS WILL ONLY WORK FOR FLUID CACHES ONLY! (As far as I know.. Haven't tested with others yet....)                                                                         :|
|: This is because I only know how fluid cache files works and i haven't really worked it other simulations yet such as smoke and fire, particle systems...                   :|
|: I'll eventually learn them too and then i'll try to upgrade it!                                                                                                            :|
|: I'll also try to make a smart cache splitter where it will split the files based on their sizes.                                                                           :|
|: But for now you will have to set how many splits you want to make.                                                                                                         :|
|: If you have any suggestions and you know how to do it, I'll appreciate the help!                                                                                           :|
|: I'm just a member of the SheepIt community i'm not a dev so if i make any errors it's my fault not theirs!                                                                 :|
|:                                                                                                                                                                            :|
|:____________________________________________________________________________________________________________________________________________________________________________:|
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

For the best visual experience, please Maximise the Terminal/Command Prompt.

BEFORE YOU START THIS MAKE SURE THAT YOU HAVE DOUBLE THE EMPTY SPACE IN YOUR DRIVE AS YOUR BLEND AND CACHE FILE COMBINED!
THAT MEANS IF YOUR BLEND FILE IS 100 mb AND YOUR SIMULATION CACHE FOLDER IS 900 mb, MAKE SURE THAT YOU HAVE ATLEAST 2 gb OF EMPTY SPACE IN YOUR DRIVE!""")
    please_enter_your_simulation_folder_name()
    return

#Printing the "please enter your Simulation folder name" text
def please_enter_your_simulation_folder_name():

    print(""" ____   _                                        _
|  _ \\ | |  ___   __ _  ___   ___    ___  _ __  | |_  ___  _ __   _   _   ___   _   _  _ __
| |_) || | / _ \\ / _` |/ __| / _ \\  / _ \\| '_ \\ | __|/ _ \\| '__| | | | | / _ \\ | | | || '__|
|  __/ | ||  __/| (_| |\\__ \\|  __/ |  __/| | | || |_|  __/| |    | |_| || (_) || |_| || |
|_|    |_| \\___| \\__,_||___/ \\___|  \\___||_| |_| \\__|\\___||_|     \\__, | \\___/  \\__,_||_|
      _                    _         _    _                  __   |___/ _      _
 ___ (_) _ __ ___   _   _ | |  __ _ | |_ (_)  ___   _ __    / _|  ___  | |  __| |  ___  _ __   _ __    __ _  _ __ ___    ___
/ __|| || '_ ` _ \\ | | | || | / _` || __|| | / _ \\ | '_ \\  | |_  / _ \\ | | / _` | / _ \\| '__| | '_ \\  / _` || '_ ` _ \\  / _ \\
\\__ \\| || | | | | || |_| || || (_| || |_ | || (_) || | | | |  _|| (_) || || (_| ||  __/| |    | | | || (_| || | | | | ||  __/
|___/|_||_| |_| |_| \\__,_||_| \\__,_| \\__||_| \\___/ |_| |_| |_|   \\___/ |_| \\__,_| \\___||_|    |_| |_| \\__,_||_| |_| |_| \\___|""")
    main_func()
    return

#Successfuly splitted it.
def success_msg():
    print(""" ____    _   _    ____    ____   _____   ____    ____    _   _   _ 
/ ___|  | | | |  / ___|  / ___| | ____| / ___|  / ___|  | | | | | |
\\___ \\  | | | | | |     | |     |  _|   \\___ \\  \\___ \\  | | | | | |
 ___) | | |_| | | |___  | |___  | |___   ___) |  ___) | |_| |_| |_|
|____/   \\___/   \\____|  \\____| |_____| |____/  |____/  (_) (_) (_)
          """)
    return

#Something went wrong while splitting.
def error_msg():
    print("""
                vXFAAAAAAAAAAAAAAAAAAAAAAAAAAOR2r
   p6HAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABCBBBBZy
         hYDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPw
               VAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA3
               fAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7
                RAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAL
                dAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAV
                PAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA                 
               sAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA3                
               kAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK                 _   _           __  _  _                        __         _      _
                mVVXYZZ36777987ZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv               | \\ | |  ___    / _|(_)| |  ___    ___   _ __   / _|  ___  | |  __| |  ___  _ __
                                  fRAAAAAAAAAAAAAAAAAAAAXv          wbMAAAAAAAAAAAAAA8              |  \\| | / _ \\  | |_ | || | / _ \\  / _ \\ | '__| | |_  / _ \\ | | / _` | / _ \\| '__|
                                     sAAAAAAAAAD0z      tmmz            8AAAAAAAAAAAAA5             | |\\  || (_) | |  _|| || ||  __/ | (_) || |    |  _|| (_) || || (_| ||  __/| |
                                       kAAAAAAi        AAAAV      p     BAAAAAAAAAAAAAAh            |_| \\_| \\___/  |_|  |_||_| \\___|  \\___/ |_|    |_|   \\___/ |_| \\__,_| \\___||_|
                                        eAAAAAABe                   s7EAAAAAAAAAAAAAAAAAb             __                           _   _              _    _             _
          qCAAAAABX6ffbdkmjchiaht       gAAAAAAAAA     qe94567992AAAAAAAAAAAAAAAAAAAAAAAAh           / _|  ___   _   _  _ __    __| | | |__   _   _  | |_ | |__    __ _ | |_
            0AAAAAAAAAAAAAAAAAAA0       nAAAAAAAAAx   XAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA          | |_  / _ \\ | | | || '_ \\  / _` | | '_ \\ | | | | | __|| '_ \\  / _` || __|
               kcVKHAAAAAAAAAA2x         AAAAAAAAA9   hDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAV         |  _|| (_) || |_| || | | || (_| | | |_) || |_| | | |_ | | | || (_| || |_
                    kAAAAAAAAR           3AAAAAAAAX   t9UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA         |_|   \\___/  \\__,_||_| |_| \\__,_| |_.__/  \\__, |  \\__||_| |_| \\__,_| \\__|
                      6AAAAAZ            lAAAAAAAAA       FAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA                                                   |___/
                       8AAAZ             gAAAAAAAAAAf     fAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF                                              ____  _                  _
                                         AAAAAAAAAAAAAr    hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAo          _ __    __ _  _ __ ___    ___      / ___|| |__    ___   ___ | | __  _   _   ___   _   _  _ __
                                         TAAAAAAAAAAAAa     zAAAAAAAAAAAAAAAAAAAAAAAAAAAAA          | '_ \\  / _` || '_ ` _ \\  / _ \\    | |    | '_ \\  / _ \\ / __|| |/ / | | | | / _ \\ | | | || '__|
                                           kEAAAAAAAAO      ZAAAAAAAAAAAANkQAAAAAAAAAAAAAh          | | | || (_| || | | | | ||  __/ _  | |___ | | | ||  __/| (__ |   <  | |_| || (_) || |_| || |   
                                              wh6WRF3     oNAAAAAAAAAAAAA9   4AAAAAAAAAAE           |_| |_| \\__,_||_| |_| |_| \\___|(_)  \\____||_| |_| \\___| \\___||_|\\_\\  \\__, | \\___/  \\__,_||_|   
                                                       vAAAAAAAAAAAAAAAAAA6   oAAAAAAAAE                               _  _  _                                      _    |___/                     
                                                      BAAAAAAAAAAAAAAAAAAAAP    2AAAAAAy             ___  _ __    ___ | || |(_) _ __    __ _    __ _   __ _   __ _ (_) _ __                        
                                            aAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa   AAAAA7             / __|| '_ \\  / _ \\| || || || '_ \\  / _` |  / _` | / _` | / _` || || '_ \\                       
                                             8RRNAAAAAAAAAAAAAAAAAAAAAAAAAAAAA9   AAAE              \\__ \\| |_) ||  __/| || || || | | || (_| | | (_| || (_| || (_| || || | | | _                    
                                  kEAA7sy               s9221ZYXWKAAAAAAMUZ45d    AAAl              |___/| .__/  \\___||_||_||_||_| |_| \\__, |  \\__,_| \\__, | \\__,_||_||_| |_|(_)                   
                                 pGAAAAAAAAAAAAGeoz                          qu   AAp                    |_|                           |___/          |___/                                        
                                   vUAAAAAAAAAAAAAAAAAAAAAWefgeeeffffffg5AAAAAAAeHAH
                                     2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg
                                     XAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                                    cDAAAAAOUHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD
                                    5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAz
                                     WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                                    ZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7
                                    LAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                                    XAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD
                                     aAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAr
                                    vTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAd
                                      cAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                                         oBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAX
                                           u7CAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAY
                                               mfKAAAAAAAAAAAAAAAAAAAAAAAAARw
                                                   tkeLAAAAAAAAAAAAAAABXw""")
    return

#The splitter is done message
def end():
    print("""Your splitting is finished. yayyyyyyy!!!!!

++++++++++++++++**++*%#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++@*#+###+%*#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++*%*+@+@#*#*%+**+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++*#*#@**#++#++@++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#@++#@++++++++
+++++++++++++*#**++++++++@%##++++++++++++++++++++++++++++++++++++++++++++++++++++++++#**#+##++##++++
++++++++++++++@+++*****+*#+*#+++++++++++++++++++++++++++++++++++++++++++++++++++++**+@*+#@*@*%*%++++
++++++++++++++@+++****%**++@+++++++++++++++++++++++++++++++++++++++++++++++++++++***#%++++*##+#+++++
++++++++++++++%#******+*++%++++++++++++++++++++++++++++++++++++++++++++++++++++++**+#*+*+++++#*%#%%+
+++++++++++++##+++++++++*#%*+++++++++++++++++++++++++++++++++++++++++++++++++++++**++*******+***%*++
+++++++++++++#++++++++++***#*++++++++++++++++++++++++++++++++++++++++++++++++++++*#+++*#***+++**++++
++++++++++++##+*#%%%%%%%%#*#*+++++++++++++++++++++++++++++++++++++++++++++++++++##%##***+*+++*#+++++
++++++++++++@@@@%%%###%%%%@@#+++++++++++++++++++++++++++++++++++++++++++++++++#*+++++++*###+#%++++++
++++++++++++@%*++++++++****#%++++++++++++++++++++++++++++++++++++++++++++++++**++++++++++++##+++++++
+++++++++++##+#%###***##%%%#@+++++++++++++++++++++++++++++++++++++++++++++++%*++++++++++++***%++++++
+++++++++++*%#*********###%@*+++*#%##***+++++++***##%%%%**++++++++++++++++*@@@@@@@@@@%#*****#%++++++
++++++++++++%**********###%@*%%#+++++++++++*#+*+++++++++*#%@%*++++++++++++@*+****++**%@@@%#*%+++++++
++++++++++++#**********##%%#*++++++*++++++#*#+#+++++*++++++++*#%#+++++++++%*######%%%#**#%@@#+++++++
+++++++++++#**********#%#+++++++++*+++++*#**#+#+++++*+++++++++++*#%#+++++++#%##########%%*#@++++++++
+++++++++++#********#%#++++*++*++#+++++*#***#+#+++++**+++++++*++**+*%%+++++%*******######@##++++++++
++++++++++##*******%%+++++*++**+*+++++*#***+*+#+++++**+++++++*+++***++#%+*%***********##%@%+++++++++
++++++++++@#*****#%*+++++**+*%**#*****#***++**%++++++#+++++++*++++**+++*%%#************#%+++++++++++
+++++++++*%*****##+++++++#**%#*%*****#***+++*#%#*****%**+++++**++++**+++*%************#@++++++++++++
+++++++++##****%*+++*+**#**#%*#%#%%%%**++++++##%***##%@%******#+++++#*++%*************%*++++++++++++
+++++++++%***#%++*******@**%##@****%**+++++++*#%******##**#***%******#+##************#%+++++++++++++
+++++++++#**##++*******##**##*%***##*++++++++++*******%#******#******##%*************%*+++++++++++++
++++++++##*#*+*****#**#*#*#***#+**#*+++++++++++++++*#***%******%*****#%**********#**##++++++++++++++
++++++++@%#+******#***#*++++***#*##*+++++++++++++*##***********%#****##*************#+++++++++++++++
++++++*#*+*#**#***#**#**++**##%%%%***+++++++++++**##%%%%%%%###**%****#*************##+++++++++++++++
++*%@*+**%##*********#**#%%%#****#%@*+++++++++++*%%#******#%@%***#**##*************%++++++++++++++++
++++***##*%*+#*******#%%%*++++**++++++++++++++++++++#%%%%%#+*%@%+*###*************##++++++++++++++++
+++++++%##@**%***#*+%%%*+++*#%%%%%*++++++++++++++++++*%%%%%%++#@%+*%#************#%+++++++++++++++++
+++++++%**%**#**+#**%%*+++++*%%%%%%*+++++++++++++*%###%@%%%@#++#@###*************##+++++++++++++++++
+++++++%*****#***##*@#++*@@%*****%@#+++++++++++++%#+++++**@@%++*@%%**************@*+++++++++++++++++
+++++++%*******##****+++#@*+++++++#*+++++++++++++%++++*+++*%*+++*%#*************##++++++++++++++++++
+++++++#*******##**#*+++*%*++++++**++++++++++++++*%*++++++#*+++*#%***********#**%@++++++++++++++++++
++++++*%******###*+*++++*+#*****++++++++++++++++++++****#*++++*#%##*******#######@*+++++++++++++++++
++++++*%*****#%*#*++*++*++*+++++++++++++++++++++++++++++++++**#*%********######@*@++++++++++++++++++
++++++*#*****#**#*++*++****++++++++++++++++++++++++++++++*+**#+%#******#########*%#+++++++++++++++++
++++++*%*****#+***++++++**++++++++++++++******++++++++++++++%*#%*******#######%**##+++++++++++++++++
++++++*%****%*++**++++++++++++++++*#%##*********#*++++++*++*#*@#******#########**##+++++++++++++++++
++++++*%***##++*%+++++++++++++++++####**********#*++++++++*#+#%*******#######%***##+++++++++++++++++
+++++++#***#+++*%+++++++++++++++++*#************#*++++++++%*+##*******######%#****%+++++++++++++++++
+++++++%***#+++*##+++++++++++++++++%************#++++++++##+*##*******######%*****%+++++++++++++++++
+++++++%#*#*+++**%*+++++++++++++++++***********#+++++++++#+*%#*********####%#+****%+++++++++++++++++
+++++++#%##+++****%%+++++++++++++++++*********#*++++++++#*+*@#*********####%*+++++%+++++++++++++++++
+++++++*@#*+++*****#@#*+++++++++++++++++++++*++++++++++*%+*##**********####%+++++*%+++++++++++++++++
++++++++@%+++****##%##%%#++++++++++++++++++++++++++++++#*+*##**********###%%*+++++##++++++++++++++++
++++++++*%+++****#%####%*#%#*++++++++++++++++++++++++*##+**#***********##%%#*+++++*@++++++++++++++++
+++++++++*+++***#######%#+%@**#%%%**++++++++++++**#%%#%****#***********##%%#*++++**@++++++++++++++++
++++++++**++****#%########*@#+******#**#%********#@#**@*+**#***********##%%*#++++++%#+++++++++++++++
++++++++@*++****%%#####**#*#@*++****####%********%***##+**##***********#%#*##*+++++*%+++++++++++++++
++++++++@*++****@#####****%+%@*+++**##**********#**++#*+**#*************%**#*#++++++%*++++++++++++++
++++++++@++*#**#%####******%*%@*++++*%#******##%*+++*%++**%************##***##*+++++*@++++++++++++++
++++++++@++****#%###*******##*%@*++++*#+****++#*+++*@#++**%************%*#**###++++++##+++++++++++++
++++++++@++****#%##**********###@#++++#*+++++##+++#@%#++*##***********#%*#***##%++++++%+++++++++++++


Please check your zip files before you upload your project.
Because, 
even if something works for someone it might not work for others.
I hope you have a great life""")

def cls_():
    os.system('cls' if os.name == 'nt' else 'clear')

def license():
    print("""
THE FUCK PAYING! ATTRIBUTE AND DONATE LICENSE (TFPADL)

Version 1.0

By using this piece of software, you agree to the following terms:

1. You are granted the right to use, modify, and redistribute this software under the following conditions:
    i) Your modified or unmodified version, and/or your own project using this software, must be distributed free of charge.
    ii) Proper attribution to the original authors must be provided.
    iii) If you receive donations related to the distribution or use of this software, you must encourage people to also donate to the original authors by providing a link to their website, account, donation links, or project page.
    iv) You must include the source code of your version, along with a link to the original version.

2. Use of this software is at your own risk. The original authors will not be responsible for any damages or liabilities arising from the use, modification, or distribution of this software.

3. The original authors reserve the right to change the terms of this license at any time without prior notice. You are obligated to comply with the updated terms.

4. Non-compliance with the terms of this license will result in the immediate termination of your rights to use this software and may lead to legal action.

Original Authors:
Ingenarel
""")

#Variables for runtime
class variables:
    #The title Variable
    local_version="v0.9"
    title=f"Split It! version {local_version}"
    
    #URL Specific stuff
    repo_owner = "ingenarel"
    repo_name = "Split-It"
    
    #folder specific variables for copying/other used in and for the "processing_folders" function
    folder_name=""
    
    #The lookup is for processing the folders and Variables for the "processing_folders" function
    folder_lookup={"1": "config", "2": "data", "3": "mesh", "4": "guiding", "5": "noise", "6": "particles"}
    current_folder=1
    max_folders=6

    output_dir=""

    file_count=0
    source_folder=""
    folder_list=""
    source_files=""
    source_file=""
    
    files_in_directory=""
    destination_base_folder="Destination"
    destination_folder="Destination"
    
    count=0
    folder_count=1
    
    exist_ok=True

#The function is for Listing the folders and setting the right folder (not yet checking if it is the right folder.)
def list_folders():
    try:
        while True:
            while True:
            #the input for the folder to copy from.
                variables.folder_name=input("Please enter your foldername. (CASE SENSITIVE!)")#.lower() #Just in case you change your mind.
                if variables.folder_name=="cls" or variables.folder_name=="clear":
                    cls_()
                else:
                    break
            variables.folder_list=[folder for folder in os.listdir('.') if os.path.isdir(folder)]
            #print(variables.folder_list) #For debugging if something goes to shit
            if variables.folder_name not in variables.folder_list:
                error_msg()
                
            else:
                return
            
    except KeyboardInterrupt:
        return

#Function for copying all the folders.
def processing_folders():
    #That while loop is for each folder "config, data, mesh, guiding, noise, particles"
    while variables.current_folder<variables.max_folders+1:
        while True:
            #That while loop is for the file count to not end up at 0
            if variables.file_count==0:
                while True:

                    variables.file_count=int(input("Enter the number of files to copy in to each folder: "))
                    
                    if variables.file_count >= 1:
                        break
                    else:
                        print("Nuh uh! There has to be at least 1 file. ")
                        continue
            
            #Getting the output directory and source folder.
            variables.output_dir=str(variables.folder_lookup.get(str(variables.current_folder)))
            variables.source_folder=os.path.join(variables.folder_name, variables.output_dir)

            #splitting >w<
            print(f"Please wait while I split the {variables.folder_lookup.get(str(variables.current_folder))} files... >.<")
            
            #If the folder doesn't exist, make one
            try:
                os.makedirs(os.path.join(variables.destination_base_folder, str(variables.folder_count), variables.folder_name, variables.output_dir), variables.exist_ok)
            
            #if the folder does exist, just pass out.
            except FileExistsError:
                pass
            
            #The actual copying finally happens.
            for filename in os.listdir(variables.source_folder):
                variables.source_file = os.path.join(variables.source_folder, filename)
                
                #Copy files to the current destination folder
                shutil.copy(variables.source_file, os.path.join(variables.destination_base_folder, str(variables.folder_count), variables.folder_name, variables.output_dir))
                
                variables.count+=1
                
                #If specified number of files are copied, reset the file counter and moce to the next destination folder
                if variables.count == variables.file_count:
                    variables.count=0
                    variables.folder_count+=1
                    try:
                        os.makedirs(os.path.join(variables.destination_base_folder, str(variables.folder_count), variables.folder_name, variables.output_dir))
                    except FileExistsError:
                        pass
            break
        
        #setting the variables back to what they should be
        variables.count=0
        variables.folder_count=1
        variables.current_folder+=1
        variables.output_dir=str(variables.folder_lookup.get(str(variables.current_folder)))
        print(variables.current_folder)
    
    #resetting the variables used that are needed to be resetted
    variables.count=0
    variables.folder_count=1
    variables.current_folder=1
    variables.output_dir=""
    blend_copypaste()

def blend_copypaste():
    while True:
        # Ask for source file name
        source_file = input("Enter the name of the blend file that you want to copy (with extension): ")

        if source_file.lower() in ["cls", "clear"]:  # Check for "cls" or "clear" inputs
            os.system('cls' if os.name == 'nt' else 'clear')
            continue  # Restart the loop without checking files

        # List files in the current directory (case sensitive)
        files_in_directory = os.listdir('.')

        # Check if source file exists (case sensitive)
        if source_file not in files_in_directory:
            error_msg()
        
        else:
            print("Please wait till I copy and paste the blend file in the correct folders... >.<")
            break

    # Destination folder name
    destination_folder = "Destination"

    # Check if destination folder exists, create if not
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate over immediate subdirectories in the Destination folder
    for directory in os.listdir(destination_folder):
        # Construct destination path
        destination_path = os.path.join(destination_folder, directory, os.path.basename(source_file))
        # Copy the file to each subdirectory
        shutil.copy2(source_file, destination_path)

    print("Blend file copy pasted successfully.")

    zip_files()
        

#The zipper function (No humans have been harmed at the making.)
def zip_files():
    #Zipping >w<
    print("Please wait while I zip the files... >.<")

    # Change directory to the destination folder
    os.chdir(variables.destination_folder)

    # Loop through each folder in the destination folder
    for variables.folder_name in os.listdir():
        if os.path.isdir(variables.folder_name):
            # Create a zip file with the same name as the folder
            with zipfile.ZipFile(f"Split-It-{variables.folder_name}.zip", "w") as zip_file:
                # Add all files and empty folders in the folder to the zip file
                for root, dirs, files in os.walk(variables.folder_name):
                    # Add files
                    for file in files:
                        zip_file.write(os.path.join(root, file),
                                    os.path.relpath(os.path.join(root, file),
                                                    os.path.join(variables.folder_name)))
                    # Add empty directories
                    for dir in dirs:
                        dir_path = os.path.relpath(os.path.join(root, dir),
                                                os.path.join(variables.folder_name))
                        zip_file.write(os.path.join(root, dir), dir_path)

    #Zipping finished and the user is being asked if they wanna delete the folders.
    print("All folders zipped successfully.")
    ask_deletion()

#Asking if filders (except the zip files!) want to be deleted.
def ask_deletion():
    while True:
        print("""
Do you want to delete the folders that were created when you split the project?
The zip files won't be deleted, just the folders and files that were created in order to make those zips.""")
        choice=input("y to delete and n to cancel: ").lower()[0:1]
        
        if choice=="y":
            # Loop through all items in the folder and delete them
            for item in os.listdir():
                if os.path.isdir(item):
                    os.system(f"rd /s /q \"{item}\"")
            print("\nAll split cache folders deleted successfully.\nDon't worry, the zips aren't deleted.")
            break
        
        elif choice.lower() in ["cls", "clear"]:
            cls_()
            continue
        
        else:
            print('Error: Please use euther "y" or "n"')
    os.chdir("..")
    success_msg()
    end()

def helpsite():
    print("""______________________________________________________________________________________________________________________________________________________
|:‾‾‾‾‾‾‾‾‾‾‾‾‾|‾‾‾‾‾‾‾‾‾‾‾‾|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾:|
|:   COMMAND   | ALSO KNOWN |                                                     DESCRIPTION                                                       :|
|:    NAME     |     AS     |                                                                                                                       :|
|:=============|============|=======================================================================================================================:|
|:             |            |   It checks your version. then displayes your current version and the latest version. If the current version is the   :|
|:             |            |  is updated than the latest stable built release, the says that you're using a version that is newer than the latest  :|
|:     ver     |   version  |   stable build. And if the current version is older than the latest version, it says that there is a newer version    :|
|:             |            |                 available. If the version is the same as the latest version, it just tells you that.                  :|
|:             |            |                                           Should work only on the main menu.                                          :|
|:=============|============|=======================================================================================================================:|
|:    cls      |   clear    |                            Clears the screen. Works anywhere where you can put an input.                              :|
|:=============|============|=======================================================================================================================:|
|:    exit     | esc, close |                                   Exits the program. Should work only on the main menu.                               :|
|:=============|============|=======================================================================================================================:|
|:             |            |    At first it goes to your cache folder. Then it takes the first x ammount files from the config file. x is you,     :|
|:             |            |   setting how much files it will take per folder. it could be 1/2/3 basically anything. Only an integer tho lol. It   :|
|:             |            |   pastes those files in a different folder. It will first create a folder called Destination. It will store all the   :|
|:             |            |  files and folders that are split. Then it creates another folder inside it that's the same name as your simulation   :|
|:             |            |     cache folder. And then create another folder called config inside it and then paste those files in the config     :|
|:             |            |                                   folder. To show it visually it's doing this...                                      :|
|:             |            |                                                                                                                       :|
|:             |            |                                         Destination                                                                   :|
|:             |            |                                           -> 1                                                                        :|
|:             |            |                                             ->simulation folder name                                                  :|
|:             |            |                                               ->config                                                                :|
|:             |            |                                                 ->the first x amount of files                                         :|
|:             |            |                                                                                                                       :|
|:             |            |   The next step is doing the same thing for all those files. Creates folders called 1, 2, 3 etc basically an unique   :|
|:             |            |                            folder for each x amount of files so now it looks like this...                             :|
|:             |            |                                                                                                                       :|
|:             |            |                                        Destination                                                                    :|
|:             |            |                                          -> 1                                                                         :|
|:             |            |                                            -> simulation folder name                                                  :|
|:             |            |                                              -> config                                                                :|
|:             |            |                                                -> the first x amount of files                                         :|
|:             |            |                                          -> 2                                                                         :|
|:             |            |                                            -> simulation folder name                                                  :|
|:             |            |                                              -> config                                                                :|
|:      s      |    start   |                                                -> the second x amount of files                                        :|
|:             |            |                                                                                                                       :|
|:             |            |   Then it does the same thing for the data and mesh folder in your simulation directory. then it asks questions it    :|
|:             |            |       would do with the guiding, noise, and particles folder. either split them too if they have files in them        :|
|:             |            |    (which i personally didn't have on my projects) or just create those folders that are named guiding, noise, and    :|
|:             |            |  particles in the split cache directory so it works properly. then it copy pastes your blend file in each sub folder  :|
|:             |            |                                       in the destination folder. that means...                                        :|
|:             |            |                                                                                                                       :|
|:             |            |                                        Destination                                                                    :|
|:             |            |                                          -> 1                                                                         :|
|:             |            |                                            -> your blend file                                                         :|
|:             |            |                                            -> simulation folder name                                                  :|
|:             |            |                                              -> config                                                                :|
|:             |            |                                                -> the first x amount of files                                         :|
|:             |            |                                                                                                                       :|
|:             |            |                                          -> 2                                                                         :|
|:             |            |                                            -> your blend file                                                         :|
|:             |            |                                            -> simulation folder name                                                  :|
|:             |            |                                              -> config                                                                :|
|:             |            |                                                -> the second x amount of files                                        :|
|:             |            |                                                                                                                       :|
|:             |            |  etc etc then it creates a zip for the 1 folder. then the 2 folder. so on and so on the zip files are created in the  :|
|:             |            |     Destination folder Then it asks you if it shoudld delete the subfolders that were created while the spliiting     :|
|:             |            |  happened. You can choose to delete them. If you wish to do so, it will delete those 1, 2, 3 folders. Deleting those  :|
|:             |            |   folders won't matter because you'll still have the zips.This functions was created so that you don't waste extra    :|
|:             |            |                                          space. Should work only on the main menu.                                    :|
|:=============|============|=======================================================================================================================:|
|:   license   |            |                                   Shows the licnese. Should work only on the main menu.                               :|
|:_____________|____________|_______________________________________________________________________________________________________________________:|
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
          """)
    
    # |::| - this is for the devs so that we can copy paste it every time we need to expand the box

def update_check(**kwargs):
    try:
        response=requests.get(kwargs["url"])
        if response.status_code == 200:
            latest_release = response.json()
            latest_version = latest_release.get('tag_name')

        else:
            if response.status_code==400:
                print("""ERROR 400: bad request.

This status code indicates that there's something off with the request you sent to the server.
It's like filling out a form incorrectly or forgetting to provide essential details.
The server couldn't understand or process your request due to missing or malformed data.
""")
        
            elif response.status_code == 401:
                print("""ERROR 401: Unauthorized
This status code means you're not allowed to access the requested resource without proper authentication.
It's like trying to enter a restricted area without showing your ID.
You need to provide valid credentials, such as a username and password or an authentication token, to gain access.
""")
        
            elif response.status_code == 403:
                print("""ERROR 403: Forbidden.

You're being denied access, plain and simple.")
Even with valid credentials, you're not allowed to access the resource because you lack the necessary permissions.
It's like trying to enter a building without the proper authorization or access card.
You need to request permission from the appropriate authorities.
""")
        
            elif response.status_code == 404:
                print("""ERROR 404: File not found.

This status code indicates that the server couldn't find the resource you requested.
It's like looking for a book on a library shelf only to discover it's not there. 
The resource may have been moved, deleted, or simply never existed. 
Double-check the URL or try searching for the resource in a different location.
""")
        
            elif response.status_code == 422:
                print("""ERROR 422: Unprocessable Entity.

Ah, it seems there's a problem with the data you provided. ")
This status code typically occurs when the server understands your request but can't process it due to invalid data.
It's like trying to fill out a form with incorrect or incomplete information. 
Review the data you submitted and ensure it meets the server's requirements.
""")
            
            elif response.status_code == 429:
                print("""ERROR 429: Too Many Requests.

Slow down there! You've been making too many requests to the server within a short period. ")
This status code indicates that you've hit a rate limit, and the server is asking you to ease up for a bit. ")
It's like trying to take too many slices of cake at once, and someone politely suggests you wait your turn.")
""")
        
            elif response.status_code == 500:
                print("""ERROR 500: Server Side Error.

Uh-oh, something went wrong on the server's end, and it's not your fault. 
This status code indicates an unexpected problem occurred while the server was trying to process your request.
It's like ordering food at a restaurant and having the kitchen catch fire. 
The server is apologizing for the inconvenience and asking for your patience while they sort things out.
""")
        
            elif response.status_code == 503:
                print("""ERROR 503: Server was not ready

Hold your horses! The server is currently unavailable to handle your request.
This status code typically occurs due to maintenance or overload.
It's like calling a store outside of business hours and getting a message saying they're closed for the day.
You'll need to try again later when the server is back up and running.
""")
            
            else:
                print(f"I Don't know what the fuck are you doing but I can't find an error code for you.\n")
    except requests.exceptions.RequestException:
        print("""
Failed to retrieve the latest version from GitHub.
Please check your internet connection.""")
        input("Press enter to return to the main menu.")
        return
    
    if latest_version:
        print(f"Current version: {variables.local_version}.")
        print(f"Latest version: {latest_version}.")
        
        if variables.local_version>latest_version:
            print("You're using a version that is newer than the latest stable built.")
    
        elif variables.local_version==latest_version:
            print("You are already using the latest version.")
        
        else:
            while True:
                print("A new version is available. Do you want to download it?")
                print("You if you want to use the latest version, you need to start it from the downloaded version though.")
                print("It creates a folder called latest_build and stores the zip there.")
                choice = input("press y to download and n to cancel: ")
                
                if choice.lower() == "y":
                    # Download the latest build
                    assets = latest_release.get('assets', [])
                    
                    if assets:
                        # Create a folder to store the downloaded files
                        download_folder = "latest_build"
                        os.makedirs(download_folder, exist_ok=True)

                        for asset in assets:
                            download_url = asset.get('browser_download_url')
                            download_response = requests.get(download_url)
                                
                            if download_response.status_code == 200:
                                # Save the file
                                file_path = os.path.join(download_folder, asset.get('name'))
                                with open(file_path, 'wb') as file:
                                    file.write(download_response.content)
                                print(f"Downloaded: {asset.get('name')}")
                                break
                            
                            #There has been an issue downloading
                            else:
                                print(f"Failed to download: {asset.get('name')}")
                                break

                        #Downloading is done 👍
                        print(f"All assets from the latest release have been downloaded to '{download_folder}'.")
                        break

                    #no assets found
                    else:
                        print("No assets found in the latest release.")
                        break

                #Skipped the download
                elif choice.lower() == "n":
                    print("Skipping download.")
                    break

                #Clearing the screen.
                elif choice.lower() in ["cls", "clear"]:
                    cls_()
                    continue

                #Choice was invalid...
                else:
                    print("Invalid choice. Please enter 'yes' or 'no'.")
                    continue
    else:
        print("Failed to retrieve the latest version from GitHub. Please check your internet connection and try again.")
        input("press enter to go back to the main menu.")

        return
    
def credits():
        print("""______________________________________________________________________________________________________________________________________________________________________
|:‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾:|
|:   Ingenarel                                                                                                                                                      :|
|:                                                                                                                                                                  :|
|:   Follow me on Instagram -                                                  https://www.instagram.com/saad_abdullah999666/                                       :|
|:   Reddit account -                                                          https://reddit.com/user/INGENAREL                                                    :|
|:   Discord -                                                                 ingenarel#2846                                                                       :|
|:   My youtube channel -                                                      https://www.youtube.com/channel/UC90Tar8Bpx3Q8UqpM8qxWZw?sub_confirmation=1          :|
|:   Sponsor me on SheepIt -                                                   https://www.sheepit-renderfarm.com/user/ingenarel/profile                            :|
|:   My github account -                                                       https://github.com/ingenarel                                                         :|
|:   Here's my public renderkey if you wanna connect a device to my account -  XQVDMUjdOKt7LBldxjuF0YERqLoGnExbeh8yUrce                                             :|
|:__________________________________________________________________________________________________________________________________________________________________:|
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
          """)
        
        print("""______________________________________________________________________________________________________________________________________________________
|:‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾:|
|:   Chaosminecraft                                                                                                                                 :|
|:   His youtube channel -                                                          https://www.youtube.com/@chaosminecraft3399                     :|
|:   Sponsor him on SheepIt -                                                       https://www.sheepit-renderfarm.com/user/Chaosminecraft/profile  :|
|:   His github account -                                                           https://github.com/Chaosminecraft                               :|
|:__________________________________________________________________________________________________________________________________________________:|
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
          """)

    # |::| - this is for the devs so that we can copy paste it every time we need to expand the box


#the main function that handles the stuff.
def main_func():
    while True:
        print("""
You can type "Ver" to check if an update is there.
You can type "cls" to clean the Terminal/Command Prompt.
Type "s" to use the splitter.
Type "help" for an in depth guide about every command
Type "c" for credits.        """) 
        
        starting_choice=input("What do you want to do? ").lower()
        
        #starting the main feature.
        if starting_choice in ["s", "start"]:
            list_folders()
            processing_folders()
        
        #Checking the version
        elif starting_choice in ["ver", "version"]:
            update_check(url=f"https://api.github.com/repos/{variables.repo_owner}/{variables.repo_name}/releases/latest")
        
        elif starting_choice in ["cls", "clear"]:
            cls_()
        
        #Closing the program
        elif starting_choice in ["esc", "exit", "close"]:
            exit()
        
        elif starting_choice == "license":
            license()

        elif starting_choice in ["credits", "c"]:
            credits()
        
        elif starting_choice == "help":
            helpsite()

if __name__=="__main__":
    start(title=variables.title)
