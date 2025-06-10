
# Voice French Agent

**Responsibility:**  
A real-time multilingual voice assistant that listens to English speech and translates in French. It uses Deepgram for speech-to-text, OpenAI for translation, ElevenLabs for French voice synthesis, and LiveKit for real-time communication with built-in noise cancellation.

## Details

- **Framework:** LiveKit Agents  
- **Tools Used:** Deepgram STT, ElevenLabs TTS, OpenAI LLM, LiveKit Plugins  
- **AI Model:** GPT-4  
- **Date Added:** June 2025  
- **License:** MIT  
- **Original Source:** [Voice French Agent](https://github.com/livekit-examples/python-agents-examples/blob/main/translators/pipeline_translator.py)  


## Install Dependencies

```bash
pip install uv
uv sync
````



## Configure Environment Variables

Copy the example file and add your API keys:

```bash
cp .env.example .env
```

Update `.env` with:

* `LIVEKIT_URL`
* `LIVEKIT_API_KEY`
* `LIVEKIT_API_SECRET`
* `OPENAI_API_KEY`
* `DEEPGRAM_API_KEY`
* `ELEVENLABS_API_KEY`



## Run Agent

Start the agent with voice input/output:

```bash
uv run python main.py console
```



## Agent Capabilities

* **English Speech Recognition** – via Deepgram
* **AI Translation to French** – powered by OpenAI
* **French Voice Output** – using ElevenLabs
* **Noise Cancellation** – with LiveKit plugins


## Example Usage

1. Start the agent.
2. Speak in English.
3. The agent:

   * Transcribes your speech.
   * Translates to French.
   * Responds in natural French voice.

## For a Multi-Agent-System
```python
# Other agents can communicate with French agent like this:
# 1. Send message to french_agent via MCP
# 2. French agent will notify interface agent
# 3. Users can then speak directly with French agent
# 4. All responses are in French via speech
```
## Creator Details

* **Name:** Ahsen Tahir
* **Contact:** [ahsen.t@coralprotocol.org](mailto:ahsen.t@coralprotocol.org)

