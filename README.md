# Voice French Agent

The Voice French Agent is a real-time multilingual voice assistant that listens to English speech and translates it into French. It uses Deepgram for speech-to-text, OpenAI for translation, ElevenLabs for French voice synthesis, and LiveKit for real-time communication with built-in noise cancellation.

## Responsibility
A real-time multilingual voice assistant that listens to English speech, translates it to French, and responds in natural French voice using advanced AI and speech technologies.

## Details
- **Framework:** LiveKit Agents
- **Tools Used:** Deepgram STT, ElevenLabs TTS, OpenAI LLM, LiveKit Plugins
- **AI Model:** GPT-4
- **Date Added:** June 2025
- **License:** MIT
- **Original Source:** [Voice French Agent](https://github.com/livekit-examples/python-agents-examples/blob/main/translators/pipeline_translator.py)

## Use the Agent

### 1. Clone & Install Dependencies

Ensure that the [Coral Server](https://github.com/Coral-Protocol/coral-server) is running on your system. If you are trying to run Voice French Agent and require an input, you can either create your agent which communicates on the coral server or run and register the [Interface Agent](https://github.com/Coral-Protocol/Coral-Interface-Agent) on the Coral Server.
<details>

```bash
# In a new terminal clone the repository:
git clone https://github.com/Coral-Protocol/Voice-French-Agent.git

# Navigate to the project directory:
cd Voice-French-Agent

# Install `uv`:
pip install uv

# Install dependencies from `pyproject.toml` using `uv`:
uv sync
```

</details>

### 2. Configure Environment Variables
<details>

Copy the example file and add your API keys:

```bash
cp .env.example .env
```

Update `.env` with:
- `LIVEKIT_URL`  ([Get LiveKit Url](https://cloud.livekit.io/))
- `LIVEKIT_API_KEY` ([Get LiveKit API Key](https://cloud.livekit.io/))
- `LIVEKIT_API_SECRET` ([Get LiveKit API Secret](https://cloud.livekit.io/))
- `OPENAI_API_KEY` ([Get OpenAI API Key](https://platform.openai.com/api-keys))
- `DEEPGRAM_API_KEY` ([Get Deepgram API Key](https://deepgram.com/))
- `ELEVENLABS_API_KEY` ([Get ElevenLabs API Key](https://elevenlabs.io/app/settings/api-keys))

</details>

### 3. Run Agent
<details>

Start the agent with voice input/output:

```bash
uv run python main.py console
```

</details>

## Agent System

- **English Speech Recognition:** via Deepgram
- **AI Translation to French:** powered by OpenAI
- **French Voice Output:** using ElevenLabs
- **Noise Cancellation:** with LiveKit plugins

## Usage Examples
<details>

1. Start the agent.
2. Speak in English.
3. The agent:
   - Transcribes your speech.
   - Translates to French.
   - Responds in natural French voice.

**For a Multi-Agent-System:**
```python
# Other agents can communicate with French agent like this:
# 1. Send message to french_agent via MCP
# 2. French agent will notify interface agent
# 3. Users can then speak directly with French agent
# 4. All responses are in French via speech
```

</details>

## Creator Details
- **Name:** Ahsen Tahir
# Medical Office Triage Voice Agent

The Medical Office Triage Voice Agent is an intelligent multi-agent voice system that automates patient routing and support in medical office environments. It uses real-time voice processing to understand patient needs and seamlessly transfers them between specialized departments (Triage, Support, and Billing) while maintaining conversation context. The system leverages Deepgram for speech-to-text, Cartesia for text-to-speech, OpenAI for natural language understanding, and LiveKit for real-time communication with noise cancellation capabilities.

## Responsibility
A real-time voice agent for medical offices that automates patient intake, support, and billing routing. **Note:** The prompts in this agent are not for a multi-agent system; it currently works as a standalone agent, does not require interface agents, but will use Coral tools. It is not continuously using the `wait_for_mention` tool to receive commands from other agents.

## Details
- **Framework:** LiveKit Agents
- **Tools Used:** Deepgram STT, Cartesia TTS, OpenAI LLM, Silero VAD, LiveKit Plugins
- **AI Model:** GPT-4o-mini
- **Date Added:** June 2025
- **License:** MIT
- **Original Source:** [LiveKit Python Agents Examples - Medical Office Triage](https://github.com/livekit-examples/python-agents-examples/tree/main/complex-agents/medical_office_triage)

## Use the Agent

### 1. Clone & Install Dependencies

Ensure that the [Coral Server](https://github.com/Coral-Protocol/coral-server) is running on your system. This agent does not require the Interface Agent and is not designed for multi-agent workflows.
<details>

```bash
# In a new terminal clone the repository:
git clone https://github.com/Coral-Protocol/Medical-Office-Triage-Voice-Agent.git

# Navigate to the project directory:
cd Medical-Office-Triage-Voice-Agent

# Install `uv`:
pip install uv

# Install dependencies from `pyproject.toml` using `uv`:
uv sync
```

</details>

### 2. Configure Environment Variables
<details>

Copy the example file and add your API keys:

```bash
cp .env.example .env
```

Update `.env` with:
- `LIVEKIT_URL` ([Get LiveKit Url](https://cloud.livekit.io/))
- `LIVEKIT_API_KEY` ([Get LiveKit API Key](https://cloud.livekit.io/))
- `LIVEKIT_API_SECRET` ([Get LiveKit API Secret](https://cloud.livekit.io/))
- `OPENAI_API_KEY` ([Get OpenAI API Key](https://platform.openai.com/api-keys))
- `DEEPGRAM_API_KEY` ([Get Deepgram API Key](https://deepgram.com/))
- `CARTESIA_API_KEY` ([Get Cartesia API Key](https://cartesia.ai/))

</details>

### 3. Run Agent
<details>

```bash
uv run triage.py console
```

</details>

## Agent System

- **Triage Agent:** Initial patient intake, determines appropriate department routing
- **Support Agent:** Handles medical services, appointments, and general patient support inquiries
- **Billing Agent:** Manages insurance inquiries, payment questions, and billing support

## Technical Features

- **Multi-Agent Voice System:** Three specialized AI agents working seamlessly together
- **Real-time Voice Processing:** Deepgram speech-to-text, Cartesia text-to-speech, OpenAI language understanding
- **Intelligent Routing:** Automatic patient transfer between departments based on conversation analysis

## Usage Examples
<details>

1. **Start the application using the console command** - The system initializes with all three agents ready
2. **Begin speaking when you hear the system is ready** - You'll be connected to the Triage Agent first
3. **Triage Agent interaction** - The Triage Agent will:
   - Listen to your initial request or concern
   - Ask clarifying questions about your medical office needs
   - Determine whether you need appointment scheduling, medical support, or billing assistance
   - Route you to the appropriate specialist agent based on your needs
4. **Automatic transfer to specialist agents**:
   - **Support Agent** - If you need:
     - Medical appointment scheduling
     - General patient support inquiries
     - Information about medical services
     - Health-related questions and guidance
   - **Billing Agent** - If you need:
     - Insurance verification and claims
     - Payment processing and billing questions
     - Cost estimates for procedures
     - Financial assistance programs
5. **Continue the conversation naturally** - Once transferred:
   - The specialist agent has full context of your previous conversation
   - You can ask follow-up questions specific to that department
   - The agent can transfer you back to Triage or to another specialist if needed
   - All conversation history is preserved throughout transfers

</details>

## Creator Details
- **Name:** Ahsen Tahir
- **Affiliation**: Coral Protocol
- **Contact**: [Discord](https://discord.com/invite/Xjm892dtt3)



