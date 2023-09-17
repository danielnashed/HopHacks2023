import os
import traceback
import openai
from openai.error import OpenAIError
from dotenv import load_dotenv
load_dotenv()

# Read environment variables
openai_model = os.getenv('OPENAI_API_MODEL')
openai.api_key = os.getenv('OPENAI_API_KEY')
print(openai_model)
async def generate_response(messages):
    try:
        async for chunk in await openai.ChatCompletion.acreate(
                model=openai_model,
                temperature=0.9,
                top_p=0.9,
                messages=messages,
                max_tokens=8000,
                stream=True
        ):
            content = chunk['choices'][0]['delta'].get('content', '')
            if content:
                yield content
    except OpenAIError as e:
        traceback.print_exc()
        yield f"EXCEPTION {str(e)}"
    except Exception as e:
        yield f"EXCEPTION {str(e)}"

async def run_conversation(messages, message_placeholder):
    full_response = ""
    message_placeholder.markdown("Thinking...")
    chunks = generate_response(messages)
    chunk = await anext(chunks, "END OF CHAT")
    while chunk != "END OF CHAT":
        if chunk.startswith("EXCEPTION"):
            full_response = ":red[We are having trouble generating advice.  Please wait a minute and try again.]"
            break
        full_response = full_response + chunk
        message_placeholder.markdown(full_response + "▌")
        chunk = await anext(chunks, "END OF CHAT")
    message_placeholder.markdown(full_response)
    messages.append({"role": "assistant", "content": full_response})
    return messages