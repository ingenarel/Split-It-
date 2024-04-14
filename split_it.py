#Importing Modules
import ctypes, os, shutil, zipfile, requests, pyautogui, platform, json
from tqdm import tqdm
from tkinter import *
from tkinter import filedialog
from threading import Thread
from multiprocessing import Process, freeze_support

#The Software startup and telling what is needed.
def start(**kwargs):
    ctypes.windll.kernel32.SetConsoleTitleW(kwargs["title"])
    print("")
    print("________       ________    ___           ___      _________                ___      _________    ___")
    print("|\\   ____\\     |\\   __  \\  |\\  \\         |\\  \\    |\\___   ___\\             |\\  \\    |\\___   ___\\ |\\  \\")
    print("\\ \\  \\___|_    \\ \\  \\|\\  \\ \\ \\  \\        \\ \\  \\   \\|___ \\  \\_|             \\ \\  \\   \\|___ \\  \\_| \\ \\  \\")
    print(" \\ \\_____  \\    \\ \\   ____\\ \\ \\  \\        \\ \\  \\       \\ \\  \\               \\ \\  \\       \\ \\  \\   \\ \\  \\")
    print("  \\|____|\\  \\    \\ \\  \\___|  \\ \\  \\____    \\ \\  \\       \\ \\  \\               \\ \\  \\       \\ \\  \\   \\ \\__\\")
    print("    ____\\_\\  \\    \\ \\__\\      \\ \\_______\\   \\ \\__\\       \\ \\__\\               \\ \\__\\       \\ \\__\\   \\|__|")
    print("   |\\_________\\    \\|__|       \\|_______|    \\|__|        \\|__|                \\|__|        \\|__|       ___")
    print("   \\|_________|                                                                                        |\\__\\")
    print("                                                                                                       \\|__|")
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
    print("________________________________________________________________________________________________________________________________________________________________________________")
    print("|:‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾:|")
    print("|: ██████╗ ██╗███████╗ ██████╗██╗      █████╗ ██╗███╗   ███╗███████╗██████╗ ██╗██╗██╗                                                                                         :|")
    print("|: ██╔══██╗██║██╔════╝██╔════╝██║     ██╔══██╗██║████╗ ████║██╔════╝██╔══██╗██║██║██║                                                                                         :|")
    print("|: ██║  ██║██║███████╗██║     ██║     ███████║██║██╔████╔██║█████╗  ██████╔╝██║██║██║                                                                                         :|")
    print("|: ██║  ██║██║╚════██║██║     ██║     ██╔══██║██║██║╚██╔╝██║██╔══╝  ██╔══██╗╚═╝╚═╝╚═╝                                                                                         :|")
    print("|: ██████╔╝██║███████║╚██████╗███████╗██║  ██║██║██║ ╚═╝ ██║███████╗██║  ██║██╗██╗██╗                                                                                         :|")
    print("|: ╚═════╝ ╚═╝╚══════╝ ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝╚═╝                                                                                         :|")
    print("|:                                                                                                                                                                            :|")
    print("|: THIS IS JUST A TEST PROJECT! SO THERE MAY BE STILL SOME BUGS LEFT!!!                                                                                                       :|")
    print("|: THIS WILL ONLY WORK FOR FLUID CACHES ONLY! (As far as I know.. Haven't tested with others yet....)                                                                         :|")
    print("|: This is because I only know how fluid cache files works and i haven't really worked it other simulations yet such as smoke and fire, particle systems...                   :|")
    print("|: I'll eventually learn them too and then i'll try to upgrade it!                                                                                                            :|")
    print("|: I'll also try to make a smart cache splitter where it will split the files based on their sizes.                                                                           :|")
    print("|: But for now you will have to set how many splits you want to make.                                                                                                         :|")
    print("|: If you have any suggestions and you know how to do it, I'll appreciate the help!                                                                                           :|")
    print("|: I'm just a member of the SheepIt community i'm not a dev so if i make any errors it's my fault not theirs!                                                                 :|")
    print("|:                                                                                                                                                                            :|")
    print("|:____________________________________________________________________________________________________________________________________________________________________________:|")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print("")
    print("For the best visual experience, please Maximise the Terminal/Command Prompt.")
    print("")
    print("BEFORE YOU START THIS MAKE SURE THAT YOU HAVE DOUBLE THE EMPTY SPACE IN YOUR DRIVE AS YOUR BLEND AND CACHE FILE COMBINED!")
    print("THAT MEANS IF YOUR BLEND FILE IS 100 mb AND YOUR SIMULATION CACHE FOLDER IS 900 mb, MAKE SURE THAT YOU HAVE ATLEAST 2 gb OF EMPTY SPACE IN YOUR DRIVE!")
    print("")

    please_enter_your_simulation_folder_name()
    return

