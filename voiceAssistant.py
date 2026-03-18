import os
from dotenv import load_dotenv
from datetime import datetime

current_time= datetime.now().strftime("%H: %M %p")

load_dotenv()

AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("API_KEY")

from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig

user_name = "Rushda"
schedule = "Do three projects untill the end of month; Gym with Lisa at 15:00; In your daily diet include protien and take iron tablets; Buy Mom's Pants and Trishna's gift ; weapons is the movie i want to watch;"
prompt = f"You are a helpful assistant. If the user asks about time use this variable: {current_time}. Your interlocutor has the following schedule: {schedule}."
first_message = f"Hello {user_name}, how can I help you today?"

conversation_override = {
    "agent": {
        "prompt": {
            "prompt": prompt,
        },
        "first_message": first_message,
    },
}

config = ConversationConfig(
    agent_id=AGENT_ID,
    user_id="rushda0109",  # required to avoid AttributeError
    extra_body={},
    dynamic_variables={"current_time": current_time },
        conversation_config_override=conversation_override,
)


client = ElevenLabs(api_key=API_KEY)
conversation = Conversation(
    client,
    AGENT_ID,
    config=config,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
)


def print_agent_response(response):
    print(f"Agent: {response}")


def print_interrupted_response(original, corrected):
    print(f"Agent interrupted, truncated response: {corrected}")


def print_user_transcript(transcript):
    print(f"User: {transcript}")
    


conversation = Conversation(
    client,
    AGENT_ID,
    config=config,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
    callback_agent_response=print_agent_response,
    callback_agent_response_correction=print_interrupted_response,
    callback_user_transcript=print_user_transcript,
)
try:
    conversation.start_session()
except KeyboardInterrupt:
    conversation.end_session()