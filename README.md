# Voice French Agent

A real-time voice agent that listens to English speech and responds in French using AI-powered translation and text-to-speech technology.

## Features

- **Real-time Speech Recognition**: Powered by Deepgram for accurate English speech-to-text
- **AI Translation**: Uses OpenAI for intelligent English to French translation and conversation
- **French Text-to-Speech**: ElevenLabs integration for natural French voice synthesis
- **Noise Cancellation**: Built-in noise reduction for clearer audio processing

## Installation

### Install uv
```bash
pip install uv
```

### Setup Project
Clone the repository:
```bash
git clone https://github.com/your-username/voice-french-agent.git
cd voice-french-agent
```

Install dependencies using uv:
```bash
uv sync
```

This will create a virtual environment and install all required dependencies including:
- livekit-agents[mcp,openai]~=1.0
- livekit-plugins-noise-cancellation~=0.2
- python-dotenv>=1.1.0

Create a `.env` file with your API keys:
```env
DEEPGRAM_API_KEY=your_deepgram_api_key
OPENAI_API_KEY=your_openai_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
LIVEKIT_URL=your_livekit_url
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
```

## API Keys

Get your API keys from:
- [Deepgram](https://deepgram.com/) - Speech recognition
- [OpenAI](https://openai.com/) - AI translation
- [ElevenLabs](https://elevenlabs.io/) - Text-to-speech
- [LiveKit](https://livekit.io/) - Real-time communication

## Running the Application

### Start the Agent
```bash
uv run python main.py
```

### Terminal Mode
Use this command to run it on terminal:
```bash
uv run python main.py console
```

## How It Works

1. **Listen**: The agent captures your English speech using advanced speech recognition
2. **Understand**: AI processes and translates your English input to French context
3. **Respond**: The agent speaks back in fluent French using natural voice synthesis




