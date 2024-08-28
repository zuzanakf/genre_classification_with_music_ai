from musicai_sdk import MusicAiClient

client = MusicAiClient(api_key='your-api-key')

# Get application info
app_info = client.get_application_info()
print('Application Info:', app_info)

# Upload local file
file_url = client.upload_file(file_path='your-file-path')
print('File Url:', file_url)

# Create Job
workflow_params = {
    'inputUrl': file_url,
}
create_job_info = client.create_job(job_name='your-job-name', workflow_id='your-workflow-id',params=workflow_params)
job_id = create_job_info['id']
print('Job Created:', job_id)

# Wait for job to complete
job_info = client.wait_for_job_completion(job_id)
print('Job Status:', job_info['status'])
print('Job Result:', job_info['result'])

# Get job info
job_info = client.get_job(job_id=job_id)
print('Job Status:', job_info['status'])
print('Job Result:', job_info['result'])

# Delete job
client.delete_job(job_id=job_id)

# Get all jobs
jobs = client.get_jobs()
print('Jobs:', jobs)