import pandas as pd

class HarmonyMusicRecommender:
    def __init__(self, data_file):
        self.data = pd.read_csv(data_file)  # Assuming the data is stored in a CSV file
    
    def recommend_music(self, user_id, num_recommendations):
        # Filter data for the given user
        user_data = self.data[self.data['user_id'] == user_id]
        
        # Calculate the average rating for each song
        song_ratings = user_data.groupby('song_id')['rating'].mean().reset_index()
        
        # Sort songs by average rating in descending order
        sorted_songs = song_ratings.sort_values('rating', ascending=False)
        
        # Get the top N recommendations
        recommendations = sorted_songs['song_id'].head(num_recommendations)
        
        return recommendations
    
# Usage example
if __name__ == '__main__':
    recommender = HarmonyMusicRecommender('music_data.csv')
    user_id = 'user123'
    num_recommendations = 5
    recommendations = recommender.recommend_music(user_id, num_recommendations)
    print(f"Recommendations for user {user_id}: {recommendations}")
