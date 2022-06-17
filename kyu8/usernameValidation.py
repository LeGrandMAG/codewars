 
import re

def validate_usr(username):
    #your code here    
    regex = re.compile(r"^[a-z0-9_]{4,18}$")
    if(regex.match(username)):
        return True
    else: return False

print(validate_usr("legrandmag"))