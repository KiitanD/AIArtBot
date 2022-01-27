import boto3, os, pathlib
from datetime import datetime, timezone
from dotenv import load_dotenv

#read in and set env variables
load_dotenv() 
AMAZONAPPKEY = os.environ.get('AMAZONAPPKEY')
AMAZONAPPSECRET = os.environ.get('AMAZONAPPSECRET')

client = boto3.client(
    's3',
    aws_access_key_id= AMAZONAPPKEY,
    aws_secret_access_key= AMAZONAPPSECRET
)

dt = datetime.now(timezone.utc).strftime("%d-%m-%y_%H")
apath = pathlib.Path(__file__).parent.resolve()
print(apath)
client.upload_file(Filename=f'{apath}/backup.zip', Bucket='artbotdump', Key=f'{dt}.zip')

