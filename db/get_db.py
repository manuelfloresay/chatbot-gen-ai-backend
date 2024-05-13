import boto3
import json
import logging
logging.basicConfig(level=logging.DEBUG)

def get_item_from_dynamodb(rut):
  logging.info("Initializing connection to Cloud Database")
  dynamodb = boto3.client("dynamodb", region_name='us-east-1')
  found_customer = dynamodb.get_item(TableName='customer', Key={'rut':{'S':rut}})
  logging.debug("Item found in Database: %s", found_customer)
  return found_customer['Item']