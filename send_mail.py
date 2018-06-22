#############################################################################
#                                                                           #
#                                                                           #
#                       SENDMAIL IN PYTHON                                  #
#                                                                           #
#                                                                           #
#############################################################################



import smtplib
import os
def menu():
	global state
	server = smtplib.SMTP('smtp.gmail.com', 587)
	email = input("Your email (using gmail): ")
	pwd = input("Your password: ")
	print("Connecting...")
	server.starttls()
	server.login(email,pwd)
	state = 1 #email state
	loggedIn(server,email)
def send(server,email, user,text):
	try:
		server.sendmail(email, user, text)
	except Exception as e:
		print("Hmm didnt work, try adding less secure apps! opening website...")
		os.system("start https://myaccount.google.com/lesssecureapps")
		state = 0
		raise(e)
		menu()
def loggedIn(server,email):
	while True:
		user = input("Who do you want to send the email to? ")
		text = input("What do you want to send? ")
		send(server,email,user,text)
		print("Send complete!")
menu()
