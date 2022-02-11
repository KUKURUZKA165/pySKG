from json import loads
import steam.webauth as wa
from time import sleep
from utils import *
badcount = 0

global user
global sessionID


async def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = wa.WebAuth(username, password)
    try:
        user.login()
    except wa.EmailCodeRequired:
        code = input("Enter email code: ")
        user.login(email_code=code)
    except wa.TwoFactorCodeRequired:
        code = input("Enter 2FA code: ")
        user.login(twofactor_code=code)
    sessionID = user.session.cookies.get_dict()["sessionid"]
    return user, sessionID


async def activate_key(keys):
    global badcount
    for key in keys:
        r = user.session.post('https://store.steampowered.com/account/ajaxregisterkey/',
                              data={'product_key': key, 'sessionid': sessionID})
        blob = loads(r.text)
        
        # Success
        if blob["success"] == 1:
            for item in blob["purchase_receipt_info"]["line_items"]:
                print("[ Redeemed ]", item["line_item_description"])
        else:
            # Error codes from https://steamstore-a.akamaihd.net/public/javascript/registerkey.js?v=qQS85n3B1_Bi&l=english
            error_code = blob["purchase_result_details"]
            s_error_message = "Unknown error!"
            if error_code == 14:
                s_error_message = 'The product code you\'ve entered is not valid. Please double check to see if you\'ve mistyped your key. I, L, and 1 can look alike, as can V and Y, and 0 and O.'

            elif error_code == 15:
                s_error_message = 'The product code you\'ve entered has already been activated by a different Steam account. This code cannot be used again. Please contact the retailer or online seller where the code was purchased for assistance.'

            elif error_code == 53:
                s_error_message = 'There have been too many recent activation attempts from this account or Internet address. Please wait and try your product code again later.'
                badcount = 10

            elif error_code == 13:
                s_error_message = 'Sorry, but this product is not available for purchase in this country. Your product key has not been redeemed.'
                await potential_key(key + "\n")

            elif error_code == 9:
                s_error_message = 'This Steam account already owns the product(s) contained in this offer. To access them, visit your library in the Steam client.'
                await potential_key(key + "\n")

            elif error_code == 24:
                s_error_message = 'The product code you\'ve entered requires ownership of another product before activation.\n\nIf you are trying to activate an expansion pack or downloadable content, please first activate the original game, then activate this additional content.'
                await potential_key(key + "\n")

            elif error_code == 36:
                s_error_message = 'The product code you have entered requires that you first play this game on the PlayStation®3 system before it can be registered.\n\nPlease:\n\n- Start this game on your PlayStation®3 system\n\n- Link your Steam account to your PlayStation®3 Network account\n\n- Connect to Steam while playing this game on the PlayStation®3 system\n\n- Register this product code through Steam.'
                await potential_key(key + "\n")

            elif error_code == 50:
                s_error_message = 'The code you have entered is from a Steam Gift Card or Steam Wallet Code. Browse here: https://store.steampowered.com/account/redeemwalletcode to redeem it.'
                await potential_key(key + "\n")

            else:
                s_error_message = 'An unexpected error has occurred.  Your product code has not been redeemed.  Please wait 30 minutes and try redeeming the code again.  If the problem persists, please contact <a href="https://help.steampowered.com/en/wizard/HelpWithCDKey">Steam Support</a> for further assistance.'
                await potential_key(key + "\n")

            print("[ Error ]", s_error_message)
            badcount = badcount + 1
            if badcount >= 10:
                print("Detected more than 10 invalid keys redeemed. Sleeping 31m.")
                sleep(1860)
                badcount = 0
