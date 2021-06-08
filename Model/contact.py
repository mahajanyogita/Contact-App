class Contact:
    def __init__(self,fname,lname,phone_number=0,email_id=''):
        self.fname=fname
        self.lname=lname
        self.phone_number=phone_number
        self.email_id=email_id

    def get_fname(self):
        return self.fname

    def get_lname(self):
        return self.lname

    def get_phone_number(self):
        return self.phone_number

    def get_email_id(self):
        return self.email_id

    def __str__(self):
        return "First Name : {}\t\tLast Name:{}\t\tPhone_Number :{}\t\tEmail_Id:{}".format(self.fname,self.lname,self.phone_number,self.email_id)



