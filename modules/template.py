# ~ IMPORT HERE ~

'''
    COMMENTS HERE
'''

class Main:
    def __init__(self):
        self.loaded = True # Don't touch this !
        self.returnOptionsSTR = False # Change it to True if your check function returns anything

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
    def authenticate(self): # Arguments here
        # Write your auth checking script here
        return False

    def check(self, items):
        try:
            # Write any optional code here!
            if(authentication):
                return authentication
            else:
                return False
        except:
            pass
