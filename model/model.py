print("Creating model...\n")
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
import pickle

features = ['popularity', 'danceability', 'energy', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
df = pd.read_csv('./model/tracks_clean.csv')
X = df[features]
scaler = StandardScaler()
scaled = scaler.fit_transform(X)
nn = NearestNeighbors(n_neighbors=10,algorithm='ball_tree')
nn.fit(scaled)
pickle.dump(nn, open('./model/nnmodel.pkl', 'wb'))
df['id'].to_csv('./model/track_ids.csv',index_label=False)
print('Exported model and CSV!')