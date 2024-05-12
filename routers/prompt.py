from fastapi import APIRouter, HTTPException, Request
from fastapi.params import Depends
from service.init_chatbot import init_chatbot
from models import Request, Response
router = APIRouter(prefix="/prompt")

react_agent = init_chatbot()

@router.post("")
def create_item(request: Request) -> Response:
    prompt_template = f"""
        \n\nHuman: {request.question}

        \n\nAssistant: Here is the one sentence summary:
        """
    result = react_agent.run(prompt_template)
    return Response(result)