import streamlit as st
import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

# --- 1. PAGE CONFIG (Must be at the very top) ---
st.set_page_config(page_title="MindCompanion", page_icon="💙")
st.title("💙 MindCompanion")
st.write("🔄 System Starting...") # Visual proof the app is loading

# --- 2. SETUP ---
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("❌ API Key is missing. Check .env file.")
    st.stop()

genai.configure(api_key=api_key)

# --- 3. CONNECT TO YOUR SPECIFIC MODELS ---
# We use the EXACT list you provided.
my_models = [
    "gemini-2.5-flash",      # You said you have this
    "gemini-2.0-flash-exp",  # This is very stable
    "gemini-2.0-flash",
    "gemini-2.5-pro"
]

if "chat" not in st.session_state:
    active_model = None
    st.write("🔌 Connecting to AI...")
    
    for name in my_models:
        try:
            # Try to connect
            model = genai.GenerativeModel(name)
            model.start_chat() # Test connection
            active_model = model
            st.success(f"✅ Connected to: {name}")
            break # Stop looking, we found one!
        except Exception as e:
            print(f"Skipping {name}...") # Print to terminal, not web
            
    if not active_model:
        st.error("❌ Critical Error: None of your models (2.5 or 2.0) could connect.")
        st.stop()
        
    st.session_state.chat = active_model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 4. CHAT LOGIC ---
system_prompt = """
You are MindCompanion.
RULES:
1. Output ONLY valid JSON.
2. NO Markdown formatting.
3. Format: {"message": "Short text", "mood": "OneWord", "score": 1-10}
"""

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("How are you feeling?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        # Send Message
        if len(st.session_state.chat.history) == 0:
            response = st.session_state.chat.send_message(system_prompt + f"\nUser: {prompt}")
        else:
            response = st.session_state.chat.send_message(prompt)

        # Clean Response
        text = response.text.strip()
        if "```" in text:
            text = text.replace("```json", "").replace("```", "")
        
        start = text.find('{')
        end = text.rfind('}') + 1
        
        bot_msg = text
        if start != -1 and end != -1:
            try:
                data = json.loads(text[start:end])
                bot_msg = data['message']
                
                # Sidebar Updates
                st.sidebar.header("Analysis")
                st.sidebar.metric("Mood", data.get('mood', 'Neutral'))
                st.sidebar.progress(data.get('score', 5)/10, text="Stress Level")
            except:
                pass

        # Show Response
        with st.chat_message("assistant"):
            st.markdown(bot_msg)
        st.session_state.messages.append({"role": "assistant", "content": bot_msg})

    except Exception as e:
        st.error(f"Error: {e}")