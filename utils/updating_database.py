import pandas as pd

#file paths
song_info_path = 'output_folder/database.csv'
generated_path = 'output_folder/generated.csv'

song_info_df = pd.read_csv(song_info_path)
generated_df = pd.read_csv(generated_path)

#cols to be added from generated.csv to song_info.csv
columns_to_add = [
    'Result - musicai_genre',
    'Result - musicai_mood',
    'Result - musicai_energy',
    'Result - musicai_emotion',
    'Result - musicai_subgenre'
]

#dictionary mapping from 'Original File Name'
for column in columns_to_add:
    song_info_df[column] = song_info_df['mp3/wav'].map(dict(zip(generated_df['Original File Name'], generated_df[column])))

#rename the Result - musicai_genre
song_info_df.rename(columns={'Result - musicai_genre': 'musicai_gen_genre'}, inplace=True)

# Save the updated song_info.csv
song_info_df.to_csv(song_info_path, index=False)

print("song_info.csv has been updated with the additional columns.")
