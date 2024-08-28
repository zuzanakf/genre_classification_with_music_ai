from dotenv import load_dotenv
import os
from musicai_sdk import MusicAiClient, process_folder

load_dotenv()

#API key
api_key = os.getenv('MUSICAI_API_KEY')

# Initialize client
client = MusicAiClient(api_key=api_key)

# input and output folders and the workflow ID
input_folder = 'input_folder'
output_folder = 'output_folder'
workflow_id = 'your-workflow-id'

#process all files in input folder
process_folder(
    input_folder=input_folder,
    output_folder=output_folder,
    workflow_id=workflow_id,
    client=client,
    parallelism=10,  #adjust to the number of parallel processes needed
    delete=True      #true if want to delete job from platform after download
)

#save
print('Processing complete. Results have been saved to:', output_folder)
