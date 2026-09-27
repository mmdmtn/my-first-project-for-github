player = {
        "name" : input("❓Enter your name : "),
        "Team" : input("Select a team (1.CT  2.T): ").lower(),
        "kill" : 0,
        "hs" : 0,
        "death" : 0,
        "hp" : 100,
        "money" : 800
}

weapon_pri = {
        "ak" : 2700,
        "awp" : 4750,
        "m4a4" : 2300,
        "m4a1" : 1900,
        "galil" : 2100,
        "p90" : 1850,
        "xm_1014" : 1750,
        "deagle" : 900,
        "usp_s" : 800,
        "glock" : 800,
        "armor" : 1800
}

weapon_dam = {
        "ak" : 35,
        "awp" : 100,
        "m4a4" : 30,
        "m4a1" : 25,
        "galil" : 30,
        "p90" : 20,
        "xm_1014" : 15,
        "deagle" : 60,
        "usp_s" : 45,
        "glock" : 20
}

TEAM_1 = 0
TEAM_2 = 0


def buy_menu():
    print("=============Buy Menu=============")
    for weapon, price in weapon_pri.items():
        print("🔫 " + weapon + " : " + str(price) +"$ 💵")
    print
    print("👉💵your money: " + str(player["money"]) + "💵")
        
def select_team(player):
    while True:
        if player["Team"] not in ["ct" , "t"]:
            print("your select is invalid")
            player["Team"] = input("Select a team (1.CT  2.T): ").lower()
        else:
            print("you are " + player["Team"].upper())
            break
def select_gun(sel_gun, weapon_pri):
    while True:
        if sel_gun not in weapon_pri:
            print("your gun is invalid")
            sel_gun = input("Select a gun for play agian : ").lower()
        else:
            player["gun"] = sel_gun
            break
    return sel_gun

def price_gun(player, weapon_pri, sel_gun):
    while True:
        if player["money"] < weapon_pri[sel_gun]:
            print("❌your money isn't enough❌")
            sel_gun = input("❓Select a gun for play agian : ").lower()
            sel_gun = select_gun(sel_gun, weapon_pri)
        else:
            player["money"] -= weapon_pri[sel_gun]
            print("✅ "+ sel_gun + " has been selected!💥")
            break
    return sel_gun

def won_round(player):
    print("+300$ for kill")
    print("+3000$ for win")
    print("🎉you won this round🥳")           
    player["money"] += 3300
    player["kill"] += 1

def lose_round(player):
    print("☠you lost this round👻")
    print("-100$ for death")
    print("+1450$ for loss")
    player["money"] += 1350
    player["death"] += 1
    player["hp"] -= (100 / 5)


def info(player):
    print("your money: " + str(player["money"]))
    print("your kill: " + str(player["kill"]))
    print("your headshot: " + str(player["hs"]))
    print("your death: " + str(player["death"]))
    print("your hp: " + str(int(player["hp"])))
    
def start_round():
    for round_num in range(1, 14):
        if player["hp"] <= 0:
            print("☠you are dead☠")
            print("THE FINAL RESULT is:")
            info(player)
            if player["kill"] <= 3:
                print("you are very weak in this game😒\nback to school🖐")
                break

            elif 4 <= player["kill"] <= 7:
                print("you are midlevel in this game👌\nwell played🖐")
                break
            elif 8 <= player["kill"] <= 10:
                print("you can train and reach the pro in this game\n🙌nice played🖐")
                break
            elif 11 <= player["kill"] <= 13:
                print("WOW! you are pro in this game\n⭐very good and nice play👍\n⭐good luck✋ ")
                break
        
        if player["hp"] <= 25:
            print("❗LOW HP💢")

        print("==========Round" + str(round_num) + "==========")

        if round_num > 1:
            print("👉💵your money: " + str(player["money"]) + "💵")
            t = input("Do you want to buy a gun (y/n): ")
            while True:
                if t not in ["y" , "n"]:
                    print("your answer is wrong")
                    t = input("Do you want to buy a gun (y/n): ") 

                elif t == "y":
                    buy_menu()
                    sel_gun = input("❓Select a gun for play : ").lower()
                    sel_gun = select_gun(sel_gun, weapon_pri)
                    sel_gun = price_gun(player, weapon_pri, sel_gun)
                    break

                else:
                    print("your gun: " + player["gun"])
                    break
                
        print("1.kill\n2.headshot\n3.death\n4.nothing")
        s = str(input("Select a chois: "))

        while s not in ["1", "2", "3", "4"]: 
            print("your select isn't in list")
            s = str(input("Select a chois agian: "))


        if s == "1":
            won_round(player)
            info(player)
        
        elif s == "2":
            print("+500$ for headshot")
            won_round(player)            
            player["money"] += 500
            player["hs"] += 1
            info(player)

        elif s == "3":
            lose_round(player)
            info(player)

        else:
            print("nothing work in this round")
        

select_team(player)
buy_menu()
sel_gun = input("❓Select a gun for play : ").lower()
sel_gun = select_gun(sel_gun, weapon_pri)
sel_gun = price_gun(player, weapon_pri, sel_gun)
player["gun_dam"] = weapon_dam[sel_gun]

start_round()