#Printing the "please enter your Simulation folder name" text
def please_enter_your_simulation_folder_name():
    print("")
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
    print("")
    
    main_func()
    return

#Successfuly splitted it.
def success_msg():
    print("")
    print(" ____    _   _    ____    ____   _____   ____    ____    _   _   _ ")
    print("/ ___|  | | | |  / ___|  / ___| | ____| / ___|  / ___|  | | | | | |")
    print("\\___ \\  | | | | | |     | |     |  _|   \\___ \\  \\___ \\  | | | | | |")
    print(" ___) | | |_| | | |___  | |___  | |___   ___) |  ___) | |_| |_| |_|")
    print("|____/   \\___/   \\____|  \\____| |_____| |____/  |____/  (_) (_) (_)")
    print("")
    
    return

#Something went wrong while splitting.
def error_msg():
    print("")
    print("                vXFAAAAAAAAAAAAAAAAAAAAAAAAAAOR2r")
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
    print("                                              wh6WRF3     oNAAAAAAAAAAAAA9   4AAAAAAAAAAE           |_| |_| \\__,_||_| |_| |_| \\___|(_)  \\____||_| |_| \\___| \\___||_|\\_\\  \\__, | \\___/  \\__,_||_|")
    print("                                                       vAAAAAAAAAAAAAAAAAA6   oAAAAAAAAE                               _  _  _                                      _    |___/")
    print("                                                      BAAAAAAAAAAAAAAAAAAAAP    2AAAAAAy             ___  _ __    ___ | || |(_) _ __    __ _    __ _   __ _   __ _ (_) _ __")
    print("                                            aAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa   AAAAA7             / __|| '_ \\  / _ \\| || || || '_ \\  / _` |  / _` | / _` | / _` || || '_ \\")
    print("                                             8RRNAAAAAAAAAAAAAAAAAAAAAAAAAAAAA9   AAAE              \\__ \\| |_) ||  __/| || || || | | || (_| | | (_| || (_| || (_| || || | | | _ ")
    print("                                  kEAA7sy               s9221ZYXWKAAAAAAMUZ45d    AAAl              |___/| .__/  \\___||_||_||_||_| |_| \\__, |  \\__,_| \\__, | \\__,_||_||_| |_|(_)")
    print("                                 pGAAAAAAAAAAAAGeoz                          qu   AAp                    |_|                           |___/          |___/")
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
    print("")
    
    return

#The splitter is done message
def end():
    print("")
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
    print("Please check your zip files before you upload your project.")
    print("Because, ")
    print("even if something works for someone it might not work for others.")
    print("I hope you have a great life")

def cls_():
    os.system('cls' if os.name == 'nt' else 'clear')

def license():
    print("")
    print("THE FUCK PAYING! ATTRIBUTE AND DONATE LICENSE (TFPADL)")
    print("")
    print("Version 1.0")
    print("")
    print("By using this piece of software, you agree to the following terms:")
    print("")
    print("1. You are granted the right to use, modify, and redistribute this software under the following conditions:")
    print("    i) Your modified or unmodified version, and/or your own project using this software, must be distributed free of charge.")
    print("    ii) Proper attribution to the original authors must be provided.")
    print("    iii) If you receive donations related to the distribution or use of this software, you must encourage people to also donate to the original authors by providing a link to their website, account, donation links, or project page.")
    print("    iv) You must include the source code of your version, along with a link to the original version.")
    print("")
    print("2. Use of this software is at your own risk. The original authors will not be responsible for any damages or liabilities arising from the use, modification, or distribution of this software.")
    print("")
    print("3. The original authors reserve the right to change the terms of this license at any time without prior notice. You are obligated to comply with the updated terms.")
    print("")
    print("4. Non-compliance with the terms of this license will result in the immediate termination of your rights to use this software and may lead to legal action.")
    print("")
    print("Original Authors:")
    print("Ingenarel")
    print("")


