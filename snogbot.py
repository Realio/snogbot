from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
import random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.critical('This is a critical message.')
logging.error('This is an error message.')
logging.warning('This is a warning message.')
logging.info('This is an informative message.')
logging.debug('This is a low-level debug message.')


astral_counter = 50 #change to make bot run longer
levy_counter = 0 #up to 5 a day? better way obv

#quickbuttons
q_archeology = 'r'
q_blacksmith = 't'
q_sylph = 'y'
q_shop = 'o'
q_eudaemon = 'a'
q_skills = 's'
q_friendslist = 'f'
q_astrals = 'h'
q_guild = 'g'
q_inventory = 'b'
q_map = 'm'


#switch between modes
def switch_city():
    pyautogui.click(random.randrange(1478,1543,1),random.randrange(294,309,1))
    time.sleep(10)
    logging.info("switched to Home City")


#load
def load_game():
    driver = webdriver.Chrome()
    driver.get("http://www.kongregate.com/games/R2Games/wartune")
    logging.info("browser loaded")
    driver.maximize_window()
    time.sleep(2)
    logging.info("screen maximized")
    username = driver.find_element_by_id("welcome_username")
    username.send_keys("Realio")
    #username.send_keys("FroggerXP")
    #username.send_keys("weareyou")
    time.sleep(2)
    logging.info("username entered")
    password = driver.find_element_by_id("welcome_password")
    password.send_keys("snogger5444")
    #password.send_keys("sounders")
    time.sleep(2)
    logging.info("password entered")
    signin = driver.find_element_by_id("welcome_box_sign_in_button")
    signin.click()
    time.sleep(2)
    logging.info("verified user")
    cinematic = driver.find_element_by_id("cinematic_mode_link")
    cinematic.click()
    time.sleep(2)
    logging.info("cinematic mode initialized")
    frame = driver.find_element_by_id("gameiframe")
    driver.switch_to.frame(frame)
    serverlogin = driver.find_element_by_xpath('//*[@id="mS1"]')
    serverlogin.click()
    time.sleep(15)
    logging.info("loading....")
    time.sleep(30)
    logging.info("loading....")
    time.sleep(15)
    logging.info("game loaded")
    time.sleep(30) #slow load

#sound
def soundoff():
    logging.info("starting sound function")
    pyautogui.click(1584,284)
    logging.info("soundclick")
    time.sleep(5)
    pyautogui.click(804,527)
    logging.info("music off")
    time.sleep(1)
    pyautogui.click(804,606)
    logging.info("effects off")
    time.sleep(1)
    pyautogui.click(867,881)
    logging.info("confirmed")
    time.sleep(4)

#devotion
def daily_devotion():
    pyautogui.click(random.randrange(350,385,1),random.randrange(580,582,1))
    logging.info("devotion menu")
    time.sleep(2)
    pyautogui.click(random.randrange(565,685,1),random.randrange(535,580,1))
    logging.info("check-in reward")
    time.sleep(1)
    pyautogui.click(875,650)
    logging.info("check in confirmed")
    time.sleep(1)
    pyautogui.click(1257,436)
    logging.info("daily check in completed")
    time.sleep(4)

#experience
def daily_experience():
    pyautogui.click(427,636)
    logging.info("exp button")
    time.sleep(4)
    pyautogui.click(1110,688)
    logging.info("xp selected")
    time.sleep(1)
    pyautogui.click(1195,472) #exit
    logging.info("daily xp click completed")
    time.sleep(2)

#levy
def daily_levy():
    global levy_counter
    pyautogui.click(random.randrange(345,510,1),random.randrange(514,521,1))
    time.sleep(8)
    logging.info("you have used "+str(levy_counter)+" out of 5 levies today")
    pyautogui.click(random.randrange(1391,1553,1),random.randrange(782,803,1))
    time.sleep(4)
    logging.info("levy collected")
    levy_counter +=1
    pyautogui.click(1248,582) #exit
    logging.info("you have now used "+str(levy_counter)+" out of 5 levies today")
    time.sleep(8)

