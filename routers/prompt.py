from fastapi import APIRouter, HTTPException, Request
from fastapi.params import Depends
from service.init_chatbot import init_chatbot
import logging
logging.basicConfig(level=logging.DEBUG)
logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/prompt")
react_agent = init_chatbot()

@router.get("")
def ask_question(request):
    logging.info("Initializing promt building")
    prompt_template = f"""
        The following is a conversation between a Human and a Chatbot, the Chatbot summarizes the answer to no more than 30 words unless it is told by the Human to summarize it in a different amount of words, if the Chatbot does not know an answer it says that it does not now.
        Current conversation:

        \n\nHuman: {request}

        \n\nChatbot: 
        """
    logging.info("Prompt: %s", prompt_template)
    try:
        result = react_agent.run(prompt_template)
    except Exception as e:
        logging.error("Error asking question to chatbot: %s, attempting to parse Chatbot answer", e)

        error = str(e)
        if "Could not parse LLM output: `" not in error:
            return {'answer': 'Please try using a different word or a different question'}
        
        result = error.split("Could not parse LLM output: `")[1].strip("`")
        logging.info("Found valid answer %s", result)
        return {'answer': result}
        
    logging.info("Answer: %s", result)
    return {'answer': result}