#Variables for runtime
class variables:
    #The title Variable
    local_version="v1.1"
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
                variables.folder_name=input("Please enter your foldername. (CASE SENSITIVE!)").strip() #.lower() #Just in case you change your mind.
                if variables.folder_name in ["cls", "clear"]:
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
            if variables.file_count == 0:
                while True:

                    variables.file_count=int(input("Enter the number of files to copy in to each folder: ")).strip()
                    
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
            
            # The actual copying finally happens.
            source_files = os.listdir(variables.source_folder)  # List of files in the source folder
            for filename in tqdm(source_files, desc="Copying files"):  # tqdm wrapper for progress bar
                variables.source_file = os.path.join(variables.source_folder, filename)
                
                # Copy files to the current destination folder
                shutil.copy(variables.source_file, os.path.join(variables.destination_base_folder, str(variables.folder_count), variables.folder_name, variables.output_dir))
                
                variables.count += 1
                
                # If specified number of files are copied, reset the file counter and move to the next destination folder
                if variables.count == variables.file_count:
                    variables.count = 0
                    variables.folder_count += 1
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
        source_file = input("Enter the name of the blend file that you want to copy (with extension): ").strip()

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

    # Get a list of immediate subdirectories in the Destination folder
    directories = [d for d in os.listdir(destination_folder) if os.path.isdir(os.path.join(destination_folder, d))]

    # Iterate over immediate subdirectories in the Destination folder with a progress bar
    for directory in tqdm(directories, desc="Copying blend file"):
        # Construct destination path
        destination_path = os.path.join(destination_folder, directory, os.path.basename(source_file))
        # Copy the file to each subdirectory
        shutil.copy2(source_file, destination_path)

    print("Blend file copy pasted successfully.")

    zip_files()
        

#The zipper function (No humans have been harmed at the making.)
def zip_files():
    print("Please wait while I zip the files... >.<")

    # Change directory to the destination folder
    os.chdir(variables.destination_folder)

    # Get a list of directories in the current folder
    directories = [d for d in os.listdir() if os.path.isdir(d)]

    # Loop through each folder in the destination folder with a progress bar
    for folder_name in tqdm(directories, desc="Zipping folders"):
        # Create a zip file with the same name as the folder
        with zipfile.ZipFile(f"Split-It-{folder_name}.zip", "w", zipfile.ZIP_DEFLATED) as zip_file:
            # Walk the directory, and add all files and empty folders to the zip file
            for root, dirs, files in os.walk(folder_name):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip_file.write(file_path, os.path.relpath(file_path, folder_name))
                for dir in dirs:
                    dir_path = os.path.join(root, dir)
                    zip_info = zipfile.ZipInfo(os.path.relpath(dir_path, folder_name) + "/")
                    zip_file.writestr(zip_info, '')

    print("All folders zipped successfully.")
    ask_deletion()

#Asking if filders (except the zip files!) want to be deleted.
def ask_deletion():
    while True:
        print("\nDo you want to delete the folders that were created when you split the project?")
        print("The zip files won't be deleted, just the folders and files that were created in order to make those zips.")
        choice = input("y to delete and n to cancel: ").lower()[0:1].strip()

        if choice == "y":
            # Get a list of directories to delete
            directories_to_delete = [item for item in os.listdir() if os.path.isdir(item)]
            total_directories = len(directories_to_delete)

            if total_directories > 0:
                print(f"\nDeleting {total_directories} directories...")
                # Loop through all directories and delete them with a progress bar
                for item in tqdm(directories_to_delete, desc="Deleting directories"):
                    os.system(f"rd /s /q \"{item}\"")
                print("\nAll split cache folders deleted successfully.\nDon't worry, the zips aren't deleted.")
            else:
                print("\nNo directories found to delete.")
            break

        elif choice.lower() in ["cls", "clear"]:
            cls_()
            continue

        else:
            print('Error: Please use either "y" or "n"')
    os.chdir("..")
    success_msg()
    end()

