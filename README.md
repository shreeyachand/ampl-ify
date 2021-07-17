# spoti-flask


## Requirements
- Flask
- Spotipy
- additional in requirements.txt

## Installation
1. Log in to the [Spotify Developer dashboard](https://developer.spotify.com/dashboard/applications) and create a new app with the name and description of your liking
2. Clone the project and activate the virtual environment by running the following in the terminal:
```
git clone https://github.com/shreeyachand/spoti-flask.git spoti-flask
cd spoti-flask
source venv/bin/activate
```

3. Create an .env file in the directory either manually or by running ```touch .env``` in the terminal. Get the client id and secret from the online dashboard as shown here:
<img width="527" alt="Screen Shot 2021-07-15 at 2 47 56 PM" src="https://user-images.githubusercontent.com/76849512/125841169-80d21bc9-010b-43bf-9844-cd33ef85ee1f.png"> 
and add them to the .env file like this:

```
SPOTIPY_CLIENT_ID="your client id here"
SPOTIPY_CLIENT_SECRET="your client secret here"
```
4. In your app's dashboard, click the "Edit Settings" button
<img width="244" alt="Screen Shot 2021-07-15 at 2 50 19 PM" src="https://user-images.githubusercontent.com/76849512/125841477-0211e73c-a3f2-4016-8752-420717d89f58.png">
and add the following links under "Redirect URIs"
<img width="541" alt="Screen Shot 2021-07-15 at 2 52 56 PM" src="https://user-images.githubusercontent.com/76849512/125841766-a60a925f-bb37-4f00-a634-27050e212722.png"> 
Be sure to add any other links (with /redirect) for any other places you will be hosting the app. Note the difference between **/redirect** and **/redirect/** as well as **http** and **https** when redirecting, so make sure to add all versions of the link if you encounter problems with the redirect URI.
5. Run ```flask run``` in the terminal and navigate to http://localhost:5000 to run the app!
