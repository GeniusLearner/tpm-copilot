"""
TPM Co-Pilot - Productivity Platform for Technical Program Managers
Streamlit Web Application
"""

import streamlit as st
from core import DocumentGenerator
import os

# Page configuration
st.set_page_config(
    page_title="TPM Co-Pilot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 0;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        margin-top: 0;
    }
    .tool-card {
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #ddd;
        margin: 1rem 0;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .stButton>button {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)


def check_api_key():
    """Check if API key is configured"""
    if not os.getenv("ANTHROPIC_API_KEY"):
        st.error("⚠️ ANTHROPIC_API_KEY not found!")
        st.info("""
        **Setup Instructions:**
        1. Copy `.env.example` to `.env`
        2. Get your API key from: https://console.anthropic.com/
        3. Add it to `.env`: `ANTHROPIC_API_KEY=your_key_here`
        4. Restart the app
        """)
        st.stop()


def initialize_session_state():
    """Initialize session state variables"""
    if 'generator' not in st.session_state:
        try:
            st.session_state.generator = DocumentGenerator()
            st.session_state.api_ready = True
        except ValueError as e:
            st.session_state.api_ready = False
            st.error(str(e))
            st.stop()

    if 'generation_count' not in st.session_state:
        st.session_state.generation_count = {
            'agenda': 0,
            'summary': 0,
            'status': 0,
            'risk': 0,
            'charter': 0
        }


def render_sidebar():
    """Render the sidebar with tool selection and stats"""
    with st.sidebar:
        st.markdown("## ⚡TPM Co-Pilot")
        st.markdown("*Productivity Platform for Technical Program Managers*")
        st.markdown("---")

        # Tool selection
        tool = st.selectbox(
            "Select Tool",
            [
                "🏠 Home",
                "📋 Meeting Agenda Generator",
                "💬 Thread Summarizer",
                "📊 Status Report Builder",
                "⚠️ Risk Analyzer",
                "📄 Project Charter Creator"
            ]
        )

        st.markdown("---")

        # Usage statistics
        st.markdown("### 📈 Usage Stats")
        total_generations = sum(st.session_state.generation_count.values())
        st.metric("Total Generations", total_generations)

        with st.expander("See breakdown"):
            for tool_name, count in st.session_state.generation_count.items():
                st.text(f"{tool_name.title()}: {count}")

        st.markdown("---")

        # About section
        st.markdown("### About")
        st.markdown("""
        Built to deeply understand TPM workflows by solving real problems TPMs face daily.

        **Features:**
        - Meeting agendas
        - Thread summaries
        - Status reports
        - Risk analysis
        - Project charters

        **Tech Stack:**
        - Python & Streamlit
        - Modern NLP Models
        - Cloud Infrastructure
        """)

        st.markdown("---")
        st.markdown("**Built by:** Sanchit Khurana")
        st.markdown("[GitHub](https://github.com/GeniusLearner/tpm-copilot)")

    return tool


def render_home():
    """Render the home page"""
    st.markdown('<p class="main-header">⚡TPM Co-Pilot</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">AI-Powered Assistant for Technical Program Managers</p>', unsafe_allow_html=True)

    st.markdown("---")

    # Problem statement
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("## 🎯 The Problem")
        st.markdown("""
        Technical Program Managers spend significant time on repetitive documentation tasks:
        - ✍️ Writing meeting agendas
        - 📧 Summarizing lengthy email/Slack threads
        - 📊 Creating executive status reports
        - ⚠️ Identifying and documenting project risks
        - 📋 Drafting project charters
        """)

    with col2:
        st.markdown("## 💡 The Solution")
        st.info("""
        **TPM Co-Pilot** automates these tasks using AI.

        From hours to minutes.
        """)

    st.markdown("---")

    # Tools overview
    st.markdown("## 🛠️ Available Tools")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📋 Meeting Agenda Generator")
        st.markdown("""
        **Input:** Meeting context and objectives

        **Output:** Structured agenda with:
        - Clear objectives
        - Timed discussion points
        - Pre-work items
        - Success criteria
        """)

        st.markdown("### 💬 Thread Summarizer")
        st.markdown("""
        **Input:** Slack/email conversation thread

        **Output:** Concise summary with:
        - TLDR
        - Key decisions
        - Action items with owners
        - Open questions
        """)

        st.markdown("### 📊 Status Report Builder")
        st.markdown("""
        **Input:** Weekly project updates

        **Output:** Executive-ready report with:
        - Project health status
        - Key accomplishments
        - Upcoming milestones
        - Risks and blockers
        """)

    with col2:
        st.markdown("### ⚠️ Risk Analyzer")
        st.markdown("""
        **Input:** Project description

        **Output:** Comprehensive risk analysis:
        - Technical risks
        - Schedule risks
        - Resource risks
        - Mitigation strategies
        """)

        st.markdown("### 📄 Project Charter Creator")
        st.markdown("""
        **Input:** High-level project information

        **Output:** Complete project charter with:
        - Objectives and scope
        - Stakeholders
        - Timeline and milestones
        - Success metrics
        """)

    st.markdown("---")

    # Getting started
    st.markdown("## 🚀 Getting Started")
    st.info("""
    1. Select a tool from the sidebar
    2. Provide the required input
    3. Click generate
    4. Review and download the output
    5. Iterate if needed

    **Pro tip:** Start with the Meeting Agenda Generator for your next team sync!
    """)


def render_agenda_generator():
    """Render the meeting agenda generator tool"""
    st.markdown("## 📋 Meeting Agenda Generator")
    st.markdown("Create structured, actionable meeting agendas in seconds.")

    st.markdown("---")

    # Example templates
    with st.expander("📝 See example templates"):
        template_choice = st.selectbox(
            "Load a template",
            [
                "Custom",
                "Sprint Planning",
                "Quarterly Business Review",
                "Technical Design Review",
                "Project Kickoff",
                "Incident Post-Mortem"
            ]
        )

        templates = {
            "Sprint Planning": "Sprint planning meeting for Q2 Platform Migration project. Team of 8 engineers + 1 designer. Need to finalize API migration roadmap, prioritize technical debt, and resolve database scaling approach. Attendees: Engineering leads (Alice, Bob), Product Manager (Carol), Designer (David), and TPM (me).",

            "Quarterly Business Review": "Q4 QBR for the Customer Authentication Platform. Review progress against OKRs, discuss 2024 roadmap priorities, address cross-team dependencies with Payments team. Attendees: VP Engineering, Engineering Director, Product Director, 3 team leads, TPMs. Need to secure buy-in for Q1 2024 headcount.",

            "Technical Design Review": "Design review for real-time notification service architecture. Team proposing WebSocket-based solution vs. long-polling. Need to evaluate scalability to 10M users, cost implications, and operational complexity. Attendees: Senior Engineers, Staff Engineer, SRE lead, TPM.",

            "Project Kickoff": "Kickoff for Mobile App Redesign project. 6-month initiative to modernize UI/UX across iOS and Android. Need to align on goals, define success metrics, establish working norms, and identify risks early. Attendees: Design lead, iOS/Android leads, PM, QA, TPM, Marketing stakeholder.",

            "Incident Post-Mortem": "Post-mortem for December 15th production outage (2.5 hours downtime). Review timeline of events, root cause analysis, impact on customers, and preventive measures. Attendees: Incident Commander, SRE team, Backend engineers, TPM, Engineering Manager. Goal: Blameless learning and action items."
        }

        if template_choice != "Custom":
            meeting_context = st.text_area(
                "Meeting Context",
                value=templates[template_choice],
                height=150,
                help="Edit the template or use as-is"
            )
        else:
            meeting_context = st.text_area(
                "Meeting Context",
                placeholder="Describe your meeting: purpose, attendees, key topics, and desired outcomes...",
                height=150,
                help="Provide details about the meeting, who's attending, what you need to discuss, and what success looks like."
            )

    col1, col2 = st.columns([1, 4])
    with col1:
        generate_btn = st.button("🚀 Generate Agenda", type="primary", use_container_width=True)

    if generate_btn and meeting_context:
        with st.spinner("⚡ Generating agenda... (takes ~10 seconds)"):
            result = st.session_state.generator.generate_agenda(meeting_context)
            st.session_state.generation_count['agenda'] += 1

        st.markdown("---")
        st.markdown("### ✅ Generated Agenda")
        st.markdown(result)

        # Download button
        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            st.download_button(
                "📥 Download (.md)",
                result,
                file_name="meeting_agenda.md",
                mime="text/markdown",
                use_container_width=True
            )
        with col2:
            st.download_button(
                "📥 Download (.txt)",
                result,
                file_name="meeting_agenda.txt",
                mime="text/plain",
                use_container_width=True
            )

    elif generate_btn:
        st.warning("⚠️ Please provide meeting context before generating.")


def render_thread_summarizer():
    """Render the thread summarizer tool"""
    st.markdown("## 💬 Thread Summarizer")
    st.markdown("Extract key decisions and action items from lengthy discussions.")

    st.markdown("---")

    # Example threads
    with st.expander("📝 See example threads"):
        example_thread = st.selectbox(
            "Load an example",
            ["Custom", "Database Decision", "API Design Discussion", "Timeline Negotiation"]
        )

        examples = {
            "Database Decision": """Alice (10:23 AM): Team, we need to finalize the database solution for the new analytics feature. Current proposal is PostgreSQL.

Bob (10:25 AM): I think PostgreSQL makes sense given our existing stack. We already have expertise.

Carol (10:27 AM): What about MongoDB? We discussed document storage benefits last quarter for this use case.

Bob (10:30 AM): True, MongoDB could work. But we'd need to onboard the team on MongoDB best practices. That's 2-3 weeks of ramp-up time.

Alice (10:32 AM): Timeline is tight - we need to ship by end of Q1. Can we afford 3 weeks of learning curve?

David (10:35 AM): Also, our DevOps pipeline is optimized for Postgres. Adding Mongo means new backup strategies, monitoring dashboards, etc.

Carol (10:38 AM): Fair points. I withdraw the Mongo suggestion. Let's go with Postgres.

Alice (10:40 AM): Great. Decision made: PostgreSQL it is. Carol, can you document this decision in the design doc with the rationale?

Carol (10:41 AM): Yes, I'll update the design doc by end of day Friday.

Bob (10:42 AM): I'll start the schema design. Will share draft by Wednesday for feedback.

Alice (10:43 AM): Perfect. Thanks everyone!""",

            "API Design Discussion": """Sarah (2:15 PM): Looking at the API design for the new booking endpoint. Should we go with REST or GraphQL?

Mike (2:18 PM): GraphQL would give clients more flexibility. They can request exactly what they need.

Sarah (2:20 PM): True, but we don't have GraphQL expertise in-house. Learning curve could be steep.

Jake (2:23 PM): Also, our mobile team is already using REST for all other endpoints. Mixing paradigms might cause confusion.

Mike (2:25 PM): Valid concern. What about REST with field filtering? Like `/bookings?fields=id,date,status`

Sarah (2:27 PM): That could work. Gives us some of the GraphQL benefits without the complexity.

Linda (2:30 PM): +1 for REST with filtering. Also easier to cache and monitor than GraphQL.

Mike (2:32 PM): Okay, I'm convinced. REST with field filtering it is.

Sarah (2:33 PM): Great! Mike, can you update the API spec by Monday? Linda, can you review it by Wednesday?

Mike (2:34 PM): Will do.

Linda (2:35 PM): Yep, I'll review Wednesday morning.""",

            "Timeline Negotiation": """PM (9:00 AM): Morning team. Leadership is pushing for the feature to launch 2 weeks earlier - March 1st instead of March 15th. Thoughts?

DevLead (9:05 AM): That's aggressive. We'd have to cut scope. What's driving the urgency?

PM (9:07 AM): Major customer committed to a demo on March 5th. Sales promised the feature would be ready.

TPM (9:10 AM): Let me break down what we could realistically deliver by March 1st. Core booking flow: yes. Admin dashboard: risky. Analytics: definitely not.

DevLead (9:13 AM): Agreed with TPM's assessment. Analytics alone is 2 weeks of work.

Designer (9:15 AM): Also, if we cut analytics, we should cut the related UI components too. No point designing for features we won't ship.

PM (9:18 AM): Can we do a phased launch? Core booking by March 1st, analytics in March 15th release?

TPM (9:20 AM): That works, but we need to be clear with the customer about what's in phase 1 vs phase 2.

PM (9:22 AM): I'll talk to Sales and set proper expectations. If customer is okay with phased approach, we'll proceed.

DevLead (9:24 AM): Sounds good. But March 1st is still tight. We'd need to lock scope by end of this week - no more changes.

PM (9:26 AM): Agreed. I'll get confirmation from customer by Thursday. If approved, scope freeze starting Friday.

TPM (9:28 AM): I'll update the project timeline and send new milestones by EOD today."""
        }

        if example_thread != "Custom":
            thread_text = st.text_area(
                "Paste Thread (Slack/Email/Teams)",
                value=examples[example_thread],
                height=300,
                help="Edit the example or use as-is"
            )
        else:
            thread_text = st.text_area(
                "Paste Thread (Slack/Email/Teams)",
                placeholder="Paste your conversation thread here...",
                height=300,
                help="Copy and paste the entire conversation from Slack, email, or any other tool."
            )

    col1, col2 = st.columns([1, 4])
    with col1:
        summarize_btn = st.button("🚀 Summarize", type="primary", use_container_width=True)

    if summarize_btn and thread_text:
        with st.spinner("⚡Analyzing thread... (takes ~10 seconds)"):
            result = st.session_state.generator.summarize_thread(thread_text)
            st.session_state.generation_count['summary'] += 1

        st.markdown("---")
        st.markdown("### ✅ Thread Summary")
        st.markdown(result)

        # Download button
        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            st.download_button(
                "📥 Download (.md)",
                result,
                file_name="thread_summary.md",
                mime="text/markdown",
                use_container_width=True
            )
        with col2:
            st.download_button(
                "📥 Download (.txt)",
                result,
                file_name="thread_summary.txt",
                mime="text/plain",
                use_container_width=True
            )

    elif summarize_btn:
        st.warning("⚠️ Please paste a thread before summarizing.")


def render_status_report():
    """Render the status report builder tool"""
    st.markdown("## 📊 Status Report Builder")
    st.markdown("Create executive-ready status reports in seconds.")

    st.markdown("---")

    col1, col2 = st.columns([2, 1])

    with col1:
        project_name = st.text_input(
            "Project Name (Optional)",
            placeholder="E.g., Platform Migration Q1 2024",
            help="Optional: Add a project name for the report header"
        )

    with col2:
        st.markdown("")  # Spacing

    updates = st.text_area(
        "Weekly Updates",
        placeholder="""E.g.,
- Completed API migration phase 1 (authentication endpoints)
- Started user testing with 50 beta users
- Database optimization improved query performance by 40%
- Blocker: Waiting on design review for dashboard redesign
- Risk: Third-party payment gateway integration delayed by 1 week
- Team morale is good, velocity on track""",
        height=250,
        help="Provide raw updates, accomplishments, blockers, risks - the AI will structure it into an executive report."
    )

    col1, col2 = st.columns([1, 4])
    with col1:
        generate_btn = st.button("🚀 Generate Report", type="primary", use_container_width=True)

    if generate_btn and updates:
        with st.spinner("⚡Creating status report... (takes ~15 seconds)"):
            result = st.session_state.generator.generate_status_report(updates, project_name or None)
            st.session_state.generation_count['status'] += 1

        st.markdown("---")
        st.markdown("### ✅ Status Report")
        st.markdown(result)

        # Download button
        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            st.download_button(
                "📥 Download (.md)",
                result,
                file_name="status_report.md",
                mime="text/markdown",
                use_container_width=True
            )
        with col2:
            st.download_button(
                "📥 Download (.txt)",
                result,
                file_name="status_report.txt",
                mime="text/plain",
                use_container_width=True
            )

    elif generate_btn:
        st.warning("⚠️ Please provide weekly updates before generating.")


def render_risk_analyzer():
    """Render the risk analyzer tool"""
    st.markdown("## ⚠️ Risk Analyzer")
    st.markdown("Identify potential risks and mitigation strategies proactively.")

    st.markdown("---")

    project_desc = st.text_area(
        "Project Description",
        placeholder="""E.g.,
Migrating 500K users from legacy authentication system to new OAuth2 implementation.
Timeline: 3 months (Jan - March 2024)
Team: 5 backend engineers, 1 SRE, 1 QA
Integration with 12 downstream services (mobile apps, web app, admin portal, 3rd party integrations)
Must maintain 99.9% uptime during migration
Legacy system is 5 years old with minimal documentation""",
        height=200,
        help="Describe your project: scope, timeline, team size, dependencies, constraints."
    )

    col1, col2 = st.columns([1, 4])
    with col1:
        analyze_btn = st.button("🚀 Analyze Risks", type="primary", use_container_width=True)

    if analyze_btn and project_desc:
        with st.spinner("⚡Analyzing risks... (takes ~20 seconds)"):
            result = st.session_state.generator.analyze_risks(project_desc)
            st.session_state.generation_count['risk'] += 1

        st.markdown("---")
        st.markdown("### ✅ Risk Analysis")
        st.markdown(result)

        # Download button
        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            st.download_button(
                "📥 Download (.md)",
                result,
                file_name="risk_analysis.md",
                mime="text/markdown",
                use_container_width=True
            )
        with col2:
            st.download_button(
                "📥 Download (.txt)",
                result,
                file_name="risk_analysis.txt",
                mime="text/plain",
                use_container_width=True
            )

    elif analyze_btn:
        st.warning("⚠️ Please provide a project description before analyzing.")


def render_charter_creator():
    """Render the project charter creator tool"""
    st.markdown("## 📄 Project Charter Creator")
    st.markdown("Create comprehensive project charters that align stakeholders.")

    st.markdown("---")

    project_info = st.text_area(
        "Project Information",
        placeholder="""E.g.,
Build a real-time notification system for our mobile and web apps.
Business goal: Increase user engagement by 25% through timely notifications.
Target: 10M users, support 50K notifications per second.
Timeline: 6 months (Q1-Q2 2024)
Team: 2 backend engineers, 1 mobile engineer, 1 web engineer, 1 QA, 1 TPM
Tech stack: WebSockets, Redis, PostgreSQL, AWS infrastructure
Key stakeholders: VP Product, Engineering Director, Mobile team lead, Growth PM""",
        height=250,
        help="Provide high-level project information: goals, scope, timeline, team, stakeholders."
    )

    col1, col2 = st.columns([1, 4])
    with col1:
        create_btn = st.button("🚀 Create Charter", type="primary", use_container_width=True)

    if create_btn and project_info:
        with st.spinner("⚡Creating project charter... (takes ~20 seconds)"):
            result = st.session_state.generator.create_project_charter(project_info)
            st.session_state.generation_count['charter'] += 1

        st.markdown("---")
        st.markdown("### ✅ Project Charter")
        st.markdown(result)

        # Download button
        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            st.download_button(
                "📥 Download (.md)",
                result,
                file_name="project_charter.md",
                mime="text/markdown",
                use_container_width=True
            )
        with col2:
            st.download_button(
                "📥 Download (.txt)",
                result,
                file_name="project_charter.txt",
                mime="text/plain",
                use_container_width=True
            )

    elif create_btn:
        st.warning("⚠️ Please provide project information before creating charter.")


def main():
    """Main application"""
    # Check API key
    check_api_key()

    # Initialize session state
    initialize_session_state()

    # Render sidebar and get selected tool
    tool = render_sidebar()

    # Render the appropriate tool
    if tool == "🏠 Home":
        render_home()
    elif tool == "📋 Meeting Agenda Generator":
        render_agenda_generator()
    elif tool == "💬 Thread Summarizer":
        render_thread_summarizer()
    elif tool == "📊 Status Report Builder":
        render_status_report()
    elif tool == "⚠️ Risk Analyzer":
        render_risk_analyzer()
    elif tool == "📄 Project Charter Creator":
        render_charter_creator()


if __name__ == "__main__":
    main()
