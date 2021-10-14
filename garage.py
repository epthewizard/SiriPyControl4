from c4_auth import director
from pyControl4.relay import C4Relay
import asyncio

garage = C4Relay(director, 232)

def toggle_garage():
	asyncio.run(garage.toggle())
	return 'Garage was Toggled'