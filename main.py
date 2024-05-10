import boto3

# os.environ["AWS_DEFAULT_REGION"] = "<REGION_NAME>"  # E.g. "us-east-1"
# os.environ["AWS_PROFILE"] = "<YOUR_PROFILE>"
# os.environ["BEDROCK_ASSUME_ROLE"] = "<YOUR_ROLE_ARN>"  # E.g. "arn:aws:..."
# os.environ['SERPAPI_API_KEY'] = "<YOUR_SERP_API_KEY>" # Required for the search tool

from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.llms.bedrock import Bedrock

model_parameter = {"temperature": 0.0, "top_p": .5, "max_tokens_to_sample": 4000}
#boto3_bedrock = boto3.client(service_name='bedrock-runtime', region_name=os.environ["AWS_DEFAULT_REGION"])
boto3_bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')
llm = Bedrock(model_id="anthropic.claude-instant-v1", client=boto3_bedrock, model_kwargs=model_parameter)

def get_item_from_dynamodb(id):
  first_name = 'Augustus'
  import boto3
  import json
  dynamodb = boto3.client("dynamodb", region_name='us-east-1')
  found_customer = dynamodb.get_item(TableName='customer', Key={'id':{'S':id}, 'first_name':{'S':first_name}})
  return found_customer['Item']

react_agent_llm = Bedrock(model_id="anthropic.claude-instant-v1", model_kwargs=model_parameter)
tools = load_tools(["wikipedia"], llm=react_agent_llm)
tools.append(Tool.from_function(
        name="get_item_from_dynamodb",
        func=get_item_from_dynamodb,
        description="Use this when you need to lookup a customer by id."
    ))

react_agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

question = """\n\nHuman: write one sentence summary about the information you know about the customer with an id of 1 and name Alexandrino.

\n\nAssistant: Here is the one sentence summary: """

result = react_agent.run(question)

print(f"{result}")