def helpsite():
    print("______________________________________________________________________________________________________________________________________________________")
    print("|:‾‾‾‾‾‾‾‾‾‾‾‾‾|‾‾‾‾‾‾‾‾‾‾‾‾|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾:|")
    print("|:   COMMAND   | ALSO KNOWN |                                                     DESCRIPTION                                                       :|")
    print("|:    NAME     |     AS     |                                                                                                                       :|")
    print("|:=============|============|=======================================================================================================================:|")
    print("|:             |            |   It checks your version. then displayes your current version and the latest version. If the current version is the   :|")
    print("|:             |            |  is updated than the latest stable built release, the says that you're using a version that is newer than the latest  :|")
    print("|:     ver     |   version  |   stable build. And if the current version is older than the latest version, it says that there is a newer version    :|")
    print("|:             |            |                 available. If the version is the same as the latest version, it just tells you that.                  :|")
    print("|:             |            |                                           Should work only on the main menu.                                          :|")
    print("|:=============|============|=======================================================================================================================:|")
    print("|:    cls      |   clear    |                            Clears the screen. Works anywhere where you can put an input.                              :|")
    print("|:=============|============|=======================================================================================================================:|")
    print("|:    exit     | esc, close |                                   Exits the program. Should work only on the main menu.                               :|")
    print("|:=============|============|=======================================================================================================================:|")
    print("|:             |            |    At first it goes to your cache folder. Then it takes the first x ammount files from the config file. x is you,     :|")
    print("|:             |            |   setting how much files it will take per folder. it could be 1/2/3 basically anything. Only an integer tho lol. It   :|")
    print("|:             |            |   pastes those files in a different folder. It will first create a folder called Destination. It will store all the   :|")
    print("|:             |            |  files and folders that are split. Then it creates another folder inside it that's the same name as your simulation   :|")
    print("|:             |            |     cache folder. And then create another folder called config inside it and then paste those files in the config     :|")
    print("|:             |            |                                   folder. To show it visually it's doing this...                                      :|")
    print("|:             |            |                                                                                                                       :|")
    print("|:             |            |                                         Destination                                                                   :|")
    print("|:             |            |                                           -> 1                                                                        :|")
    print("|:             |            |                                             ->simulation folder name                                                  :|")
    print("|:             |            |                                               ->config                                                                :|")
    print("|:             |            |                                                 ->the first x amount of files                                         :|")
    print("|:             |            |                                                                                                                       :|")
    print("|:             |            |   The next step is doing the same thing for all those files. Creates folders called 1, 2, 3 etc basically an unique   :|")
    print("|:             |            |                            folder for each x amount of files so now it looks like this...                             :|")
    print("|:             |            |                                                                                                                       :|")
    print("|:             |            |                                        Destination                                                                    :|")
    print("|:             |            |                                          -> 1                                                                         :|")
    print("|:             |            |                                            -> simulation folder name                                                  :|")
    print("|:             |            |                                              -> config                                                                :|")
    print("|:             |            |                                                -> the first x amount of files                                         :|")
    print("|:             |            |                                          -> 2                                                                         :|")
    print("|:             |            |                                            -> simulation folder name                                                  :|")
    print("|:             |            |                                              -> config                                                                :|")
    print("|:      s      |    start   |                                                -> the second x amount of files                                        :|")
    print("|:             |            |                                                                                                                       :|")
    print("|:             |            |   Then it does the same thing for the data and mesh folder in your simulation directory. then it asks questions it    :|")
    print("|:             |            |       would do with the guiding, noise, and particles folder. either split them too if they have files in them        :|")
    print("|:             |            |    (which i personally didn't have on my projects) or just create those folders that are named guiding, noise, and    :|")
    print("|:             |            |  particles in the split cache directory so it works properly. then it copy pastes your blend file in each sub folder  :|")
    print("|:             |            |                                       in the destination folder. that means...                                        :|")
    print("|:             |            |                                                                                                                       :|")
    print("|:             |            |                                        Destination                                                                    :|")
    print("|:             |            |                                          -> 1                                                                         :|")
    print("|:             |            |                                            -> your blend file                                                         :|")
    print("|:             |            |                                            -> simulation folder name                                                  :|")
    print("|:             |            |                                              -> config                                                                :|")
    print("|:             |            |                                                -> the first x amount of files                                         :|")
    print("|:             |            |                                                                                                                       :|")
    print("|:             |            |                                          -> 2                                                                         :|")
    print("|:             |            |                                            -> your blend file                                                         :|")
    print("|:             |            |                                            -> simulation folder name                                                  :|")
    print("|:             |            |                                              -> config                                                                :|")
    print("|:             |            |                                                -> the second x amount of files                                        :|")
    print("|:             |            |                                                                                                                       :|")
    print("|:             |            |  etc etc then it creates a zip for the 1 folder. then the 2 folder. so on and so on the zip files are created in the  :|")
    print("|:             |            |     Destination folder Then it asks you if it shoudld delete the subfolders that were created while the spliiting     :|")
    print("|:             |            |  happened. You can choose to delete them. If you wish to do so, it will delete those 1, 2, 3 folders. Deleting those  :|")
    print("|:             |            |   folders won't matter because you'll still have the zips.This functions was created so that you don't waste extra    :|")
    print("|:             |            |                                          space. Should work only on the main menu.                                    :|")
    print("|:=============|============|=======================================================================================================================:|")
    print("|:   license   |            |                                   Shows the licnese. Should work only on the main menu.                               :|")
    print("|:_____________|____________|_______________________________________________________________________________________________________________________:|")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print("")
    
    # |::| - this is for the devs so that we can copy paste it every time we need to expand the box

