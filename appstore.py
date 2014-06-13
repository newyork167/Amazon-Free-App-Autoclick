from splinter import Browser
import time

username = "username"
password = "password"
appstore_url = 'http://www.amazon.com/mobile-apps/b?ie=UTF8&node=2350149011'
login_url = "https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Dgno_signin"

with Browser() as browser:
	browser.visit(login_url)
	browser.fill('email', username)
	browser.fill('password', password)
	sign_in = browser.find_by_id('signInSubmit-input').first.click()
	
	# Sleep to allow time for login to work
	time.sleep(5)
	browser.visit(appstore_url)
	button = browser.find_by_id('fad-get-started-button')
	button.first.click()
	
	# Sleep in case you want to confirm
	time.sleep(5)