import os
from musicai_sdk import MusicAiClient, process_folder


#API key
api_key = os.getenv('MUSICAI_API_KEY')

# Initialize client
client = MusicAiClient(api_key=api_key)

# input and output folders and the workflow ID
input = 'input_folder'
output = 'output_folder'
workflow_id = 'untitled-workflow-5a6c33'

#process all files in input folder
process_folder(
    input_folder=input,
    output_folder=output,
    workflow_id=workflow_id,
    client=client,
    parallelism=10,  #adjust to the number of parallel processes needed
    delete=False     #true if want to delete job from platform after download
)

#save
print('Processing complete. Results have been saved to:', output)
