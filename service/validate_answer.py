import logging
logging.basicConfig(level=logging.DEBUG)
logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def validate_answer(react_agent, prompt_template):
    try:
        answer = react_agent.run(prompt_template)
    except Exception as e:
        logging.error("Error asking question to chatbot: %s, attempting to parse Chatbot answer", e)

        error = str(e)
        if "Could not parse LLM output: `" not in error:
            return {'answer': 'Please try using a different word or a different question'}
        
        answer = error.split("Could not parse LLM output: `")[1].strip("`").strip(" ")
        logging.info("Found valid answer %s", answer)
        return {'answer': answer}
        
    logging.info("Answer: %s", answer)