#spins
def daily_spins():
    global q_inventory
    pyautogui.typewrite(q_inventory)
    time.sleep(2)
    pyautogui.click(762,601)
    time.sleep(2)
    pyautogui.click(random.randrange(1121,1160,1),random.randrange(618,671,1))
    logging.info("snipers edge spin")
    time.sleep(6)
    pyautogui.click(914,830)
    time.sleep(2)
    pyautogui.click(random.randrange(1121,1160,1),random.randrange(618,671,1))
    logging.info("tenacity spin")
    time.sleep(6)
    pyautogui.click(920,889)
    time.sleep(2)
    pyautogui.click(random.randrange(1121,1160,1),random.randrange(618,671,1))
    logging.info("influence spin")
    time.sleep(6)
    pyautogui.click(1331,455)
    logging.info("spins completed")
    time.sleep(5)

#all first time login stuff
def login_daily_stuff():
    daily_devotion()
    time.sleep(5)
    daily_experience()
    time.sleep(5)
    daily_levy()
    time.sleep(5)
    daily_spins()
    time.sleep(5)
    sylph_expedition()
    time.sleep(5)

#map manipulation
def open_map():
    global q_map
    pyautogui.typewrite(q_map)
    logging.info("map opened")
    time.sleep(15)


#sylph arena
def sylph_arena():
    open_map()
    pyautogui.click(random.randrange(981,992,1),random.randrange(537,550,1))
    logging.info("walking to sylph arena")
    time.sleep(25)
    pyautogui.click(random.randrange(827,1215,1),random.randrange(748,768,1))
    logging.info("open sylph arena")
    time.sleep(15)
    count = 0
    while count < 10:
        pyautogui.click(random.randrange(1275,1350,1),random.randrange(753,825,1))
        logging.info("battle commenced")
        count += 1
        logging.info(str(count)+" battles completed")
        time.sleep(420)

    pyautogui.click(random.randrange(1393,1412,1),random.randrange(411,425,1))
    logging.info("sylph arena attempts completed")
    time.sleep(15)


#sylph expedition
def sylph_expedition():
    open_map()
    pyautogui.click(random.randrange(1000,1010,1),random.randrange(525,535,1))
    logging.info("walking to sylph expedition")
    time.sleep(25)
    pyautogui.click(random.randrange(827,1215,1),random.randrange(748,768,1))
    logging.info("open sylph expedition")
    time.sleep(5)
    '''

    #code here to automate - pick top sylph?
    pick helper
    pick top guy
    initiate
    blitz
    time.sleep(15 min) #blitzing
    exit
    time.sleep(10)
    '''

#arena
def arena():
    open_map()
    pyautogui.click(random.randrange(798,803,1),random.randrange(639,644,1))
    logging.info("walking to arena")
    time.sleep(20)
    pyautogui.click(random.randrange(841,1177,1),random.randrange(747,767,1))
    logging.info("opening arena")
    time.sleep(15)
    pyautogui.click(random.randrange(1058,1179,1),random.randrange(854,888,1))
    logging.info("duel")
    time.sleep(15)
    count = 0
    while count < 5:
        pyautogui.click(random.randrange(919,976,1),random.randrange(652,741,1))
        logging.info("choosing central opponent")
        time.sleep(20)
        pyautogui.click(random.randrange(868,1026,1),random.randrange(1048,1079,1))
        logging.info("autofight")
        count += 1
        logging.info("you have completed "+str(count)+" out of 10 battles")
        time.sleep(600)

    pyautogui.click(random.randrange(1468,1559,1),random.randrange(301,334,1))
    logging.info("back")
    time.sleep(15)
    pyautogui.click(random.randrange(1285,1307,1),random.randrange(454,476,1))
    logging.info("finished "+str(count)+" daily battles today")
    time.sleep(10)

