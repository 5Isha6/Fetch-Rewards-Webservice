# Calling webserver
1. Open a terminal and git clone the repository
2. In same directory,  run "python run.py"
By default this is set to run on localhost:5000
Now the server is up and users may call the endpoints

# Gain Points
Send a PUT request to ```http://localhost:5000/api/user/transaction``` to earn points
Eg. JSON {
    "payer": "Isha",
    "points": 100,
    "timestamp": "12/4/2022"
}


# Redeem points
Send a PUT request to ```http://localhost:5000/api/user/redeem``` to redeem points
{ "points": 5000 }

It sends back a response of the the transactions done to remove the points.
{"Isha": -100}

# Check final points
Send a GET request to ```http://localhost:5000/api/user/balance``` to see your detailed balance and the payer who sent them.

The caller recieves a JSON of the payer and points. 
{"Isha": 0}

