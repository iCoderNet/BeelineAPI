import requests
from http.cookies import SimpleCookie


class BeelineAPI:
    def __init__(self):
        session = requests.session()
        session.headers['User-agent'] = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36'
        session.headers['Referer'] = 'https://beeline.uz/uz/dashboard'
        session.headers['Accept'] = 'application/json, text/plain, */*'
        session.headers['Accept-Encoding'] = 'gzip, deflate, br'
        session.headers['Accept-Language'] = 'en,ru;q=0.9,uz;q=0.8'
        session.headers['Host'] = 'beeline.uz'
        session.headers['If-None-Match'] = 'W/"11e43-K4Vg5ZMZ4vZ2Age+XmtTvz9bnVE"'
        session.headers['sec-ch-ua'] = '"Not.A/Brand";v="8", "Chromium";v="114", "YaBrowser";v="23"'
        session.headers['sec-ch-ua-mobile'] = '?1'
        session.headers['sec-ch-ua-platform'] = '"Android"'
        session.headers['Sec-Fetch-Dest'] = 'empty'
        session.headers['Sec-Fetch-Mode'] = 'cors'
        session.headers['Sec-Fetch-Site'] = 'same-origin'
        session.headers['Xappkey'] = 'Gr8M2k5FQkbK'
        self.session = session
        self.cookies = None


    def parse_cookies(self, cookies_source):
        cookie = SimpleCookie()
        cookie.load(cookies_source)
        cookies = {k: v.value for k, v in cookie.items()}
        self.cookies = cookies
        return True

    def existnumber(self, number):
        try:
            response = self.session.get(f"https://beeline.uz/api/refill/args/auth/{number}/checkexists").json()
            return response
        except Exception as e:
            return {'ok': False, 'errors': str(e)}
        
    def sendOTP(self, number):
        try:
            self.parse_cookies("_ym_uid=1680160665154616425; _ym_d=1680160665; _ga_LMRG19E8FQ=GS1.1.1681784982.1.1.1681785785.25.0.0; _ga_JRPJZDEM31=GS1.1.1681784988.1.1.1681785785.0.0.0; _ga_2ZNH10TF1M=GS1.1.1687195457.1.1.1687196782.0.0.0; wp-wpml_current_language=uz; _gcl_au=1.1.1879833666.1690208893; konst-popup_last2=1690208892898; _gid=GA1.2.1309634740.1690208895; _ym_isad=1; _ym_visorc=w; chilla_popup_new=1690209038230; _ga=GA1.2.107750464.1680160664; _gat_UA-124738920-1=1; _ga_N837KGK1RT=GS1.1.1690208892.4.1.1690209570.0.0.0")
            response = self.session.post(f"https://beeline.uz/api/refill/args/auth/{number}/otp/send").json()
            return response
        except Exception as e:
            return {'ok': False, 'errors': str(e)}
        
    def login(self, number, otp_code):
        try:
            data = {"account":number,"password":otp_code}
            response = self.session.post(f"https://beeline.uz/api/refill/args/auth/login", data=data).json()
            return response
        except Exception as e:
            return {'ok': False, 'errors': str(e)}
        
    def datas(self, accessToken, refreshToken, number):
        try:
            cookies_source = f"_ym_uid=1680160665154616425; _ym_d=1680160665; phonePrefix=+998; phoneMask=9; _ga_N837KGK1RT=GS1.1.1681784972.3.1.1681785785.0.0.0; _ga_LMRG19E8FQ=GS1.1.1681784982.1.1.1681785785.25.0.0; _ga_JRPJZDEM31=GS1.1.1681784988.1.1.1681785785.0.0.0; _ga=GA1.2.107750464.1680160664; _ga_2ZNH10TF1M=GS1.1.1687195457.1.1.1687196782.0.0.0; wp-wpml_current_language=uz; accessToken={accessToken}; isAuth=true; refreshToken={refreshToken}; accessPhone={number}"
            self.parse_cookies(cookies_source)
            response = self.session.get(f"https://beeline.uz/api/refill/args/telco/v2/{number}/subscriptions/{number}/dashboard-updated", cookies=self.cookies).json()
            return response
        except Exception as e:
            return {'ok': False, 'errors': str(e)}