'''
#eud bounty
def eud_bounty():
    open_map()
    pyautogui.click(random.randrange(,,1),random.randrange(,,1))
    logging.info("walking to bounty")
    time.sleep(15)
    pyautogui.click(random.randrange(,,1),random.randrange(,,1))
    logging.info("choosing bounty targets")
    pyautogui.click(random.randrange(,,1),random.randrange(,,1))
    logging.info("attack 1")
    send_keys(8)
    send_keys(6)
    time.sleep(45)
    pyautogui.click(random.randrange(,,1),random.randrange(,,1))
    logging.info("attack 2")
    send_keys(8)
    send_keys(6)
    time.sleep(45)
    pyautogui.click(random.randrange(,,1),random.randrange(,,1))
    logging.info("attack 3")
    send_keys(8)
    send_keys(6)
    time.sleep(45)
    pyautogui.click(random.randrange(,,1),random.randrange(,,1))
    logging.info("attack 4")
    send_keys(8)
    send_keys(6)
    time.sleep(45)
    pyautogui.click(random.randrange(,,1),random.randrange(,,1))
    logging.info("attack 5")
    send_keys(8)
    send_keys(6)
    time.sleep(45)
    pyautogui.click(random.randrange(,,1),random.randrange(,,1))
    logging.info("attack 6")
    send_keys(8)
    send_keys(6)
    time.sleep(45)
    pyautogui.click(random.randrange(,,1),random.randrange(,,1))
    logging.info("attack 7")
    send_keys(8)
    send_keys(6)
    time.sleep(45)
    pyautogui.click(random.randrange(,,1),random.randrange(,,1))
    logging.info("attack 8")
    send_keys(8)
    send_keys(6)
    time.sleep(45)
    pyautogui.click(random.randrange(,,1),random.randrange(,,1))
    logging.info("bounty completed")
'''

def astrals():
    global q_astrals
    pyautogui.typewrite(q_astrals)
    time.sleep(5)
    logging.info("astral page opened")
    global astral_counter
    count = 0
    while count < astral_counter:
        pyautogui.click(470,random.randrange(904,908,1)) #magus
        pyautogui.click(564,random.randrange(904,908,1)) #ceres
        pyautogui.click(655,random.randrange(904,908,1)) #pallas
        pyautogui.click(757,random.randrange(904,908,1)) #satum
        pyautogui.click(855,random.randrange(904,908,1)) #chiron
        pyautogui.click(897,813) #1click synth
        time.sleep(1)
        pyautogui.click(868,710) #confirm
        count = count+1
        if count % 10 == 0
            print(str(count)+" astrals completed")

    time.sleep(2)
    pyautogui.click(1034,414) #close
    logging.info(str(count)+" total astrals farmed this round")
    time.sleep(10)


#farm panel
def farm():
    switch_city()
    pyautogui.click(1587,494) #minimize quest tracking
    time.sleep(2)
    pyautogui.click(random.randrange(1331,1466,1),random.randrange(520,564,1)) #click farm
    time.sleep(10) #farm load can be slow
    logging.info("farm opened")
    kittens()
    #crops()
    #pasture()
    #dock()
    time.sleep(5)
    pyautogui.click(1578,1040) #return to home city
    logging.info("farming completed")

#kitten club
def kittens():
    pyautogui.click(1554,307) #kittens chosen
    time.sleep(5)
    pyautogui.click(random.randrange(582,671,1),random.randrange(636,658,1))
    time.sleep(1)
    pyautogui.click(random.randrange(582,671,1),random.randrange(880,904,1))
    time.sleep(1)
    pyautogui.click(random.randrange(834,924,1),random.randrange(780,806,1))
    time.sleep(1)
    pyautogui.click(random.randrange(1046,1135,1),random.randrange(635,659,1))
    time.sleep(1)
    pyautogui.click(random.randrange(1056,1150,1),random.randrange(884,911,1))
    time.sleep(1)
    logging.info("all 5 kittens retrieved")
    pyautogui.click(random.randrange(582,671,1),random.randrange(636,658,1))
    time.sleep(2)
    pyautogui.click(1088,520)
    logging.info("1")
    pyautogui.click(random.randrange(582,671,1),random.randrange(880,904,1))
    time.sleep(2)
    pyautogui.click(1088,520)
    logging.info("2")
    pyautogui.click(random.randrange(834,924,1),random.randrange(780,806,1))
    time.sleep(2)
    pyautogui.click(1088,520)
    logging.info("3")
    pyautogui.click(random.randrange(1046,1135,1),random.randrange(635,659,1))
    time.sleep(2)
    pyautogui.click(1088,520)
    logging.info("4")
    pyautogui.click(random.randrange(1056,1150,1),random.randrange(884,911,1))
    time.sleep(2)
    pyautogui.click(1088,520)
    logging.info("all 5 kittens reloaded")
    pyautogui.click(1241,422)
    time.sleep(10)
    logging.info("kittens completed")

