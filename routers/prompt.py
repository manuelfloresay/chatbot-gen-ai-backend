from fastapi import APIRouter, HTTPException, Request
from fastapi.params import Depends
from service.init_chatbot import init_chatbot
from models import Request, Response
import logging
logging.basicConfig(level=logging.DEBUG)

router = APIRouter(prefix="/prompt")
react_agent = init_chatbot()

@router.get("")
def create_item(request):
    logging.info("Initializing promt building")
    prompt_template = f"""
        \n\nHuman: {request}

        \n\nAssistant: Here is the one sentence summary:
        """
    result = react_agent.run(prompt_template)
    return {'answer': result}