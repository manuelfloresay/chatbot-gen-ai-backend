from fastapi import APIRouter, HTTPException, Request
from fastapi.params import Depends
from service.init_chatbot import init_chatbot
import logging
logging.basicConfig(level=logging.DEBUG)

router = APIRouter(prefix="/prompt")
react_agent = init_chatbot()

@router.get("")
def ask_question(request):
    logging.info("Initializing promt building")
    prompt_template = f"""
        \n\nHuman: {request}

        \n\nAssistant: Here is the one sentence summary:
        """
    logging.info("Prompt: %s", prompt_template)
    result = react_agent.run(prompt_template)
    logging.info("Answer: %s", result)
    return {'answer': result}