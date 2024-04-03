import ctypes
import os
import shutil
import zipfile
import requests

def set_terminal_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

if __name__ == "__main__":
    set_terminal_title("Split It! version 0.8")

def start():

    print(" ________       ________    ___           ___      _________                ___      _________    ___")
    print("|\\   ____\\     |\\   __  \\  |\\  \\         |\\  \\    |\\___   ___\\             |\\  \\    |\\___   ___\\ |\\  \\")
    print("\\ \\  \\___|_    \\ \\  \\|\\  \\ \\ \\  \\        \\ \\  \\   \\|___ \\  \\_|             \\ \\  \\   \\|___ \\  \\_| \\ \\  \\")
    print(" \\ \\_____  \\    \\ \\   ____\\ \\ \\  \\        \\ \\  \\       \\ \\  \\               \\ \\  \\       \\ \\  \\   \\ \\  \\")
    print("  \\|____|\\  \\    \\ \\  \\___|  \\ \\  \\____    \\ \\  \\       \\ \\  \\               \\ \\  \\       \\ \\  \\   \\ \\__\\")
    print("    ____\\_\\  \\    \\ \\__\\      \\ \\_______\\   \\ \\__\\       \\ \\__\\               \\ \\__\\       \\ \\__\\   \\|__|")
    print("   |\\_________\\    \\|__|       \\|_______|    \\|__|        \\|__|                \\|__|        \\|__|       ___ ")
    print("   \\|_________|                                                                                        |\\__\\")
    print("                                                                                                       \\|__")
    print("")
    print("    _                           _                              _                    _         _    _")
    print("   / \\         ___  _   _  ___ | |_  ___   _ __ ___       ___ (_) _ __ ___   _   _ | |  __ _ | |_ (_)  ___   _ __")
    print("  / _ \\       / __|| | | |/ __|| __|/ _ \\ | '_ ` _ \\     / __|| || '_ ` _ \\ | | | || | / _` || __|| | / _ \\ | '_ \\")
    print(" / ___ \\     | (__ | |_| |\\__ \\| |_| (_) || | | | | |    \\__ \\| || | | | | || |_| || || (_| || |_ | || (_) || | | |")
    print("/_/   \\_\\     \\___| \\__,_||___/ \\__|\\___/ |_| |_| |_|    |___/|_||_| |_| |_| \\__,_||_| \\__,_| \\__||_| \\___/ |_| |_|")
    print("                   _                            _  _  _    _                    __                   ____   _                        ___  _        _")
    print("  ___  __ _   ___ | |__    ___      ___  _ __  | |(_)| |_ | |_  ___  _ __      / _|  ___   _ __     / ___| | |__    ___   ___  _ __ |_ _|| |_     | |")
    print(" / __|/ _` | / __|| '_ \\  / _ \\    / __|| '_ \\ | || || __|| __|/ _ \\| '__|    | |_  / _ \\ | '__|    \\___ \\ | '_ \\  / _ \\ / _ \\| '_ \\ | | | __|    | |")
    print("| (__| (_| || (__ | | | ||  __/    \\__ \\| |_) || || || |_ | |_|  __/| |       |  _|| (_) || |        ___) || | | ||  __/|  __/| |_) || | | |_     |_|")
    print(" \\___|\\__,_| \\___||_| |_| \\___|    |___/| .__/ |_||_| \\__| \\__|\\___||_|       |_|   \\___/ |_|       |____/ |_| |_| \\___| \\___|| .__/|___| \\__|    (_)")
    print("                                        |_|                                                                                   |_|")
    print("")
    print("")
    print(" __  __               _            ____")
    print("|  \\/  |   __ _    __| |   ___    | __ )   _   _")
    print("| |\\/| |  / _` |  / _` |  / _ \\   |  _ \\  | | | |")
    print("| |  | | | (_| | | (_| | |  __/   | |_) | | |_| |")
    print("|_|  |_|  \\__,_|  \\__,_|  \\___|   |____/   \\__, |")
    print("                                           |___/")
    print(" ___   _   _    ____   _____   _   _      _      ____    _____   _")
    print("|_ _| | \\ | |  / ___| | ____| | \\ | |    / \\    |  _ \\  | ____| | |")
    print(" | |  |  \\| | | |  _  |  _|   |  \\| |   / _ \\   | |_) | |  _|   | |")
    print(" | |  | |\\  | | |_| | | |___  | |\\  |  / ___ \\  |  _ <  | |___  | |___")
    print("|___| |_| \\_|  \\____| |_____| |_| \\_| /_/   \\_\\ |_| \\_\\ |_____| |_____|")
    print("")
    print("")
    print("________________________________________________________________________________________________________________________________________________")
    print("|:‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾:|")
    print("|:   Wanna support me?                                                                                                                        :|")
    print("|:                                                                                                                                            :|")
    print("|:   SUPPORT THE SHEEPIT DEVS!!!! -                                                 https://www.sheepit-renderfarm.com/donation               :|")
    print("|:                                                                                                                                            :|")
    print("|:   Follow me on Instagram -                                                       https://www.instagram.com/saad_abdullah999666/            :|")
    print("|:   Reddit account -                                                               https://reddit.com/user/INGENAREL                         :|")
    print("|:   Discord -                                                                      ingenarel#2846                                            :|")
    print("|:   My youtube channel -                                                           https://www.youtube.com/channel/UC90Tar8Bpx3Q8UqpM8qxWZw  :|")
    print("|:   Sponsor me on SheepIt -                                                        https://www.sheepit-renderfarm.com/user/ingenarel/profile :|")
    print("|:   Here's my public renderkey if you wanna connect a device to my account -       XQVDMUjdOKt7LBldxjuF0YERqLoGnExbeh8yUrce                  :|")
    print("|:                                                                                                                                            :|")
    print("|:____________________________________________________________________________________________________________________________________________:|")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print("")
    print("________________________________________________________________________________________________________________________________________________________________________________")
    print("|:‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾:|")
    print("|: ██████╗ ██╗███████╗ ██████╗██╗      █████╗ ██╗███╗   ███╗███████╗██████╗ ██╗██╗██╗                                                                                         :|")
    print("|: ██╔══██╗██║██╔════╝██╔════╝██║     ██╔══██╗██║████╗ ████║██╔════╝██╔══██╗██║██║██║                                                                                         :|")
    print("|: ██║  ██║██║███████╗██║     ██║     ███████║██║██╔████╔██║█████╗  ██████╔╝██║██║██║                                                                                         :|")
    print("|: ██║  ██║██║╚════██║██║     ██║     ██╔══██║██║██║╚██╔╝██║██╔══╝  ██╔══██╗╚═╝╚═╝╚═╝                                                                                         :|")
    print("|: ██████╔╝██║███████║╚██████╗███████╗██║  ██║██║██║ ╚═╝ ██║███████╗██║  ██║██╗██╗██╗                                                                                         :|")
    print("|: ╚═════╝ ╚═╝╚══════╝ ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝╚═╝                                                                                         :|")
    print("|:                                                                                                                                                                            :|")
    print("|: THIS IS JUST A TEST PROJECT! I'M JUST AN AMATEUR PROGRAMMER! I LEARNED TO CODE THIS WHILE I WAS ALSO CODING IT SO THERE MAY BE STILL SOME BUGS LEFT!!!                     :|")
    print("|: THIS WILL ONLY WORK FOR FLUID CACHES ONLY! (As far as I know.. Haven't tested with others yet....)                                                                         :|")
    print("|: This is because I only know how fluid cache files works and i haven't really worked it other simulations yet such as smoke and fire, particle systems...                   :|")
    print("|: I'll eventually learn them too and then i'll try to upgrade it!                                                                                                            :|")
    print("|: I'll also try to make a smart cache splitter where it will split the files based on their sizes.                                                                           :|")
    print("|: But for now you will have to set how many splits you want to make.                                                                                                         :|")
    print("|: If you have any suggestions and you know how to do it, I'll appreciate the help!                                                                                           :|")
    print("|: I'm just a member of the SheepIt community i'm not a dev so if i make any errors it's my fault not theirs!                                                                 :|")
    print("|: I'll also try to post this on github and make it open source too altho i'm kinda a noob at that too. :(                                                                    :|")
    print("|:                                                                                                                                                                            :|")
    print("|:____________________________________________________________________________________________________________________________________________________________________________:|")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print("")
    print("BEFORE YOU START THIS MAKE SURE THAT YOU HAVE DOUBLE THE EMPTY SPACE IN YOUR DRIVE AS YOUR BLEND AND CACHE FILE COMBINED!")
    print("THAT MEANS IF YOUR BLEND FILE IS 100 mb AND YOUR SIMULATION CACHE FOLDER IS 900 mb, MAKE SURE THAT YOU HAVE ATLEAST 2 gb OF EMPTY SPACE IN YOUR DRIVE! ")

