# SiriPyControl4

This can be used to access your Control4 lights/relays/etc through Siri. 
The benefit is not having to set up homebridge or buy expensive drivers to integrate. Flask is used to serve up API endpoints which are 
authenticated through the PyControl4 package. 

**Installation**
1. Clone the package and create a `.env` file in the same folder. Then add the environment variables which are used to authenticate like
the IP of your C4 controller, C4USERNAME and C4Pass. Check the `c4auth.py` file to find the exact environment variable names.
2. Install the requirements with `pip3 install -r requirements.txt`
3. You need to find the item ID of the light/relay/etc you want to change. To do this, run the `get_item_ids.py` file and it will output all of your C4 controller information. It will be alot but you can search through it and find the item ID's that you need and change them in the script.
3. Run the program with `python3 main.py` and it serve up the endpoints.
4. Now the important part, go to the shortcuts app on your IPhone, add a new shortcut, hit add action, and then search for "get contents of url"
5. Click that and enter the IP and port that flask is running on as well as the endpoint you are trying to hit. For example, a garage would be ```<IP>:<PORT>/garage/toggle``
6. Change the request type to POST and then add form data with the environment variable you set for FLASKPASS.
7. Give the new shortcut a name and you can now use Siri with Control4
