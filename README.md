# ampl-ify

Currently, the app is hosted at https://ampl-ify.herokuapp.com, but it is in development mode, so additional users needed to be added by me. Fill out [this form](https://docs.google.com/forms/d/e/1FAIpQLSeM8OUUgS0DQAx4xq5SjVxpz9AOIOKRWag70q6s8yDkpxwxhw/viewform) to become a user.

## Table of Contents
1. [Requirements](https://github.com/shreeyachand/ampl-ify#requirements)
2. [Installation](https://github.com/shreeyachand/ampl-ify#installation)
3. [Algorithm](https://github.com/shreeyachand/ampl-ify#algorithm)

## Requirements
- Flask
- Spotipy
- additional in requirements.txt

## Installation
1. Log in to the [Spotify Developer dashboard](https://developer.spotify.com/dashboard/applications) and create a new app with the name and description of your liking
2. Clone the project and create a virtual environment by running the following in the terminal:
```
git clone https://github.com/shreeyachand/ampl-ify.git ampl-ify
cd ampl-ify
python3 -m venv venv
source venv/bin/activate
```
3. Install the project dependencies by running ```pip install -r requirements.txt```

4. Create an .env file in the directory by running ```touch .env``` in the terminal. Get the client id and secret from the online dashboard as shown here: <br> <img width="527" alt="Screen Shot 2021-07-15 at 2 47 56 PM" src="https://user-images.githubusercontent.com/76849512/125841169-80d21bc9-010b-43bf-9844-cd33ef85ee1f.png"> <br> and add them to the .env file like this:

```
SPOTIPY_CLIENT_ID="your client id here"
SPOTIPY_CLIENT_SECRET="your client secret here"
```
5. In your app's dashboard, click the "Edit Settings" button <img width="100" alt="Screen Shot 2021-07-15 at 2 50 19 PM" src="https://user-images.githubusercontent.com/76849512/125841477-0211e73c-a3f2-4016-8752-420717d89f58.png"> and add the following links under "Redirect URIs": <br> <img width="541" alt="Screen Shot 2021-07-15 at 2 52 56 PM" src="https://user-images.githubusercontent.com/76849512/125841766-a60a925f-bb37-4f00-a634-27050e212722.png">

Be sure to add any other links (with /redirect) for any other places you will be hosting the app. Note the difference between **/redirect** and **/redirect/** as well as **http** and **https** when redirecting, so make sure to add all versions of the link if you encounter problems with the redirect URI.


6. Download [this dataset](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks?select=tracks.csv) from Kaggle as `.tracks.csv` (you can call it whatever you want as long as you change the name in the Jupyter Notebook in the next step).
7. Create the NearestNeighbors model by running the cells in [`ModelingTracks.ipynb`](https://github.com/shreeyachand/ampl-ify/blob/main/ModelingTracks.ipynb). You don't need to run any cells after exporting the pickle model, those are a work in progress.

8. Run ```flask run``` in the terminal and navigate to http://localhost:5000 to run the app!

Note: The app will be in [development mode](https://developer.spotify.com/community/news/2021/05/27/improving-the-developer-and-user-experience-for-third-party-apps/) until a quota request is approved. For others using it or for testing with up to 25 other accounts, the email addresses need to be added in the dashboard.

## Algorithm
The app uses NearestNeighbors from the sklearn Python package to "plot" the audio and other features of ~600k songs from [this dataset](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks?select=tracks.csv). When a user selects a playlist, the average features of the songs are passed through the model and songs within a certain distance of the average are found and shown to the user. Currently, the features used by the model are popularity, danceability, energy, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, and tempo. I plan to add categorical features like artists by one-hot encoding the values and utilizing each track of a playlist to find close neighbors instead of the average of all of them. [See how the model was made](https://github.com/shreeyachand/ampl-ify/blob/main/ModelingTracks.ipynb).