def please_enter_your_simulation_folder_name():

    print(" ____   _                                        _")
    print("|  _ \\ | |  ___   __ _  ___   ___    ___  _ __  | |_  ___  _ __   _   _   ___   _   _  _ __")
    print("| |_) || | / _ \\ / _` |/ __| / _ \\  / _ \\| '_ \\ | __|/ _ \\| '__| | | | | / _ \\ | | | || '__|")
    print("|  __/ | ||  __/| (_| |\\__ \\|  __/ |  __/| | | || |_|  __/| |    | |_| || (_) || |_| || |")
    print("|_|    |_| \\___| \\__,_||___/ \\___|  \\___||_| |_| \\__|\\___||_|     \\__, | \\___/  \\__,_||_|")
    print("      _                    _         _    _                  __   |___/ _      _")
    print(" ___ (_) _ __ ___   _   _ | |  __ _ | |_ (_)  ___   _ __    / _|  ___  | |  __| |  ___  _ __   _ __    __ _  _ __ ___    ___")
    print("/ __|| || '_ ` _ \\ | | | || | / _` || __|| | / _ \\ | '_ \\  | |_  / _ \\ | | / _` | / _ \\| '__| | '_ \\  / _` || '_ ` _ \\  / _ \\")
    print("\\__ \\| || | | | | || |_| || || (_| || |_ | || (_) || | | | |  _|| (_) || || (_| ||  __/| |    | | | || (_| || | | | | ||  __/")
    print("|___/|_||_| |_| |_| \\__,_||_| \\__,_| \\__||_| \\___/ |_| |_| |_|   \\___/ |_| \\__,_| \\___||_|    |_| |_| \\__,_||_| |_| |_| \\___|")
       
def success_msg():
    print(" ____    _   _    ____    ____   _____   ____    ____    _   _   _ ")
    print("/ ___|  | | | |  / ___|  / ___| | ____| / ___|  / ___|  | | | | | |")
    print("\\___ \\  | | | | | |     | |     |  _|   \\___ \\  \\___ \\  | | | | | |")
    print(" ___) | | |_| | | |___  | |___  | |___   ___) |  ___) | |_| |_| |_|")
    print("|____/   \\___/   \\____|  \\____| |_____| |____/  |____/  (_) (_) (_)")

