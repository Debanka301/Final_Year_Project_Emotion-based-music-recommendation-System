from recommend import recommend_song

def recommender(emotion):
    if emotion=="happy":
        return recommend_song("all about you")
    else:
        return recommend_song("don't throw your love away")
    
print(recommender("happy"))