def update_check(**kwargs):
    try:
        response=requests.get(kwargs["url"])
        if response.status_code == 200:
            latest_release = response.json()
            latest_version = latest_release.get('tag_name')

        else:
            if response.status_code == 400:
                print("")
                print("ERROR 400: bad request.")
                print("")
                print("his status code indicates that there's something off with the request you sent to the server.")
                print("t's like filling out a form incorrectly or forgetting to provide essential details.")
                print("he server couldn't understand or process your request due to missing or malformed data.")
                print("")
        
            elif response.status_code == 401:
                print("")
                print("ERROR 401: Unauthorized")
                print("")
                print("This status code means you're not allowed to access the requested resource without proper authentication.")
                print("It's like trying to enter a restricted area without showing your ID.")
                print("You need to provide valid credentials, such as a username and password or an authentication token, to gain access.")
                print("")
        
            elif response.status_code == 403:
                print("")
                print("ERROR 403: Forbidden.")
                print("")    
                print("You're being denied access, plain and simple.")
                print("Even with valid credentials, you're not allowed to access the resource because you lack the necessary permissions.")
                print("It's like trying to enter a building without the proper authorization or access card.")
                print("You need to request permission from the appropriate authorities.")
                print("")
        
            elif response.status_code == 404:
                print("ERROR 404: File not found.")
                print("")
                print("This status code indicates that the server couldn't find the resource you requested.")
                print("It's like looking for a book on a library shelf only to discover it's not there.")
                print("The resource may have been moved, deleted, or simply never existed.")
                print("Double-check the URL or try searching for the resource in a different location.")
                print("")

            elif response.status_code == 422:
                print("")
                print("ERROR 422: Unprocessable Entity.")
                print("")
                print("Ah, it seems there's a problem with the data you provided. ")
                print("This status code typically occurs when the server understands your request but can't process it due to invalid data.")
                print("It's like trying to fill out a form with incorrect or incomplete information.")
                print("Review the data you submitted and ensure it meets the server's requirements.")
            
            elif response.status_code == 429:
                print("")
                print("ERROR 429: Too Many Requests.")
                print("")
                print("Slow down there! You've been making too many requests to the server within a short period. ")
                print("This status code indicates that you've hit a rate limit, and the server is asking you to ease up for a bit.")
                print("It's like trying to take too many slices of cake at once, and someone politely suggests you wait your turn.")
                print("")

            elif response.status_code == 500:
                print("")
                print("ERROR 500: Server Side Error.")
                print("")
                print("Uh-oh, something went wrong on the server's end, and it's not your fault.")
                print("This status code indicates an unexpected problem occurred while the server was trying to process your request.")
                print("It's like ordering food at a restaurant and having the kitchen catch fire.")
                print("The server is apologizing for the inconvenience and asking for your patience while they sort things out.")
                print("")
        
            elif response.status_code == 503:
                print("")
                print("ERROR 503: Server was not ready")
                print("")
                print("Hold your horses! The server is currently unavailable to handle your request.")
                print("This status code typically occurs due to maintenance or overload.")
                print("It's like calling a store outside of business hours and getting a message saying they're closed for the day.")
                print("You'll need to try again later when the server is back up and running.")
                print("")

            else:
                print(f"I Don't know what the fuck are you doing but I can't find an error code for you.\n")
    except requests.exceptions.RequestException:
        print("")
        print("Failed to retrieve the latest version from GitHub.")
        print("Please check your internet connection.")
        print("")
        return
    
    if latest_version:
        print(f"Current version: {variables.local_version}.")
        print(f"Latest version: {latest_version}.")
        
        if variables.local_version>latest_version:
            print("You're using a version that is newer than the latest stable built.")
    
        elif variables.local_version == latest_version:
            print("You are already using the latest version.")
        
        else:
            while True:
                print("A new version is available. Do you want to download it?")
                print("You if you want to use the latest version, you need to start it from the downloaded version though.")
                print("It creates a folder called latest_build and stores the zip there.")
                choice = input("press y to download and n to cancel: ").strip()
                
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
        input("press enter to go back to the main menu.").strip()

        return
    
