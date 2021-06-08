
class IncorrectEmail(Exception):
    def __str__(self):
        return "Invalid Email "

class IncorrectPhone(Exception):
    def __str__(self):
        return "Invalid Phone Number"

class ContactNotFound(Exception):
    def __str__(self):
        return "Contact Not Found"

class ContactLogEmpty(Exception):
    def __str__(self):
        return "Contact List is Empty"