def error_msg():
    print("        vXFAAAAAAAAAAAAAAAAAAAAAAAAAAOR2r")
    print("   p6HAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABCBBBBZy")
    print("         hYDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPw")
    print("               VAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA3")
    print("               fAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7")
    print("                RAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAL")
    print("                dAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAV")
    print("                PAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")                 
    print("               sAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA3")                
    print("               kAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK                 _   _           __  _  _                        __         _      _")
    print("                mVVXYZZ36777987ZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv               | \\ | |  ___    / _|(_)| |  ___    ___   _ __   / _|  ___  | |  __| |  ___  _ __")
    print("                                  fRAAAAAAAAAAAAAAAAAAAAXv          wbMAAAAAAAAAAAAAA8              |  \\| | / _ \\  | |_ | || | / _ \\  / _ \\ | '__| | |_  / _ \\ | | / _` | / _ \\| '__|")
    print("                                     sAAAAAAAAAD0z      tmmz            8AAAAAAAAAAAAA5             | |\\  || (_) | |  _|| || ||  __/ | (_) || |    |  _|| (_) || || (_| ||  __/| |")
    print("                                       kAAAAAAi        AAAAV      p     BAAAAAAAAAAAAAAh            |_| \\_| \\___/  |_|  |_||_| \\___|  \\___/ |_|    |_|   \\___/ |_| \\__,_| \\___||_|")
    print("                                        eAAAAAABe                   s7EAAAAAAAAAAAAAAAAAb             __                           _   _              _    _             _")
    print("          qCAAAAABX6ffbdkmjchiaht       gAAAAAAAAA     qe94567992AAAAAAAAAAAAAAAAAAAAAAAAh           / _|  ___   _   _  _ __    __| | | |__   _   _  | |_ | |__    __ _ | |_")
    print("            0AAAAAAAAAAAAAAAAAAA0       nAAAAAAAAAx   XAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA          | |_  / _ \\ | | | || '_ \\  / _` | | '_ \\ | | | | | __|| '_ \\  / _` || __|")
    print("               kcVKHAAAAAAAAAA2x         AAAAAAAAA9   hDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAV         |  _|| (_) || |_| || | | || (_| | | |_) || |_| | | |_ | | | || (_| || |_")
    print("                    kAAAAAAAAR           3AAAAAAAAX   t9UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA         |_|   \\___/  \\__,_||_| |_| \\__,_| |_.__/  \\__, |  \\__||_| |_| \\__,_| \\__|")
    print("                      6AAAAAZ            lAAAAAAAAA       FAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA                                                   |___/")
    print("                       8AAAZ             gAAAAAAAAAAf     fAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF                                              ____  _                  _")
    print("                                         AAAAAAAAAAAAAr    hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAo          _ __    __ _  _ __ ___    ___      / ___|| |__    ___   ___ | | __  _   _   ___   _   _  _ __")
    print("                                         TAAAAAAAAAAAAa     zAAAAAAAAAAAAAAAAAAAAAAAAAAAAA          | '_ \\  / _` || '_ ` _ \\  / _ \\    | |    | '_ \\  / _ \\ / __|| |/ / | | | | / _ \\ | | | || '__|")
    print("                                           kEAAAAAAAAO      ZAAAAAAAAAAAANkQAAAAAAAAAAAAAh          | | | || (_| || | | | | ||  __/ _  | |___ | | | ||  __/| (__ |   <  | |_| || (_) || |_| || |   ")
    print("                                              wh6WRF3     oNAAAAAAAAAAAAA9   4AAAAAAAAAAE           |_| |_| \\__,_||_| |_| |_| \\___|(_)  \\____||_| |_| \\___| \\___||_|\\_\\  \\__, | \\___/  \\__,_||_|   ")
    print("                                                       vAAAAAAAAAAAAAAAAAA6   oAAAAAAAAE                               _  _  _                                      _    |___/                     ")
    print("                                                      BAAAAAAAAAAAAAAAAAAAAP    2AAAAAAy             ___  _ __    ___ | || |(_) _ __    __ _    __ _   __ _   __ _ (_) _ __                        ")
    print("                                            aAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa   AAAAA7             / __|| '_ \\  / _ \\| || || || '_ \\  / _` |  / _` | / _` | / _` || || '_ \\                       ")
    print("                                             8RRNAAAAAAAAAAAAAAAAAAAAAAAAAAAAA9   AAAE              \\__ \\| |_) ||  __/| || || || | | || (_| | | (_| || (_| || (_| || || | | | _                    ")
    print("                                  kEAA7sy               s9221ZYXWKAAAAAAMUZ45d    AAAl              |___/| .__/  \\___||_||_||_||_| |_| \\__, |  \\__,_| \\__, | \\__,_||_||_| |_|(_)                   ")
    print("                                 pGAAAAAAAAAAAAGeoz                          qu   AAp                    |_|                           |___/          |___/                                        ")
    print("                                   vUAAAAAAAAAAAAAAAAAAAAAWefgeeeffffffg5AAAAAAAeHAH")                
    print("                                     2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg")                
    print("                                     XAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")                 
    print("                                    cDAAAAAOUHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD")
    print("                                    5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAz")
    print("                                     WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    print("                                    ZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7")
    print("                                    LAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    print("                                    XAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD")
    print("                                     aAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAr")
    print("                                    vTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAd")
    print("                                      cAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    print("                                         oBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAX")
    print("                                           u7CAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAY")
    print("                                               mfKAAAAAAAAAAAAAAAAAAAAAAAAARw")
    print("                                                   tkeLAAAAAAAAAAAAAAABXw")

def end():
    print("Your splitting is finished. yayyyyyyy!!!!!")
    print("")
    print("++++++++++++++++**++*%#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++@*#+###+%*#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++*%*+@+@#*#*%+**+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++*#*#@**#++#++@++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#@++#@++++++++")
    print("+++++++++++++*#**++++++++@%##++++++++++++++++++++++++++++++++++++++++++++++++++++++++#**#+##++##++++")
    print("++++++++++++++@+++*****+*#+*#+++++++++++++++++++++++++++++++++++++++++++++++++++++**+@*+#@*@*%*%++++")
    print("++++++++++++++@+++****%**++@+++++++++++++++++++++++++++++++++++++++++++++++++++++***#%++++*##+#+++++")
    print("++++++++++++++%#******+*++%++++++++++++++++++++++++++++++++++++++++++++++++++++++**+#*+*+++++#*%#%%+")
    print("+++++++++++++##+++++++++*#%*+++++++++++++++++++++++++++++++++++++++++++++++++++++**++*******+***%*++")
    print("+++++++++++++#++++++++++***#*++++++++++++++++++++++++++++++++++++++++++++++++++++*#+++*#***+++**++++")
    print("++++++++++++##+*#%%%%%%%%#*#*+++++++++++++++++++++++++++++++++++++++++++++++++++##%##***+*+++*#+++++")
    print("++++++++++++@@@@%%%###%%%%@@#+++++++++++++++++++++++++++++++++++++++++++++++++#*+++++++*###+#%++++++")
    print("++++++++++++@%*++++++++****#%++++++++++++++++++++++++++++++++++++++++++++++++**++++++++++++##+++++++")
    print("+++++++++++##+#%###***##%%%#@+++++++++++++++++++++++++++++++++++++++++++++++%*++++++++++++***%++++++")
    print("+++++++++++*%#*********###%@*+++*#%##***+++++++***##%%%%**++++++++++++++++*@@@@@@@@@@%#*****#%++++++")
    print("++++++++++++%**********###%@*%%#+++++++++++*#+*+++++++++*#%@%*++++++++++++@*+****++**%@@@%#*%+++++++")
    print("++++++++++++#**********##%%#*++++++*++++++#*#+#+++++*++++++++*#%#+++++++++%*######%%%#**#%@@#+++++++")
    print("+++++++++++#**********#%#+++++++++*+++++*#**#+#+++++*+++++++++++*#%#+++++++#%##########%%*#@++++++++")
    print("+++++++++++#********#%#++++*++*++#+++++*#***#+#+++++**+++++++*++**+*%%+++++%*******######@##++++++++")
    print("++++++++++##*******%%+++++*++**+*+++++*#***+*+#+++++**+++++++*+++***++#%+*%***********##%@%+++++++++")
    print("++++++++++@#*****#%*+++++**+*%**#*****#***++**%++++++#+++++++*++++**+++*%%#************#%+++++++++++")
    print("+++++++++*%*****##+++++++#**%#*%*****#***+++*#%#*****%**+++++**++++**+++*%************#@++++++++++++")
    print("+++++++++##****%*+++*+**#**#%*#%#%%%%**++++++##%***##%@%******#+++++#*++%*************%*++++++++++++")
    print("+++++++++%***#%++*******@**%##@****%**+++++++*#%******##**#***%******#+##************#%+++++++++++++")
    print("+++++++++#**##++*******##**##*%***##*++++++++++*******%#******#******##%*************%*+++++++++++++")
    print("++++++++##*#*+*****#**#*#*#***#+**#*+++++++++++++++*#***%******%*****#%**********#**##++++++++++++++")
    print("++++++++@%#+******#***#*++++***#*##*+++++++++++++*##***********%#****##*************#+++++++++++++++")
    print("++++++*#*+*#**#***#**#**++**##%%%%***+++++++++++**##%%%%%%%###**%****#*************##+++++++++++++++")
    print("++*%@*+**%##*********#**#%%%#****#%@*+++++++++++*%%#******#%@%***#**##*************%++++++++++++++++")
    print("++++***##*%*+#*******#%%%*++++**++++++++++++++++++++#%%%%%#+*%@%+*###*************##++++++++++++++++")
    print("+++++++%##@**%***#*+%%%*+++*#%%%%%*++++++++++++++++++*%%%%%%++#@%+*%#************#%+++++++++++++++++")
    print("+++++++%**%**#**+#**%%*+++++*%%%%%%*+++++++++++++*%###%@%%%@#++#@###*************##+++++++++++++++++")
    print("+++++++%*****#***##*@#++*@@%*****%@#+++++++++++++%#+++++**@@%++*@%%**************@*+++++++++++++++++")
    print("+++++++%*******##****+++#@*+++++++#*+++++++++++++%++++*+++*%*+++*%#*************##++++++++++++++++++")
    print("+++++++#*******##**#*+++*%*++++++**++++++++++++++*%*++++++#*+++*#%***********#**%@++++++++++++++++++")
    print("++++++*%******###*+*++++*+#*****++++++++++++++++++++****#*++++*#%##*******#######@*+++++++++++++++++")
    print("++++++*%*****#%*#*++*++*++*+++++++++++++++++++++++++++++++++**#*%********######@*@++++++++++++++++++")
    print("++++++*#*****#**#*++*++****++++++++++++++++++++++++++++++*+**#+%#******#########*%#+++++++++++++++++")
    print("++++++*%*****#+***++++++**++++++++++++++******++++++++++++++%*#%*******#######%**##+++++++++++++++++")
    print("++++++*%****%*++**++++++++++++++++*#%##*********#*++++++*++*#*@#******#########**##+++++++++++++++++")
    print("++++++*%***##++*%+++++++++++++++++####**********#*++++++++*#+#%*******#######%***##+++++++++++++++++")
    print("+++++++#***#+++*%+++++++++++++++++*#************#*++++++++%*+##*******######%#****%+++++++++++++++++")
    print("+++++++%***#+++*##+++++++++++++++++%************#++++++++##+*##*******######%*****%+++++++++++++++++")
    print("+++++++%#*#*+++**%*+++++++++++++++++***********#+++++++++#+*%#*********####%#+****%+++++++++++++++++")
    print("+++++++#%##+++****%%+++++++++++++++++*********#*++++++++#*+*@#*********####%*+++++%+++++++++++++++++")
    print("+++++++*@#*+++*****#@#*+++++++++++++++++++++*++++++++++*%+*##**********####%+++++*%+++++++++++++++++")
    print("++++++++@%+++****##%##%%#++++++++++++++++++++++++++++++#*+*##**********###%%*+++++##++++++++++++++++")
    print("++++++++*%+++****#%####%*#%#*++++++++++++++++++++++++*##+**#***********##%%#*+++++*@++++++++++++++++")
    print("+++++++++*+++***#######%#+%@**#%%%**++++++++++++**#%%#%****#***********##%%#*++++**@++++++++++++++++")
    print("++++++++**++****#%########*@#+******#**#%********#@#**@*+**#***********##%%*#++++++%#+++++++++++++++")
    print("++++++++@*++****%%#####**#*#@*++****####%********%***##+**##***********#%#*##*+++++*%+++++++++++++++")
    print("++++++++@*++****@#####****%+%@*+++**##**********#**++#*+**#*************%**#*#++++++%*++++++++++++++")
    print("++++++++@++*#**#%####******%*%@*++++*%#******##%*+++*%++**%************##***##*+++++*@++++++++++++++")
    print("++++++++@++****#%###*******##*%@*++++*#+****++#*+++*@#++**%************%*#**###++++++##+++++++++++++")
    print("++++++++@++****#%##**********###@#++++#*+++++##+++#@%#++*##***********#%*#***##%++++++%+++++++++++++")
    print("")
    print("")
    print("Please check your zip files before you upload your project. Because")
    print("I'm dumb")
    print("and")
    print("even if something works for someone it might not work for others.")
    print("I hope you have a great life")

start()
please_enter_your_simulation_folder_name()


# take the fucking folder names
while True:

    print("You can your 'ver' or 'version' to check for the latest build.")
    print("You can type cls or clear to clear the screen")
    print("Type s to start.")
    
    starting_choice = input("What do you want to do? ")


    if starting_choice == 's':

        while True:

            folder_name = input("Enter folder name (CASE SENSITIVE): ")

            # Get the list of folders in the current directory
            folders = [folder for folder in os.listdir('.') if os.path.isdir(folder)]

            if folder_name in folders:

            # if the fucking job is done this does the splits
                
                while True:
                    file_count = input("Enter the number of files to copy into each folder (numerical values only): ")

                    if file_count.isdigit():
                        file_count = int(file_count)

                        #config files splitter####################################################################################################################################################################################################################################################

                        source_folder = os.path.join(folder_name, "config")
                        destination_base_folder = "Destination"

                        print("Please wait while I split the Config files...")

                        count = 0
                        folder_count = 1

                        os.makedirs(os.path.join(destination_base_folder, str(folder_count), folder_name, "config"), exist_ok=True)

                        for filename in os.listdir(source_folder):
                            source_file = os.path.join(source_folder, filename)

                            # Copy files to the current destination folder
                            shutil.copy(source_file, os.path.join(destination_base_folder, str(folder_count), folder_name, "config"))

                            count += 1

                            # If specified number of files are copied, reset the file counter and move to the next destination folder
                            if count == file_count:
                                count = 0
                                folder_count += 1
                                os.makedirs(os.path.join(destination_base_folder, str(folder_count), folder_name, "config"), exist_ok=True)

                        print("Config files copy pasted successfully.")

                        #data files splitter####################################################################################################################################################################################################################################################

                        source_folder = os.path.join(folder_name, "data")
                        destination_base_folder = "Destination"

                        print("Please wait while I split the Data files...>.<")

                        count = 0
                        folder_count = 1

                        os.makedirs(os.path.join(destination_base_folder, str(folder_count), folder_name, "data"), exist_ok=True)

                        for filename in os.listdir(source_folder):
                            source_file = os.path.join(source_folder, filename)

                            # Copy files to the current destination folder
                            shutil.copy(source_file, os.path.join(destination_base_folder, str(folder_count), folder_name, "data"))

                            count += 1

                            # If specified number of files are copied, reset the file counter and move to the next destination folder
                            if count == file_count:
                                count = 0
                                folder_count += 1
                                os.makedirs(os.path.join(destination_base_folder, str(folder_count), folder_name, "data"), exist_ok=True)

                        print("Data files copy pasted successfully.")

                        #mesh files splitter####################################################################################################################################################################################################################################################

                        source_folder = os.path.join(folder_name, "mesh")
                        destination_base_folder = "Destination"

                        print("Please wait while I split the Mesh files...>.<")

                        count = 0
                        folder_count = 1

                        os.makedirs(os.path.join(destination_base_folder, str(folder_count), folder_name, "mesh"), exist_ok=True)

                        for filename in os.listdir(source_folder):
                            source_file = os.path.join(source_folder, filename)

                            # Copy files to the current destination folder
                            shutil.copy(source_file, os.path.join(destination_base_folder, str(folder_count), folder_name, "mesh"))

                            count += 1

                            # If specified number of files are copied, reset the file counter and move to the next destination folder
                            if count == file_count:
                                count = 0
                                folder_count += 1
                                os.makedirs(os.path.join(destination_base_folder, str(folder_count), folder_name, "mesh"), exist_ok=True)

                        print("Mesh files copy pasted successfully...>.<")

                        #guiding config####################################################################################################################################################################################################################################################

                        while True:
                            guiding_folder = input("Do you have a guiding folder? Enter 'y' for yes, 'n' for no: ")
                            
                            if guiding_folder == "y":
                                
                                guiding_split = input("Do you want to split it? If it has files then you should. Enter 'y' for yes, 'n' for no: ")
                                
                                if guiding_split == "y":
                                
                                    # Guiding files splitter

                                    source_folder = os.path.join(folder_name, "guiding")
                                    destination_base_folder = "Destination"

                                    print("Please wait while I split the Guiding files...>.<")

                                    count = 0
                                    folder_count = 1

                                    os.makedirs(os.path.join(destination_base_folder, str(folder_count), folder_name, "guiding"), exist_ok=True)

                                    for filename in os.listdir(source_folder):
                                        source_file = os.path.join(source_folder, filename)

                                        # Copy files to the current destination folder
                                        shutil.copy(source_file, os.path.join(destination_base_folder, str(folder_count), folder_name, "guiding"))

                                        count += 1

                                        # If specified number of files are copied, reset the file counter and move to the next destination folder
                                        if count == file_count:
                                            count = 0
                                            folder_count += 1
                                            os.makedirs(os.path.join(destination_base_folder, str(folder_count), folder_name, "guiding"), exist_ok=True)

                                    print("Guiding files copy pasted successfully...>.<")

                                    break
                                
                                elif guiding_split == "n":
                                    # Guiding folders creator
                                
                                    destination_root = "Destination"

                                    print("Please wait while i copy the guiding folders... >.<")

                                    for subfolder in os.listdir(destination_root):
                                        destination_folder = os.path.join(destination_root, subfolder, folder_name)
                                        source_folder = os.path.join(folder_name, "guiding")
                                        
                                        # Check if the source guiding folder exists
                                        if os.path.exists(source_folder):
                                            # Create destination folder if it doesn't exist
                                            os.makedirs(destination_folder, exist_ok=True)
                                            # Copy the entire guiding folder and its contents
                                            shutil.copytree(source_folder, os.path.join(destination_folder, "guiding"))

                                    print("Guiding folders copy pasted successfully.")

                                    break

                                elif guiding_split.lower() in ["cls", "clear"]:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    continue

                                #guiding folder split yn error
                                else:
                                    print("Error. Please use either 'y' or 'n'")
                                    continue
                            
                            #no guiding folders
                            elif guiding_folder == "n":
                                break

                            elif guiding_folder.lower() in ["cls", "clear"]:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                continue
                            
                            #guiding folder yn error
                            else:
                                print("Error. Please use either 'y' or 'n'")
                                continue

                        #noise config####################################################################################################################################################################################################################################################

                        while True:
                            noise_folder = input("Do you have a noise folder? Enter 'y' for yes, 'n' for no: ")
                            
                            if noise_folder == "y":
                                
                                noise_split = input("Do you want to split it? If it has files then you should. Enter 'y' for yes, 'n' for no: ")
                                
                                if noise_split == "y":
                                
                                    # noise files splitter

                                    source_folder = os.path.join(folder_name, "noise")
                                    destination_base_folder = "Destination"

                                    print("Please wait while I split the Noise files...>.<")

                                    count = 0
                                    folder_count = 1

                                    os.makedirs(os.path.join(destination_base_folder, str(folder_count), folder_name, "noise"), exist_ok=True)

                                    for filename in os.listdir(source_folder):
                                        source_file = os.path.join(source_folder, filename)

                                        # Copy files to the current destination folder
                                        shutil.copy(source_file, os.path.join(destination_base_folder, str(folder_count), folder_name, "noise"))

                                        count += 1

                                        # If specified number of files are copied, reset the file counter and move to the next destination folder
                                        if count == file_count:
                                            count = 0
                                            folder_count += 1
                                            os.makedirs(os.path.join(destination_base_folder, str(folder_count), folder_name, "noise"), exist_ok=True)

                                    print("Noise files copy pasted successfully...>.<")

                                    break
                                
                                elif noise_split == "n":
                                    # noise folders creator
                                
                                    destination_root = "Destination"

                                    print("Please wait while i copy the Noise folders... >.<")

                                    for subfolder in os.listdir(destination_root):
                                        destination_folder = os.path.join(destination_root, subfolder, folder_name)
                                        source_folder = os.path.join(folder_name, "noise")
                                        
                                        # Check if the source noise folder exists
                                        if os.path.exists(source_folder):
                                            # Create destination folder if it doesn't exist
                                            os.makedirs(destination_folder, exist_ok=True)
                                            # Copy the entire noise folder and its contents
                                            shutil.copytree(source_folder, os.path.join(destination_folder, "noise"))

                                    print("Noise folders copied successfully.")

                                    break

                                elif noise_split.lower() in ["cls", "clear"]:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    continue

                                #noise folder split yn error
                                else:
                                    print("Error. Please use either 'y' or 'n'")
                                    continue
                            
                            #no noise folder
                            elif noise_folder == "n":
                                break

                            elif noise_folder.lower() in ["cls", "clear"]:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                continue
                            
                            #noise folder yn error
                            else:
                                print("Error. Please use either 'y' or 'n'")
                                continue

                        #particles config####################################################################################################################################################################################################################################################

                        while True:
                            particles_folder = input("Do you have a particles folder? Enter 'y' for yes, 'n' for no: ")
                            
                            if particles_folder == "y":
                                
                                particles_split = input("Do you want to split it? If it has files then you should. Enter 'y' for yes, 'n' for no: ")
                                
                                if particles_split == "y":
                                
                                    # particles files splitter

                                    source_folder = os.path.join(folder_name, "particles")
                                    destination_base_folder = "Destination"

                                    print("Please wait while I split the Particles files...>.<")

                                    count = 0
                                    folder_count = 1

                                    os.makedirs(os.path.join(destination_base_folder, str(folder_count), folder_name, "particles"), exist_ok=True)

                                    for filename in os.listdir(source_folder):
                                        source_file = os.path.join(source_folder, filename)

                                        # Copy files to the current destination folder
                                        shutil.copy(source_file, os.path.join(destination_base_folder, str(folder_count), folder_name, "particles"))

                                        count += 1

                                        # If specified number of files are copied, reset the file counter and move to the next destination folder
                                        if count == file_count:
                                            count = 0
                                            folder_count += 1
                                            os.makedirs(os.path.join(destination_base_folder, str(folder_count), folder_name, "particles"), exist_ok=True)

                                    print("Particles files copy pasted successfully...>.<")

                                    break
                                
                                elif particles_split == "n":
                                    # particles folders creator
                                
                                    destination_root = "Destination"

                                    print("Please wait while i copy the Particles folders... >.<")

                                    for subfolder in os.listdir(destination_root):
                                        destination_folder = os.path.join(destination_root, subfolder, folder_name)
                                        source_folder = os.path.join(folder_name, "particles")
                                        
                                        # Check if the source particles folder exists
                                        if os.path.exists(source_folder):
                                            # Create destination folder if it doesn't exist
                                            os.makedirs(destination_folder, exist_ok=True)
                                            # Copy the entire particles folder and its contents
                                            shutil.copytree(source_folder, os.path.join(destination_folder, "particles"))

                                    print("Particles folders copy pasted successfully.")

                                    break

                                elif particles_split.lower() in ["cls", "clear"]:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    continue

                                #particles folder split yn error
                                else:
                                    print("Error. Please use either 'y' or 'n'")
                                    continue
                            
                            #no particles folder
                            elif particles_folder == "n":
                                break

                            elif particles_folder.lower() in ["cls", "clear"]:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                continue
                            
                            #particles folder yn error
                            else:
                                print("Error. Please use either 'y' or 'n'")
                                continue

                        #blend file copy paste####################################################################################################################################################################################################################################################

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

                        break
                        
                    elif file_count.lower() in ["cls", "clear"]:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue

                    else:
                        print("Please enter a valid integer value.")
                        continue



                break

            # clears your shit
            elif folder_name.lower() in ["cls", "clear"]:
                os.system('cls' if os.name == 'nt' else 'clear')
                continue


            # because people are dumb fucks
            else:
                error_msg()
                continue
            
            break
        # checks the version
    elif starting_choice.lower() in ["ver", "version"]:

            # Specify your GitHub username and repository name
            repo_owner = "ingenarel"
            repo_name = "Split-It"

            # Get local version of your tool (replace this with your logic)
            local_version = "v0.8"  # Example local version, replace with your own logic

            # Get latest release version from GitHub
            try:
                url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
                response = requests.get(url)
                if response.status_code == 200:
                    latest_release = response.json()
                    latest_version = latest_release.get('tag_name')

                else:
                    if response.status_code == 400:
                        print("ERROR 400 Bad request:")
                        print("")
                        print("This status code indicates that there's something off with the request you sent to the server.")
                        print("It's like filling out a form incorrectly or forgetting to provide essential details.")
                        print("The server couldn't understand or process your request due to missing or malformed data.")
                        print("")

                    elif response.status_code == 401:
                        print("ERROR 401 Unauthorized:")
                        print("")
                        print("This status code means you're not allowed to access the requested resource without proper authentication.")
                        print("It's like trying to enter a restricted area without showing your ID.")
                        print("You need to provide valid credentials, such as a username and password or an authentication token, to gain access.")
                        print("")

                    elif response.status_code == 403:
                        print("ERROR 403 Unauthorized:")
                        print("")
                        print("You're being denied access, plain and simple.")
                        print("Even with valid credentials, you're not allowed to access the resource because you lack the necessary permissions. ")
                        print("It's like trying to enter a building without the proper authorization or access card.")
                        print("You need to request permission from the appropriate authorities.")
                        print("")

                    elif response.status_code == 404:
                        print("ERROR 404 Unauthorized:")
                        print("")
                        print("This status code indicates that the server couldn't find the resource you requested.")
                        print("It's like looking for a book on a library shelf only to discover it's not there. ")
                        print("The resource may have been moved, deleted, or simply never existed. ")
                        print("Double-check the URL or try searching for the resource in a different location.")
                        print("")

                    elif response.status_code == 422:
                        print("ERROR 422 Unauthorized:")
                        print("")
                        print("Ah, it seems there's a problem with the data you provided. ")
                        print("This status code typically occurs when the server understands your request but can't process it due to invalid data. ")
                        print("It's like trying to fill out a form with incorrect or incomplete information. ")
                        print("Review the data you submitted and ensure it meets the server's requirements.")
                        print("")

                    elif response.status_code == 429:
                        print("ERROR 429 Unauthorized:")
                        print("")
                        print("Slow down there! You've been making too many requests to the server within a short period. ")
                        print("This status code indicates that you've hit a rate limit, and the server is asking you to ease up for a bit. ")
                        print("It's like trying to take too many slices of cake at once, and someone politely suggests you wait your turn.")
                        print("")

                    elif response.status_code == 500:
                        print("ERROR 500 Unauthorized:")
                        print("")
                        print("Uh-oh, something went wrong on the server's end, and it's not your fault. ")
                        print("This status code indicates an unexpected problem occurred while the server was trying to process your request. ")
                        print("It's like ordering food at a restaurant and having the kitchen catch fire. ")
                        print("The server is apologizing for the inconvenience and asking for your patience while they sort things out.")
                        print("")

                    elif response.status_code == 503:
                        print("ERROR 503 Unauthorized:")
                        print("")
                        print("Hold your horses! The server is currently unavailable to handle your request. ")
                        print("This status code typically occurs due to maintenance or overload. ")
                        print("It's like calling a store outside of business hours and getting a message saying they're closed for the day. ")
                        print("You'll need to try again later when the server is back up and running.")
                        print("")

                    else:
                        print("I Don't know what the fuck are you doing but I can't find an error code for you.")
                        print("")
                        
                    input("press enter to go back to simulation folder select")
                    continue

            except requests.exceptions.RequestException as e:
                print("Failed to retrieve the latest version from GitHub.")
                print("Please check your internet connection and try again.")
                continue

            # Check if latest version is available and prompt user to download
            if latest_version:
                print(f"Current version: {local_version}")
                print(f"Latest version: {latest_version}")
                
                if local_version == latest_version:
                    print("You are already using the latest version.")
                    input("press enter to go back to simulation folder select")

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

                                    else:
                                        print(f"Failed to download: {asset.get('name')}")
                                        input("press enter to go back to simulation folder select")
                                        break

                                print(f"All assets from the latest release have been downloaded to '{download_folder}'.")
                                input("press enter to go back to simulation folder select")
                                break

                            else:
                                print("No assets found in the latest release.")
                                input("press enter to go back to simulation folder select")
                                break
                        elif choice.lower() == "n":
                            print("Skipping download.")
                            input("press enter to go back to simulation folder select")
                            break

                        elif choice.lower() in ["cls", "clear"]:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            continue

                        else:
                            print("Invalid choice. Please enter 'yes' or 'no'.")
                            continue
            else:
                print("Failed to retrieve the latest version from GitHub. Please check your internet connection and try again.")
                input("press enter to go back to simulation folder select")

            continue

#THIS IS THE ZIPPER AND I FUCKING HAD TO PUT IT HERE BECAUSE IT WASN'T FUCKING WORKING AND NOW I'M TESTING IT I JUST WANT TO FUCKING KILL MYSELF FUCK

print("Please wait while I zip the files... >.<")

# Set the path to the destination folder
destination_folder = "Destination"

# Change directory to the destination folder
os.chdir(destination_folder)

# Loop through each folder in the destination folder
for folder_name in os.listdir():
    if os.path.isdir(folder_name):
        # Create a zip file with the same name as the folder
        with zipfile.ZipFile(f"{folder_name}.zip", "w") as zip_file:
            # Add all files and empty folders in the folder to the zip file
            for root, dirs, files in os.walk(folder_name):
                # Add files
                for file in files:
                    zip_file.write(os.path.join(root, file),
                                os.path.relpath(os.path.join(root, file),
                                                os.path.join(folder_name)))
                # Add empty directories
                for dir in dirs:
                    dir_path = os.path.relpath(os.path.join(root, dir),
                                            os.path.join(folder_name))
                    zip_file.write(os.path.join(root, dir), dir_path)

print("All folders zipped successfully.")

###############folder deleter###############################################################################################################################################################################################

folder = "Destination"

# Navigate to the Destination folder
os.chdir(os.path.join(os.path.dirname(__file__), folder))

# Prompt the user for confirmation
while True:
    print("Do you want to delete the folders that were created when you split the project?")
    print("The zip files won't be deleted, just the folders and files that were created in order to make those zips.")
    choice = input("y to delete and n to cancel: ").strip().lower()
    
    # Check the user's choice
    if choice == 'y':
        # Loop through all items in the folder and delete them
        for item in os.listdir():
            if os.path.isdir(item):
                os.system(f"rd /s /q \"{item}\"")
        print("\nAll split cache folders deleted successfully.\nDon't worry, the zips aren't deleted.")
        break
    elif choice == 'n':
        print("Operation cancelled. No folders have been deleted.")
        break

    elif choice.lower() in ["cls", "clear"]:
        os.system('cls' if os.name == 'nt' else 'clear')

    else:
        print("Error. Please use either 'y' or 'n'")

end()

input("Press Enter to exit.")


# i wanna kill myself... i'm seriously struggling with my personal shit rn. if i don't update this anymore then you know what happened. and i'm sorry for it.
