from pyControl4.account import C4Account
from pyControl4.director import C4Director
from pyControl4.light import C4Light
import asyncio
from dotenv import load_dotenv
import os
import sys

if os.path.exists(".env"):
	load_dotenv()
	username = os.environ.get("C4USERNAME")
	password = os.environ.get("C4PASS")
	ip = os.environ.get("IP") 
	FLASKPASS = os.environ.get("FLASKPASS")
	
else:
	print("[-] Could not find the env file!")

try:
	"""Authenticate with Control4 account"""
	account = C4Account(username, password)
	asyncio.run(account.getAccountBearerToken())

	"""Get and print controller name"""
	accountControllers = asyncio.run(account.getAccountControllers())

	"""Get bearer token to communicate with controller locally"""
	director_bearer_token = asyncio.run(
		account.getDirectorBearerToken(accountControllers["controllerCommonName"])
	)["token"]

	"""Create new C4Director instance"""
	director = C4Director(ip, director_bearer_token)
except:
	director = None