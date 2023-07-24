from beeline import BeelineAPI

bl = BeelineAPI()

number = int(input("Telefon raqam kiriting (998901234567): "))

# Nomer Beelineda mavjudmi shuni tekshiramiz
exist =  bl.existnumber(number)
if exist.get('status'): 
    print("Tastiqlash kodi yuborilmoqda...")
    
    otp = bl.sendOTP(number)
    if otp.get('code') == "OK":
        code = int(input("> "))
        login = bl.login(number, code)
        if login.get('accessToken', False) != False:
            accessToken = login['accessToken']
            refreshToken = login['refreshToken']
            datas = bl.datas(accessToken, refreshToken, number)
            # Men barcha malumotlarni ekranga chiqazib qo'ydim
            # Kerakli malumotni o'zingiz olib ishlatasiz
            print(datas)
        else:
            # Yuborilgan kodda xato bo'lsa yoki boshqa xatolarni ko'rish
            print(login['text']['uz'])
    else:
        # Juda ko'p urinish va boshqa xatoliklar ko'rish
        print(otp)
else:
    # Raqam Beeline mijozi bo'lmasa yoki raqam noto'g'ri kiritgandagi xatoliklarini ko'rish
    print(exist['text']['uz'])
