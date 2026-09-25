# only def's

def incorrect_enter_inclog_ageacc_username(inc_log , age_acc , u_n):
    while True:
        if inc_log.isdigit():
            break

        else:
            print("your incorrect login is wrong")
            inc_log = input("Enter your incorrect login agian: ")

    while True:
        if age_acc.isdigit():
            break

        else:
            print("your age account is wrong")
            age_acc = input("Enter your age account agian: ")

    while True:
        if u_n.isalnum():
            break

        else:
            print("your user name is wrong")
            u_n = input("Enter your user name agian: ")

    return u_n , inc_log , age_acc 


def incorrect_enter_pswrd(pswrd):
    
    while True:
        wrng_pswrd = False
        num_report = False
        al_report = False
        for i in pswrd:
            if i.isdigit():
                num_report = True
            elif i.isalpha():
                al_report = True
            elif i == "_" :
                continue
            else:
                print("your password is wrong")
                wrng_pswrd = True
                pswrd = input("Enter your password agian: ")
                break
                                       
        if wrng_pswrd:
            continue

        elif num_report and al_report:
            break
        
        elif not num_report and not al_report:
            print("your password is wrong")
            pswrd = input("Enter your age password agian: ")

        else:
            break

    return pswrd

def wrong_len_pswrd(pswrd):
    while True:
        if len(pswrd) < 8:
            print("your password is very weak")
            pswrd = input("Enter your password agian: ")
            continue

        elif 8 <= len(pswrd) < 12:
            print("your password is weak")
            q = input("do you want to change your password?:(y/n) ")
            q = q.lower()    
            if q == "y":
                pswrd = input("Enter your password agian: ")
                pswrd = incorrect_enter_pswrd(pswrd)
                continue

            elif q == "n":
                break
            else:
                print("your answer is inccorect")
                continue
        elif len(pswrd) >= 12:
            print("your password is stronge now")
            break
    
    return pswrd

def score_rate_len_p(pswrd_len , score_rate_pswrd):
    
    if 8 <= pswrd_len < 12:
        score_rate_pswrd += 10

    if 12 <= pswrd_len < 16:
        score_rate_pswrd += 20

    if 16 <= pswrd_len:
        score_rate_pswrd += 30

    return score_rate_pswrd

def info(u_n , pswrd , inc_log , age_acc , score_rate_pswrd , score_rate_inc_log):
    print("Username: ",u_n)
    print("Password: " , end="")
    for u in pswrd:
        print("*" , end="")
    print()
    print("Incorrect Login: " ,inc_log)
    print("Age Account: " ,age_acc , "day")
    print("Password Score: " ,score_rate_pswrd, "/ 100")
    print("Login Score:" ,score_rate_inc_log ,"/ 20")

def alnum_lowup(nm_exst , al_exst , low_exst , up_exst , pswrd , score_rate_pswrd):
        for o in pswrd:
            if o.isdigit():
                nm_exst = True
     
            if o.isalpha():
                al_exst = True
        
            if o.islower():
                low_exst = True

            if o.isupper():
                up_exst = True

        if low_exst:
            score_rate_pswrd += 20

        if up_exst:
            score_rate_pswrd += 20

        if nm_exst:
            score_rate_pswrd += 10

        if al_exst:
            score_rate_pswrd += 10
        
        return score_rate_pswrd

def score_inc_log(inc_log , score_rate_inc_log):
    if inc_log <= 2:
        score_rate_inc_log += 20

    elif 3 <= inc_log <= 5:
        score_rate_inc_log += 15

    elif 6 <= inc_log <= 10:
        score_rate_inc_log += 10

    elif 11 <= inc_log <= 20:
        score_rate_inc_log += 5

    else:
        score_rate_inc_log += 0

    return score_rate_inc_log
#____________________________valuables______________________________#


u_n = input("Enter your user name: ")

pswrd = input("Enter your password: ")
pswrd = incorrect_enter_pswrd(pswrd)
pswrd = wrong_len_pswrd(pswrd)

inc_log = input("Enter your incorrect login: ")

age_acc = input("Enter your age account: ")

u_n, inc_log, age_acc = incorrect_enter_inclog_ageacc_username(inc_log , age_acc , u_n)


#_______________________password codes_________________________#

pswrd_len = len(pswrd)

if 12 <= pswrd_len < 16:
    print("your password is good")

elif 16 <= pswrd_len:
    print("your password is strong")

score_rate_pswrd = 0

score_rate_pswrd = score_rate_len_p(pswrd_len , score_rate_pswrd)

nm_exst = False
al_exst = False
low_exst = False
up_exst = False

score_rate_pswrd = alnum_lowup(nm_exst , al_exst , low_exst , up_exst , pswrd , score_rate_pswrd)


count_rep = 0

for d in range(0 , len(pswrd) - 1):
    if pswrd[d] == pswrd[d + 1]:
        count_rep += 1

if count_rep >= 3:
    score_rate_pswrd -= 10

if count_rep < 3:
    score_rate_pswrd += 10
    
#_________________incorrect login codes__________________#

score_rate_inc_log = 0
inc_log = int(inc_log)


score_rate_inc_log = score_inc_log(inc_log , score_rate_inc_log)

info(u_n , pswrd , inc_log , age_acc , score_rate_pswrd , score_rate_inc_log)
