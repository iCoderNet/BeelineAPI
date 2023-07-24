# Beeline API

Beeline tomonidan tayyor yaratilgan api tizimidan foydalanish uchun qo'llanma 


#### BeelineAPI
Ichida bir nechta funksiyalarni o'z ichiga olgan Class
`Exist`, `SendOTP`, `Login`, `DATAS` kabi funksiyalarga ega

#### Exist
`existnumber(number)` kiritish orqali beeline mijozi ekanligini tekshirish mumkin

#### SendOTP
`bl.sendOTP(number)` kiritish orqali shu telefon raqamga tastiqlash kodini yuborish mumkin bo'ladi
**Haddan tashqari ko'p tastiqlash kodi yubormang, har holda u Provider**

#### Login
`login(number, code)` kiritish orqali nomerga kelgan tastiqlash kod bilan raqamni kiritib loginni amalga oshiramiz va asosiy `accessToken` va `refreshToken` larni qo'lga kiritamiz


#### Datas
`datas(accessToken, refreshToken, number)` kiritish orqali tastiqlagan telefon raqamimizning barcha malumotlariga ega bo'ladi, Misol uchun: Kim tomonidan olingan, Qanday xizmatlar yoniq, balansida qancha mablag' bor va boshqa malumotlar


# Ishga tushirish:

```sh
python3 main.py
```

`main.py` faylida qisqa va sodda qilib qanday ishlatish uchun sxema qilib ketilgan