def credits():
        print("")
        print("______________________________________________________________________________________________________________________________________________________________________")
        print("|:‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾:|")
        print("|:   Ingenarel                                                                                                                                                      :|")
        print("|:                                                                                                                                                                  :|")
        print("|:   Follow me on Instagram -                                                  https://www.instagram.com/saad_abdullah999666/                                       :|")
        print("|:   Reddit account -                                                          https://reddit.com/user/INGENAREL                                                    :|")
        print("|:   Discord -                                                                 ingenarel#2846                                                                       :|")
        print("|:   My youtube channel -                                                      https://www.youtube.com/channel/UC90Tar8Bpx3Q8UqpM8qxWZw?sub_confirmation=1          :|")
        print("|:   Sponsor me on SheepIt -                                                   https://www.sheepit-renderfarm.com/user/ingenarel/profile                            :|")
        print("|:   My github account -                                                       https://github.com/ingenarel                                                         :|")
        print("|:   Here's my public renderkey if you wanna connect a device to my account -  XQVDMUjdOKt7LBldxjuF0YERqLoGnExbeh8yUrce                                             :|")
        print("|:__________________________________________________________________________________________________________________________________________________________________:|")
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        print("")
        print("______________________________________________________________________________________________________________________________________________________")
        print("|:‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾:|")
        print("|:   Chaosminecraft                                                                                                                                 :|")
        print("|:   His youtube channel -                                                          https://www.youtube.com/@chaosminecraft3399                     :|")
        print("|:   Sponsor him on SheepIt -                                                       https://www.sheepit-renderfarm.com/user/Chaosminecraft/profile  :|")
        print("|:   His github account -                                                           https://github.com/Chaosminecraft                               :|")
        print("|:__________________________________________________________________________________________________________________________________________________:|")
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        print("")

    # |::| - this is for the devs so that we can copy paste it every time we need to expand the box


#the main function that handles the stuff.
def main_func():
    while True:
        print("")
        print("You can type 'Ver' to check if an update is there.")
        print("You can type 'cls' to clean the Terminal/Command Prompt.")
        print("Type 's' to use the splitter.")
        print("Type 'help' for an in depth guide about every command")
        print("Type 'c' for credits.") 
        print("")
        
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
        
        if starting_choice=="g" or starting_choice=="gui":
            gui_process=Process(target=main_ui)
            gui_process.start()

        else:
            print("")
            print("Invalid input.")
            print("")

