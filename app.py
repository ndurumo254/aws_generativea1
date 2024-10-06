import boto3
import botocore.config



def blog_generate_using_bedrock(blogtopic:str) ->str:
    prompt= f""