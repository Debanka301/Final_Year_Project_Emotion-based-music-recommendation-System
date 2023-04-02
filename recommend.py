import numpy as np
import pandas as pd
import pickle

similarity= pickle.load(open('similarity.pkl','rb'))
songs= pickle.load(open('songs_dict.pkl','rb'))
new= pd.DataFrame(songs)

def recommend_song(song):
    index = new[new['track_name'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])[1:6]

    recommended_songs=[]
    for i in distances:
        recommended_songs.append(new.iloc[i[0]].track_name)
    return recommended_songs

# print(recommend_song('all about you'))
# print(recommend_song("don't throw your love away"))
