from c4_auth import director
from pyControl4.light import C4Light
import asyncio

# Create new C4Light instance
light = C4Light(director, 240)

def check_lights():
	return 'Lights are On' if asyncio.run(light.getState()) == True else 'Lights are Off' 

# # Toggle the lights
def toggle_lights():
    asyncio.run(light.changeLightState())
    return 'Lights Toggled'
