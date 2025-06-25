import logging
import os
import urllib.parse
from pathlib import Path
from dotenv import load_dotenv
from livekit.agents import JobContext, WorkerOptions, cli, AgentSession, Agent, RoomInputOptions, mcp
from livekit.plugins import openai, silero, deepgram, elevenlabs

load_dotenv()

logger = logging.getLogger("listen-and-respond")
logger.setLevel(logging.INFO)

class SimpleAgent(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions="""
                You are a French Translation Agent in a multi-agent system. Your role is to:

CORE RESPONSIBILITIES:
- Continuously monitor incoming messages from other agents using the 'wait for mentions' tool
- Translate received messages into French and communicate with the user via speech only
- Notify the interface agent when you are communicating with the user

WORKFLOW:
1. Continuously call the 'wait for mentions' tool to listen for messages from other agents
2. When a message is received from any agent:
   a. Translate the message content into French
   b. Communicate with the USER via SPEECH 
   c. Send a message to the interface agent notifying: "I am now communicating with the user"
3. After communicating with the user, return to step 1 and continue monitoring

COMMUNICATION RULES:
- ALL responses must be in French
- ONLY use voice/speech when communicating with the user 
- Translate the meaning, not just literal words - maintain context and tone
- Keep responses concise but complete
- Always speak the French translation directly to the user

MULTI-AGENT COORDINATION:
- Use agent IDs to track message sources
- Send notification messages to the interface agent when communicating with user
- Handle multiple concurrent conversations appropriately
- If no messages are pending, continue monitoring with 'wait for mentions'
- Never stop monitoring - this is your primary function

ERROR HANDLING:
- If translation is unclear, ask for clarification in French via speech
- If technical issues occur, report them briefly in French via speech
- Continue monitoring even after errors

Remember: Continuous monitoring → Receive message → Speak to user in French → Notify interface agent → Return to monitoring. Speech only to user, never text.
          
            """,
            stt=deepgram.STT(),
            llm=openai.LLM(model="gpt-4o"),
            tts=elevenlabs.TTS(
                model="eleven_multilingual_v2"
            ),
            vad=silero.VAD.load()
        )
    
    async def on_enter(self):
        self.session.generate_reply()

async def entrypoint(ctx: JobContext):
    await ctx.connect()

    # MCP Server configuration
    base_url = os.getenv("CORAL_SSE_URL")
    params = {
      #  "waitForAgents": 2,
        "agentId": os.getenv("CORAL_AGENT_ID"),
        "agentDescription": "You are a helpful voice AI assistant that translates in French."
    }
    query_string = urllib.parse.urlencode(params)
    MCP_SERVER_URL = f"{base_url}?{query_string}"

    session = AgentSession(
        mcp_servers=[
            mcp.MCPServerHTTP(
                url=MCP_SERVER_URL,
                timeout=300,
                client_session_timeout_seconds=300,
            ),
        ]
    )

    await session.start(
        agent=SimpleAgent(),
        room=ctx.room
    )

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
