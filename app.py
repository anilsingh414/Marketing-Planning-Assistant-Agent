import streamlit as st
import os
import sys
from dotenv import load_dotenv

try:
    from crew import MarketingCrew
except ImportError:
    st.error("### ❌ CrewAI not found!")
    st.warning(f"You are currently running on Python **{sys.version.split()[0]}**.")
    st.info("Please make sure to run the app using the virtual environment command:")
    st.code(".\\venv\\Scripts\\streamlit run app.py")
    st.stop()

load_dotenv()

# Premium UI Configuration
st.set_page_config(
    page_title="Marketing AI Planner",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Look
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stButton>button {
        background: linear-gradient(45deg, #00c6ff, #0072ff);
        color: white;
        border-radius: 10px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        border: none;
        transition: 0.3s;
        width: 100%;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 15px rgba(0, 198, 255, 0.4);
    }
    .stTextInput>div>div>input {
        background-color: #1e2227;
        color: white;
        border: 1px solid #3e444e;
        border-radius: 8px;
    }
    .agent-box {
        background-color: #1e2227;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #3e444e;
        margin: 10px 0;
        height: 100%;
    }
    h1, h2, h3 {
        color: #00c6ff !important;
    }
    .status-text {
        color: #a0a0a0;
        font-size: 0.9rem;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title("🚀 Marketing Planning Assistant")
    st.markdown("Automate your market research, competitor analysis, and strategic scheduling.")
    st.markdown("---")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("💡 Campaign Objectives")
        goal = st.text_area("What is your primary marketing goal?", 
                           placeholder="e.g., Launch a high-conversion social media campaign for our new eco-friendly water bottle...",
                           height=100)
        
        st.subheader("🏁 Competitors")
        competitors = st.text_input("Who are your main competitors?", 
                                   placeholder="e.g., HydroFlask, Yeti, Klean Kanteen")

    with col2:
        st.subheader("⚙️ Control Center")
        if st.button("Generate Marketing Plan"):
            if not goal or not competitors:
                st.warning("Please fill in both the goal and competitors to proceed.")
            else:
                with st.status("🤖 AI Agents at work...", expanded=True) as status:
                    st.write("🔍 **Researcher** is gathering market data...")
                    # The crew run will happen here
                    try:
                        crew_instance = MarketingCrew(goal, competitors)
                        
                        st.write("📊 **Competitor Analyst** is examining strategies...")
                        st.write("📅 **Scheduler** is building the timeline...")
                        
                        result = crew_instance.run()
                        
                        status.update(label="✅ Strategy Ready!", state="complete", expanded=False)
                        
                        st.session_state['marketing_plan'] = result
                    except Exception as e:
                        st.error(f"Execution Error: {e}")
                        status.update(label="❌ Failed", state="error")

        if 'marketing_plan' in st.session_state:
            st.success("Plan generated successfully!")
            st.download_button(
                label="📥 Download Marketing Plan",
                data=str(st.session_state['marketing_plan']),
                file_name="marketing_plan.md",
                mime="text/markdown"
            )

    if 'marketing_plan' in st.session_state:
        st.markdown("---")
        st.markdown("### 📋 Final Marketing Plan")
        st.markdown(st.session_state['marketing_plan'])

    st.markdown("---")
    st.markdown("### Agent Specialized Roles")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class='agent-box'>
        <h4>🔍 Researcher</h4>
        <p class='status-text'>Uses real-time search to find trends, audience behavior, and industry news.</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class='agent-box'>
        <h4>📊 Analyst</h4>
        <p class='status-text'>Deconstructs competitor ad strategies and identifies market gaps.</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class='agent-box'>
        <h4>📅 Scheduler</h4>
        <p class='status-text'>Integrates insights into a chronological, task-based execution timeline.</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