def crops():
    pyautogui.click(1424,304) #open farm page
    time.sleep(5) #load farm
    pyautogui.click(1009,572)
    time.sleep(2)
    pyautogui.click(1009,572)
    time.sleep(2)
    logging.info("energized/refreshed tree")
    pyautogui.click(713,645)
    time.sleep(2)
    pyautogui.click(783,675)
    time.sleep(2)
    pyautogui.click(859,710)
    time.sleep(2)
    pyautogui.click(648,674)
    time.sleep(2)
    pyautogui.click(726,715)
    time.sleep(2)
    pyautogui.click(790,747)
    time.sleep(2)
    pyautogui.click(584,713)
    time.sleep(2)
    pyautogui.click(660,748)
    time.sleep(2)
    pyautogui.click(725,793)
    time.sleep(2)
    pyautogui.click(909,755)
    time.sleep(2)
    pyautogui.click(978,791)
    time.sleep(2)
    pyautogui.click(1048,825)
    time.sleep(2)
    pyautogui.click(845,792)
    time.sleep(2)
    pyautogui.click(921,825)
    time.sleep(2)
    pyautogui.click(989,859)
    time.sleep(2)
    pyautogui.click(780,832)
    time.sleep(2)
    pyautogui.click(856,862)
    time.sleep(2)
    pyautogui.click(926,901)
    time.sleep(5)
    logging.info("all crops harvested")
    # repeat above, planting crops
    #logging.info("crops finished")
    pyautogui.click(1359,420)
'''
def pasture():
    #some code here

def dock():
    pyautogui.click(1362,306) #dock chosen
    #some code here
'''
def catacombs():
    switch_city()
    pyautogui.click(random.randrange(620,690,1),random.randrange(760,790,1))
    time.sleep(2)
    logging.info("catacombs loaded")
    pyautogui.click(616,561)
    logging.info("forgotten catacombs chosen")
    time.sleep(1)
    pyautogui.click(1055,778) #crypt key
    pyautogui.click(1079,855)
    time.sleep(3)
    pyautogui.click(1062,751)
    logging.info("blitzing catacombs")
    time.sleep(3000)#time can be changed for blitz

    pyautogui.click(621,690)
    logging.info("tormented necropolis chosen")
    time.sleep(1)
    pyautogui.click(1055,778) #crypt key
    pyautogui.click(1079,855)
    time.sleep(3)
    pyautogui.click(1062,751)
    logging.info("blitzing necro")
    time.sleep(1)#time can be changed for blitz

    pyautogui.click(615,832)
    logging.info("purgatory maze chosen")
    time.sleep(1)
    pyautogui.click(1055,778) #purgatory key
    pyautogui.click(1079,855)
    time.sleep(3)
    pyautogui.click(1062,751)
    logging.info("blitzing maze")
    time.sleep(1)#time can be changed for blitz

#magic inn
def inn():
    #switch_city()
    count = 0
    pyautogui.click(random.randrange(860,930,1),random.randrange(750,800,1))
    logging.info("inn opened")
    time.sleep(4)
    pyautogui.click(random.randrange(1160,1275,1),random.randrange(910,925,1))
    logging.info("explore option")
    time.sleep(2)
    while count < 10:
        pyautogui.click(random.randrange(890,980,1),random.randrange(920,930,1)) #walking
        time.sleep(8)
        pyautogui.click(880,770) #confirmed
        count += 1
        print(str(count)+" out of 10 completed")
        time.sleep(2)
    pyautogui.click(1397,418) #confirmed
    time.sleep(2)
    pyautogui.click(1334,404) #exit
    time.sleep(5)
    logging.info("magic inn completed")

#main

#load_game()
#soundoff()
#login_daily_stuff()
#farm()
#sylph_expedition()
#catacombs
astrals()
#arena()
#kittens()
#inn()
#sylph_arena()
#catacombs()

#pyautogui.displayMousePosition()
input("wait for click...")