class StartupVar:
    commandline=True
    current_config_version="1"

#The class for basic operation of the Window with the strings.
class UiVariables:
    root="" #The main window
    setting_window="" #the window for the upcomming settings window
    gui_size={"width": "500", "height": "350"} #the scale the Window is gonna be at
    current_theme={"bg": "#666", "button": "#888", "text": "#FFF", "checkbox": "#000"} #Currently only flat colors are there.
    current_settings={}
    setting_window=False #a variable to check if there is already a settings window running.
    going_crazy=0 #That is a variable of code that i happened to add for fun, but if not wanted, you can safely remove it with the code that uses it.
    #the strings that are used in the UI
    checkbox_var=""      #the variable to keep track of the checkbox value
    strings={
        "browse": "Browse for the folder (recommended that it is in the same folder most likely for now.)",
        "presplit": "Select a folder before splitting.",
        "splitamount": "How many files should each split have?",
        "deletetext": "Do you wanna delete the folders SplitIt made to make the ZIP files?",
        "splitbutton": "SplitIt!",
        "exitbutton": "Exit"
    }

#That is for now for the convenience of having the buttons and anything that is interactable in there.
class UiLayout:
    browse_button=""     #that is the browse button
    target_foldername="" #that is to display the folder name
    split_label=""       #that shows the message for the split amount.
    split_amount=""      #that takes in a value to split a file to x amount of files.
    delete_message=""    #that shows the deletion message
    delete_checkbox=""   #simple checkbox 🤷‍♂️
    split_button=""      #button to start splitting using the CLI version of the code.
    exit_button=""       #that only closes the window.

#That is for the GUI variant that can be Sperately called with the CLI version.
def main_ui():
    UiVariables.root=Tk() #Making the window
    UiVariables.root.config(bg=UiVariables.current_theme.get("bg")) #applying the background
    UiVariables.root.title(variables.title) #setting the title
    UiVariables.root.resizable(width=False, height=False) #telling tkinter to not let it be able to resize
    UiVariables.root.geometry(f"{UiVariables.gui_size.get("width")}x{UiVariables.gui_size.get("height")}") #setting the intended size
    UiLayout.browse_button=Button(UiVariables.root, text=UiVariables.strings.get("browse"), bg=UiVariables.current_theme.get("button"), fg=UiVariables.current_theme.get("text"), padx=5, pady=5, command=list_folders_gui)
    UiLayout.browse_button.place(x=18, y=10)
    UiLayout.target_foldername=Label(UiVariables.root,text=UiVariables.strings.get("presplit"), relief="raised", bg=UiVariables.current_theme.get("button"), fg=UiVariables.current_theme.get("text"), padx=6, pady=5)
    UiLayout.target_foldername.place(x=150, y=50)
    UiLayout.split_label=Label(UiVariables.root, text=UiVariables.strings.get("splitamount"), relief="raised", bg=UiVariables.current_theme.get("button"), fg=UiVariables.current_theme.get("text"),  padx=6, pady=5)
    UiLayout.split_label.place(x=125, y=110)
    UiLayout.split_amount=Entry(UiVariables.root, bg=UiVariables.current_theme.get("button"), fg=UiVariables.current_theme.get("text"),  width=50)
    UiLayout.split_amount.place(x=85, y=150)
    UiLayout.delete_message=Label(UiVariables.root, text=UiVariables.strings.get("deletetext"), relief="raised", bg=UiVariables.current_theme.get("button"), fg=UiVariables.current_theme.get("text"),  padx=6, pady=5)
    UiLayout.delete_message.place(x=55, y=200)
    UiVariables.checkbox_var=IntVar()
    UiLayout.delete_checkbox=Checkbutton(UiVariables.root, relief="raised",  bg=UiVariables.current_theme.get("button"), fg=UiVariables.current_theme.get("checkbutton"),  onvalue=True, offvalue=False, variable=UiVariables.checkbox_var)
    UiLayout.delete_checkbox.place(x=450, y=202)
    UiLayout.split_button=Button(UiVariables.root, text=UiVariables.strings.get("splitbutton"), bg=UiVariables.current_theme.get("button"), fg=UiVariables.current_theme.get("text"))
    UiLayout.split_button.place(x=100, y=275)
    UiLayout.exit_button=Button(UiVariables.root, text=UiVariables.strings.get("exitbutton"), bg=UiVariables.current_theme.get("button"), fg=UiVariables.current_theme.get("text"))
    UiLayout.exit_button.place(x=300, y=275)
    UiVariables.root.mainloop() #running the window.

