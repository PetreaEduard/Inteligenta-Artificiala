from re import sub
from decimal import Decimal
from hashlib import new
import requests
from bs4 import BeautifulSoup
import smtplib
sender='nu_vreau_spam@coneasorin.ro'
subject='Pretul a scazut la:'
to_addr_list = ['petreaeduard20.01@gmail.com']
cc_addr_list = ['']

def sendemail(sender, message, subject, to_addr_list, cc_addr_list=[]):
    try:
        smtpserver='mail.x-it.ro'
        header = 'From %s\n' % sender
        header += 'To %s\n' % ','.join(to_addr_list)
        header += 'Cc: %s\n' % ','.join(cc_addr_list)
        header += 'Subject %s\n\n' % subject
        message = header + message
        server = smtplib.SMTP(smtpserver,26)
        server.ehlo()
        server.starttls()
        server.login(sender,"stiinte216_2022")
        problems = server.sendmail(sender, to_addr_list, message)
        server.quit()
        return True
    except:
        print("Error: unable to send mail")
        return False
def data_scraping():
    req = requests.get("https://www.emag.ro/telefon-mobil-apple-iphone-14-pro-max-256gb-5g-deep-purple-mq9x3rx-a/pd/DJDY4LMBM/")
    soup = BeautifulSoup(req.text, "html.parser")  
    price = soup.find('p', attrs={'class':'product-new-price'}).text
    price = price.translate({ord('.'): None})
    size = len(price)
    mod_value = price[:size - 7]
    new_price = int(mod_value)
    if(new_price<7799):
        sendemail(sender,"Pretul a scazut la: "+str(new_price),subject,to_addr_list, cc_addr_list=[])
        print("Avem o modificare de pret!!!")
    else:
        print("Pretul nu a scazut")

data_scraping()



