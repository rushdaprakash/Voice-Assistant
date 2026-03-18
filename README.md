 Voice AI Assistant using ElevenLabs

An intelligent, real-time voice-enabled AI assistant built using ElevenLabs Conversational AI.
This project demonstrates how to design a **context-aware, personalized conversational agent** with dynamic inputs, custom prompts, and callback-driven interaction.

 Overview
This system enables natural voice-based interaction with an AI assistant that adapts its responses based on **real-time data (current time)** and **user-specific context (personal schedule)**.

It showcases key concepts in:

* Agentic AI systems
* Prompt engineering
* Real-time conversational interfaces
* API integration and event-driven programming
 Features

Real-Time Voice Interaction
  Engage in seamless conversations using ElevenLabs audio interface

Dynamic Time Awareness
  AI responds intelligently using live system time

Personalized Context Injection
  Assistant behavior adapts based on user schedule and preferences

Prompt Engineering
  Custom-designed prompts for controlled and meaningful responses

Callback-Based Architecture
  Handles:
  * Agent responses
  * User transcripts
  * Interrupted responses

Tech Stack
* **Python**
* **ElevenLabs Conversational AI**
* **dotenv** (environment variable management)
* **Real-time audio interface**

System Workflow

1. Load environment variables securely
2. Generate dynamic variables (e.g., current time)
3. Inject personalized context (user schedule) into prompt
4. Configure AI agent using `ConversationConfig`
5. Start real-time voice session
6. Process interactions using callback functions



Setup & Installation
Clone the repository

```bash
git clone https://github.com/rushdaprakash/Voice-Assistant.git
cd Voice-Assistant
```
Install dependencies

```bash
pip install -r requirements.txt
```
Create `.env` file

```
AGENT_ID=your_agent_id
API_KEY=your_api_key
```

Run the application

```bash
python voiceAssistant.py

 Use Cases
* Personal AI assistant
* Smart scheduling assistant
* Voice-enabled productivity tools
* Conversational AI experimentation

Security Note

API keys and sensitive credentials are stored in a `.env` file and are **excluded from version control** using `.gitignore`.
