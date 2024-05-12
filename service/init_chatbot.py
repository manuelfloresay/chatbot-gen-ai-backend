import boto3
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.llms.bedrock import Bedrock
from connection_service import get_item_from_dynamodb

def init_chatbot():
    model_parameter = {"temperature": 0.0, "top_p": .5, "max_tokens_to_sample": 4000}
    #boto3_bedrock = boto3.client(service_name='bedrock-runtime', region_name=os.environ["AWS_DEFAULT_REGION"])
    boto3_bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')
    llm = Bedrock(model_id="anthropic.claude-instant-v1", client=boto3_bedrock, model_kwargs=model_parameter)

    react_agent_llm = Bedrock(model_id="anthropic.claude-instant-v1", model_kwargs=model_parameter)
    tools = load_tools(["wikipedia"], llm=react_agent_llm)
    tools.append(Tool.from_function(
            name="get_item_from_dynamodb",
            func=get_item_from_dynamodb,
            description="Use this when you need to lookup a customer by rut."
        ))

    react_agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    return react_agent
