import hashlib
import os,sys
import time
import random
from zlib import DEF_BUF_SIZE

class Game(object):
    def __init__(self,index):
        self.index=index
        self.level = 0
        self.money = 100
        self.loses = 0
        self.small_monster = 1
        self.xp = -10
        self.new_level = self.level

    def check_stats(self):
        if self.xp > 120:
            print(f"Youre up to Level {self.new_level}! And got {self.get_money} EURO.")
            self.new_level = 2
            self.money = self.money + self.get_money
        else:
            pass
        if self.xp > 190:
            print(f"Youre up to Level {self.new_level+1}! And got {self.get_money} EURO.")
            self.new_level = 3
            self.money = self.money + self.get_money
        else:
            pass
        if self.xp > 240:
            print(f"Youre up to Level {self.new_level+2}! And got {self.get_money} EURO.")
            self.new_level = 4
            self.money = self.money + self.get_money
        else:
            pass
        if self.new_level > 5:
            input("BIGGER THAN 5")
        else:
            pass

    def menustart(self):
        self.menu = input(str(f"""
Menu:
    [X] -> Check Profile
    [Y] -> Play Level {self.new_level}
    [F] -> Quit
""")) 

        if self.menu == "X":
            print(f"""
Profile:
    Level: {self.new_level},
    Money: {self.money} EURO,
    Loses: {self.loses},
    XP: {self.xp},
""")
            time.sleep(3)
            self.menustart()
        elif self.menu == "Y":
            self.startlevel()
        elif self.menu == "F":
            sys.exit()


    def startlevel(self):
        os.system("cls")
        self.choose_challenge = input(str("""
1 - Kill small monsters (Farm/Easy/XP Farm)
2 - Kill Bigger Monsters (Medium)
3 - Kill insane monsters (Hard, for big levels)
4 - Boss monsters (Accessible Every 5th level.)
"""))
        print(self.choose_challenge+"\n")
        if self.choose_challenge == "1":
            self.amount_kill = int(input("Amount of kills (1 kill 10 XP): "))
            self.new_amount_kill_under_ten_level=random.randrange(0,13)
            self.new_amount_kill_under_twenty_level=random.randrange(11,36)
            self.get_money=random.randrange(5,30)
            for i in range(self.amount_kill+1):
                self.xp += 10
                if self.level < 5:
                    print(f"Killed monsters {i}")
                    if i == self.new_amount_kill_under_ten_level:
                        print("Couldnt kill more, your level is weak!")
                        print(f"Gained {self.xp} XP!")
                        self.xp = self.xp
                        if self.xp > 80:
                            self.new_level += 1
                            self.money = self.money + self.get_money
                        else:
                            print(f"Need 90 XP to level {self.level+1}!")
                        if self.xp > self.xp:
                            self.check_stats()
                            self.menustart()
                        else:
                            time.sleep(3)
                            self.menustart()
                        break
                else:
                    continue
                
                time.sleep(0.1)
                self.small_monster += 1
        elif self.choose_challenge == "2":
            pass
        elif self.choose_challenge == "3":
            pass
        elif self.choose_challenge == "4":
            pass


    def start(self):
        os.system("cls")
        self.name = input(str("Enter Name: "))
        print("Welcome,",self.name+"!")

        self.menu = input(str(f"""
Menu:
    [X] -> Check Profile
    [Y] -> Play Level {self.level}
    [F] -> Quit
"""))   

        if self.menu == "X":
            print(f"""
Profile:
    Level: {self.level},
    Money: {self.money} EURO,
    Loses: {self.loses},
""")
            self.menustart()
        elif self.menu == "Y":
            self.startlevel()
        elif self.menu == "F":
            sys.exit()

        

run = Game(0)
run.start()