def list_folders_gui():
    root = Tk()
    root.withdraw()  # Hide the tkinter window

    # Prompt user to select a folder using the file manager dialog
    folder_path = filedialog.askdirectory(title="Select Folder")

    # Return the folder name if a folder is selected
    if folder_path:
        variables.folder_name = os.path.basename(folder_path)
        print("Selected folder:", variables.folder_name)
        UiVariables.folder_path_entry.config(text=f"The folder was chosen: {variables.folder_name}")
        return
    else:
        if UiVariables.going_crazy==0:
            UiLayout.target_foldername.config(text=f"Th... you chose cancel, That isn't a folder.")
        elif UiVariables.going_crazy==1:
            UiLayout.target_foldername.config(text=f"You yet again chose to close it the wrong way.")
        elif UiVariables.going_crazy==2:
            UiLayout.target_foldername.config(text=f"THAT... (breathes in and out) No.")
        elif UiVariables.going_crazy==3:
            UiLayout.target_foldername.config(text=f"Stop it please :(")
        elif UiVariables.going_crazy==4:
            UiLayout.target_foldername.config(text=f"Why are you doing that? Is it funny?") #for me to make it it was at least funny.
        elif UiVariables.going_crazy==5:
            UiLayout.target_foldername.config(text=f"You do know that eventually the texts stop right?")
        elif UiVariables.going_crazy==6:
            UiLayout.target_foldername.config(text=f"*sighs* okay, there might be some still, but stop please.")
        elif UiVariables.going_crazy==7:
            UiLayout.target_foldername.config(text=f"Are you getting any enjoyment out of that? Like how?")
        elif UiVariables.going_crazy==8:
            ctypes.windll.user32.MessageBoxW(0, "What is making you do that? Why are you continuing even though i told you to stop?", "Stop it please", 0)
        UiVariables.going_crazy+=1
        return

#That is to make the config
def make_config():
    #the config variables set by default with some metadata of the config version
    UiVariables.current_settings={
        "config_version": "1",
        "commandline": True,
        "bg theme": "#666",
        "button theme": "#888",
        "text color": "#FFF"
    }
    with open("config.json", "w") as file:
        json.dump(UiVariables.current_settings, file)
    
    return

#the initialisation step to look if the CLI version shall be started.
def init():
    attempts=0 #the current attempts
    max_attempts=10 #The max attempts to make a config file
    try:
        while attempts!=max_attempts:
            try:
                with open("config.json") as file:
                    UiVariables.current_settings=json.load(file)
                break

            except FileNotFoundError:
                make_config()
                attempts+=1
        if UiVariables.current_settings.get("config_version")>StartupVar.current_config_version:
            print("WARNING: there has been a version that was unexpected been used. please use the same version if possible!")
            input("Press enter to exit")
            exit()
    except:
        pass
    
    if UiVariables.current_settings.get("commandline")==True:
        print("CLI")

        system = platform.system()

        def windows_fullscreen():
            pyautogui.hotkey('win', 'up')

        def macos_fullscreen():
            try:
                pyautogui.hotkey('ctrl', 'cmd', 'f')
            except:
                pyautogui.hotkey('ctrl', 'win', 'f')

        def linux_fullscreen():
            try:
                pyautogui.hotkey('ctrl', 'super', 'f')
            except:
                pyautogui.hotkey('ctrl', 'win', 'f')

        if system == 'Windows':
            windows_fullscreen()
        elif system == 'Linux':
            linux_fullscreen()
        elif system == 'Darwin':
            macos_fullscreen()
        
        start(title=variables.title)
    
    elif UiVariables.current_settings.get("commandline")==False:
        print("UI")
        main_ui()

if __name__ == "__main__":
    init()
