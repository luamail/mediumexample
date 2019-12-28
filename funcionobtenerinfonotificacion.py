import json
import boto3
def lambda_handler(event, context):
    # TODO implement
    #print(event)
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    bucket_arn = event['Records'][0]['s3']['bucket']['arn']
    key = event['Records'][0]['s3']['object']['key']
    print(bucket_name)
    print(bucket_arn)
    print(key)
    return {
        'statusCode': 200,
        'body': json.dumps('Todo a salido bien!')   
    }
