import boto3
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Source and Backup Bucket Names (update these!)
    source_bucket = 'my-source-bkt2'
    backup_bucket = 'my-backup-bkt2'
    
    # List all objects in the source bucket
    objects = s3.list_objects_v2(Bucket=source_bucket)['Contents']
    
    # Copy each file to the backup bucket
    for obj in objects:
        key = obj['Key']
        copy_source = {'Bucket': source_bucket, 'Key': key}
        s3.copy_object(
            CopySource=copy_source,
            Bucket=backup_bucket,
            Key=key
        )
        print(f"Copied {key} to backup bucket.")
    
    return {
        'statusCode': 200,
        'body': 'Backup completed successfully!'
    }