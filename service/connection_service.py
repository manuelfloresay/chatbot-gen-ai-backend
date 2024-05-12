import boto3
import json

def get_item_from_dynamodb(rut):
  dynamodb = boto3.client("dynamodb", region_name='us-east-1')
  found_customer = dynamodb.get_item(TableName='customer', Key={'rut':{'S':rut}})
  return found_customer['Item']