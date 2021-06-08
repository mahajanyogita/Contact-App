from Model import contact
from View import Exceptions as e

import sqlite3
db = sqlite3.connect('contacts.db')
cur = db.cursor()
class Repository(contact.Contact):
    def __init__(self):

        cur.execute("Create Table if not exists contact_details ("
                + "fname text,lname text,phone_number text,email_id text)")
        db.commit()

    def add_contact(self,contact):

        try:
            cur.execute("Select * from contact_details where fname=? and lname=?", (contact.get_fname(),contact.get_lname()))
            result = cur.fetchone()
            if(result):
                res = self.search_by_name(contact.get_fname(),contact.get_lname())
                return "Contact Already Exists",res
            else:
                query="insert into contact_details values(?,?,?,?)"
                records=(contact.get_fname(),contact.get_lname(),contact.get_phone_number(),contact.get_email_id())
                cur.execute(query,records)
                res = self.search_by_name(contact.get_fname(),contact.get_lname())
                return "Contact Added",res

        except sqlite3.Error as e:
            return "Failed to add Contact",e

    def search_by_name(self,fname,lname):
        cur.execute("Select * from contact_details where fname=? and lname=?",(fname,lname))
        result = cur.fetchone()
        if(result):
            fname, lname, phone_number, email_id = result
            contacts = contact.Contact(fname, lname, phone_number, email_id)
            return contacts
        else:
            raise e.ContactNotFound

    def search_by_phone_no(self,phone_no):
        cur.execute("Select * from contact_details where phone_number=?",(phone_no,))
        result = cur.fetchone()
        if(result):
            fname, lname, phone_number, email_id = result
            contacts = contact.Contact(fname, lname, phone_number, email_id)
            return contacts
        else:
            raise e.ContactNotFound

    def edit_contact(self,fname,lname,updated_fname,updated_lname):
        cur.execute("update contact_details set fname=?,lname=? where fname=? and lname=?",(updated_fname,updated_lname,fname,lname))
        db.commit()
        res=self.search_by_name(updated_fname,updated_lname)
        return "Contact Edited",res

    def edit_contact_phone_no(self, fname, lname, updated_phone_no):
        cur.execute("update contact_details set phone_number=? where fname=? and lname=?",(updated_phone_no,fname,lname))
        db.commit()
        res = self.search_by_name(fname,lname)
        return "Contact Edited",res


    def edit_contact_email(self, fname, lname, updated_email):
        cur.execute("update contact_details set email_id= ? where fname=? and lname=?",(updated_email,fname,lname))
        db.commit()
        res = self.search_by_name(fname, lname)
        return "Contact Edited",res


    def delete_contact_by_name(self,fname,lname):
        try:
            cur.execute("select * from contact_details where fname=? and lname=?",(fname,lname))
            res=cur.fetchone()
            if(res):
                cur.execute("delete from contact_details where fname=? and lname=?",(fname,lname))
            else:
                return "Contact Not Found"
        except sqlite3.Error as e:
            print(e)
        else:
            db.commit()
            return "Contact Deleted"


    def show_all_contacts(self):
        contact_list=[]
        cur.execute("select * from contact_details")
        while True:
            contacts = cur.fetchone()
            if not contacts:
                break
            else:
                fname, lname, phone_number, email_id=contacts
                cont=contact.Contact(fname,lname,phone_number,email_id)
                contact_list.append(cont)
        if(len(contact_list)==0):
            raise e.ContactLogEmpty

        return contact_list
