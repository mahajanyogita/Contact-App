import re
import Exceptions as e

def check_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        pass
    else:
        raise e.IncorrectEmail


def isValid_Phone(s):

    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
    if(Pattern.match(s)):
        pass
    else:
        raise e.IncorrectPhone

