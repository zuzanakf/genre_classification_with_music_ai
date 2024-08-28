import pandas as pd

#file paths
song_info_path = 'output_folder/song_info.csv'
generated_path = 'output_folder/generated.csv'

#load
song_info_df = pd.read_csv(song_info_path)
generated_df = pd.read_csv(generated_path)

#mapping
genre_mapping = dict(zip(generated_df['Original File Name'], generated_df['musicai_genre']))

#new column in song_info_df for musicai_gen_genre
song_info_df['musicai_gen_genre'] = song_info_df['mp3/wav'].map(genre_mapping)

#save
song_info_df.to_csv(song_info_path, index=False)

print("song_info.csv has been updated with the 'musicai_gen_genre' column.")
