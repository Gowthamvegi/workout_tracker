## workout_tracker

Code Explanation
The Python script workout_tracker.py does the following:

User Input:

The script prompts the user to input information about the exercises they did.
Nutritionix API Request:

The user input is used to construct parameters (params) for a POST request to the Nutritionix API.
The requests.post method is used to send the request to the API with the provided headers.
Sheety Google Sheet Update:

The response from the Nutritionix API is used to update a Google Sheet using the Sheety API.
Basic authentication is used with Sheety credentials provided in config.py.
