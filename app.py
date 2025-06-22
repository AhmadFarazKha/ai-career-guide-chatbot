import streamlit as st
import os
from dotenv import load_dotenv
from src.core.generator import CareerGuideGenerator
from src.utils.file_operations import create_directories_if_not_exist

def run_streamlit_app():
    load_dotenv()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    directories_to_create = [
        os.path.join(base_dir, "src"),
        os.path.join(base_dir, "src", "core"),
        os.path.join(base_dir, "src", "utils"),
        os.path.join(base_dir, "data")
    ]
    create_directories_if_not_exist(directories_to_create)

    google_api_key = os.getenv("API_KEY")
    if not google_api_key:
        st.error("Error: API_KEY not found in .env file. Please ensure it's in the project root and named 'API_KEY'.")
        st.stop()

    generator = CareerGuideGenerator(api_key=google_api_key)

    # Set page config for a wider layout and initially expanded sidebar
    st.set_page_config(page_title="AI Career Guide Pakistan", layout="centered", initial_sidebar_state="expanded")

    # Custom CSS for a beautiful, darker, and more colorful interface
    st.markdown("""
    <style>
    /* Overall app background */
    .stApp {
        background-color: #1a1a2e; /* Darker blue/purple background */
        color: #e0e0e0; /* Light gray text */
        font-family: 'Inter', sans-serif;
    }

    /* Main content area background (slightly lighter than app background) */
    .main {
        background-color: #2a2a4a; /* Darker blue/purple */
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
        border: 1px solid #4a4a7a; /* Subtle border */
    }

    /* Titles and Headers */
    h1 {
        color: #8be9fd; /* Neon blue for main title */
        text-align: center;
        font-family: 'Inter', sans-serif;
        font-size: 2.8em;
        margin-bottom: 25px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    h2, h3, h4 {
        color: #f1fa8c; /* Yellowish green for subheadings */
        font-family: 'Inter', sans-serif;
        border-bottom: 1px solid #4a4a7a; /* Underline for sections */
        padding-bottom: 5px;
        margin-top: 30px;
    }
    h3 {
        color: #ff79c6; /* Pink for sub-subheadings */
    }

    /* Buttons */
    .stButton>button {
        background-color: #50fa7b; /* Bright green button */
        color: #282a36; /* Dark text on button */
        border-radius: 10px;
        border: none;
        padding: 12px 25px;
        font-size: 1.2em;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.2s ease, box-shadow 0.3s ease;
        box-shadow: 3px 3px 8px rgba(0,0,0,0.3);
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #69ffb0; /* Lighter green on hover */
        transform: translateY(-3px);
        box-shadow: 5px 5px 10px rgba(0,0,0,0.4);
    }

    /* Text Inputs, Text Areas, Selectboxes, Multiselects */
    .stTextInput>div>div>input,
    .stTextArea>div>div>textarea,
    .stSelectbox>div>div>div:first-child, /* Target the input/display area */
    .stMultiSelect>div>div>div:first-child { /* Target the input/display area */
        border-radius: 10px;
        border: 1px solid #6272a4; /* Lighter blue/purple border */
        padding: 10px 15px;
        background-color: #44475a; /* Slightly lighter dark background for inputs */
        color: #f8f8f2; /* Light text color for input */
        box-shadow: inset 1px 1px 5px rgba(0,0,0,0.2);
    }

    /* Placeholder text color */
    .stTextInput>div>div>input::placeholder,
    .stTextArea>div>div>textarea::placeholder {
        color: #a0a0a0;
    }

    /* Alerts (Info, Warning, Error) */
    .stAlert {
        border-radius: 10px;
        border: 1px solid;
        padding: 15px;
        font-weight: bold;
    }
    .stAlert.info { background-color: #6272a4; border-color: #44475a; color: #f8f8f2; } /* Darker info */
    .stAlert.warning { background-color: #ffb86c; border-color: #bd93f9; color: #44475a; } /* Orange warning */
    .stAlert.error { background-color: #ff5555; border-color: #ff79c6; color: #282a36; } /* Red error */
    .stSuccess { background-color: #50fa7b; color: #282a36; border-radius: 10px; padding: 15px; font-weight: bold; }

    /* Radio buttons and checkboxes */
    .stRadio > label, .stCheckbox > label {
        color: #e0e0e0;
        padding: 5px 0;
    }

    /* Style for the generated output markdown (code block style) */
    .stMarkdown pre {
        background-color: #282a36; /* Dracula Theme background */
        color: #f8f8f2; /* Dracula Theme foreground */
        border-radius: 10px;
        padding: 20px;
        white-space: pre-wrap; /* Ensure text wraps */
        word-break: break-word; /* Break long words */
        border: 1px solid #6272a4;
        box-shadow: inset 2px 2px 8px rgba(0,0,0,0.3);
    }
    .stMarkdown code {
        background-color: #44475a; /* Inline code background */
        color: #50fa7b; /* Inline code color */
        border-radius: 4px;
        padding: 2px 4px;
    }

    /* Sidebar styling */
    .css-1d391kg.e1fqkh3o1 { /* Target for the main sidebar div */
        background-color: #282a36; /* Darker sidebar background */
        color: #f8f8f2;
        padding: 20px;
        border-right: 1px solid #4a4a7a;
    }
    .css-1d391kg.e1fqkh3o1 .css-1aum7qf.e1fqkh3o1 { /* Target for sidebar content */
        background-color: #282a36;
        padding: 0;
    }
    .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3, .css-1d391kg h4 { /* Sidebar titles */
        color: #bd93f9; /* Purple for sidebar titles */
        border-bottom: none;
    }
    .css-1d391kg a { /* Sidebar links */
        color: #bd93f9;
    }
    </style>
    """, unsafe_allow_html=True)

    # Sidebar for branding
    st.sidebar.title("Career Guide 🇵🇰")
    st.sidebar.image("https://placehold.co/200x200/50fa7b/282a36?text=AI+Guide+Logo", use_column_width=True) # Updated placeholder logo for dark theme
    st.sidebar.write("Your personalized AI assistant for academic and career planning in Pakistan.")
    st.sidebar.info("💡 Tip: Provide as much detail as possible for accurate guidance! The more you share, the better the advice.")


    st.title("🎓 AI-Powered Career Guide for O/A Level Students (Pakistan)")
    st.write("Unlock your future! Get personalized degree and career recommendations based on your profile.")

    st.markdown("---")

    # Placeholder for general status messages (e.g., app loaded, form submitted, etc.)
    status_message_placeholder = st.empty()
    guidance_placeholder = st.empty() # Placeholder for the generated guidance output

    status_message_placeholder.info("🚀 Welcome! Fill out your profile below to get started.")


    st.subheader("🌟 Tell us about yourself:")

    # Input Form
    with st.form("career_profile_form"):
        st.write("### 📚 Your Academic Profile")
        academic_stream = st.selectbox(
            "Which academic stream are you studying/have studied?",
            ["Pre-Medical", "Pre-Engineering", "Computer Science (ICS)", "Commerce (I.Com/B.Com)", "Arts / Humanities", "Other / Undecided"],
            index=2, # Default to Computer Science (ICS) as a common tech-interest
            help="Select your primary academic track. This helps tailor degree recommendations."
        )
        academic_profile_text = st.text_area(
            "Mention your O-Level / A-Level (or F.Sc/ICS) subjects and indicative grades/performance:",
            "e.g., O-Levels: Math (A), Physics (B), Chemistry (B), English (A*)\nA-Levels: Computer Science (B), Math (C)\nF.Sc Pre-Engineering: 80% overall in relevant subjects",
            height=100,
            help="Be specific about your core subjects (Maths, Sciences etc.) and how well you performed. This is crucial for relevant advice."
        )
        study_level = st.selectbox(
            "Your Current Study Level:",
            ["O-Level / Matric", "A-Level / F.Sc / ICS", "Intermediate (Other)"],
            index=1,
            help="Select your current or most recently completed academic level. This helps determine suitable next steps."
        )

        st.divider() # Visual separator

        st.write("### 💡 Your Interests & Strengths")
        selected_interests = st.multiselect(
            "What are your main areas of interest and passion?",
            ["Technology & IT", "Science & Research", "Business & Finance", "Healthcare & Medicine",
             "Arts & Design", "Law & Politics", "Social Sciences", "Education", "Environmental Studies",
             "Creative Writing", "Problem Solving", "Helping People", "Data & Analytics", "Robotics & AI",
             "Marketing", "Entrepreneurship", "Sports", "Music", "Engineering (General)"],
            default=["Technology & IT", "Problem Solving", "Data & Analytics"],
            help="Choose categories that genuinely excite and motivate you. You can select multiple."
        )
        other_interests = st.text_input(
            "Any other specific interests not listed above?",
            placeholder="e.g., Photography, Blockchain, Psychology, Renewable Energy"
        )
        selected_strengths = st.multiselect(
            "What are your key strengths?",
            ["Analytical Thinking", "Problem-Solving", "Creativity", "Communication", "Leadership",
             "Teamwork", "Adaptability", "Attention to Detail", "Mathematical Skills", "Programming Skills",
             "Research Skills", "Critical Thinking", "Organization", "Public Speaking", "Writing"],
            default=["Analytical Thinking", "Problem-Solving"],
            help="Select skills you are confident in and enjoy utilizing."
        )
        other_strengths = st.text_input(
            "Any other unique strengths you possess?",
            placeholder="e.g., Quick learner, Highly organized, Empathetic, Detail-oriented"
        )

        st.divider() # Visual separator

        st.write("### 🎯 Your Career Ambitions")
        selected_career_goals = st.multiselect(
            "Which broad career fields are you considering?",
            ["IT & Software Development", "Healthcare & Pharmaceuticals", "Business Management & Consulting",
             "Finance & Banking", "Engineering (Civil, Electrical, Mechanical, etc.)", "Law & Legal Services",
             "Arts & Media", "Education & Academia", "Public Sector & Civil Services",
             "Research & Development", "Data Science & AI", "Entrepreneurship", "Marketing & Sales",
             "Human Resources", "Supply Chain & Logistics", "Architecture & Urban Planning"],
            default=["IT & Software Development", "Data Science & AI"],
            help="Choose fields that align with your long-term aspirations. Multiple selections are allowed."
        )
        other_career_goals = st.text_input(
            "Any specific career roles or other goals?",
            placeholder="e.g., Cybersecurity expert, Digital Marketer, Urban Planner, Clinical Psychologist"
        )
        preferred_work_environment = st.selectbox(
            "What type of work environment do you prefer?",
            ["Office-based (Traditional)", "Fieldwork/Outdoor", "Lab/Research-focused", "Remote/Flexible",
             "Creative Studio/Collaborative", "Dynamic & Fast-paced", "Structured & Predictable", "Any"],
            index=0,
            help="Consider the daily setting you'd thrive in. (e.g., quiet office vs. dynamic startup)."
        )
        st.markdown("---") # End of form visual separator

        # Buttons in the form
        col_submit, col_reset = st.columns([1, 1])
        with col_submit:
            submitted = st.form_submit_button("🚀 Get My Personalized Career Guidance!")
        with col_reset:
            reset_button = st.form_submit_button("🔄 Reset Form", help="Clear all inputs and start fresh.")

    if submitted:
        status_message_placeholder.empty() # Clear initial welcome message
        guidance_placeholder.empty() # Clear previous guidance

        # Combine all input into a single profile string for the AI
        user_profile_text = (
            f"Academic Stream: {academic_stream}\n"
            f"Subjects & Grades: {academic_profile_text}\n"
            f"Interests: {', '.join(selected_interests)}{', ' + other_interests if other_interests else ''}\n"
            f"Strengths: {', '.join(selected_strengths)}{', ' + other_strengths if other_strengths else ''}\n"
            f"Career Goals: {', '.join(selected_career_goals)}{', ' + other_career_goals if other_career_goals else ''}\n"
            f"Preferred Work Environment: {preferred_work_environment}"
        )

        if not academic_profile_text or not selected_interests or not selected_strengths:
            status_message_placeholder.warning("⚠️ Please fill in your academic subjects, primary interests, and key strengths for accurate guidance.")
        else:
            with st.spinner("🧠 Analyzing your profile and generating guidance... This might take a moment."):
                try:
                    guidance_output = generator.get_career_guidance(user_profile_text, study_level)
                    guidance_placeholder.subheader("✨ Your Personalized Career Guidance:")
                    guidance_placeholder.markdown(f"```markdown\n{guidance_output}\n```")
                    status_message_placeholder.success("✅ Guidance generated successfully! Scroll down to see your recommendations.")
                except Exception as e:
                    status_message_placeholder.error(f"❌ Failed to generate guidance: {e}")
                    status_message_placeholder.info("💡 Please ensure your Google API key is valid and you have an active internet connection. If the issue persists, try again later or check your API key.")
    elif reset_button:
        # To truly reset the form, Streamlit requires rerunning the script.
        # This is a common pattern for "hard" resets in Streamlit apps.
        st.session_state["reset_form"] = True
        st.experimental_rerun()

    # Handle the "hard" reset logic after rerunning
    if "reset_form" in st.session_state and st.session_state["reset_form"]:
        st.session_state.clear() # Clear all session state variables
        status_message_placeholder.info("🔄 Form has been reset. Please fill in your details again.")
        st.session_state["reset_form"] = False # Reset the flag

    st.markdown("---")
    st.markdown("Developed with ❤️ using Python, Streamlit, and Google Gemini API for Pakistani youth. [Link to GitHub Repo (Placeholder)]") # Remember to add your GitHub link here
    st.markdown("Disclaimer: This AI provides guidance based on general information and publicly available data. Always verify details with official university/career counseling sources and consider seeking professional advice.")

if __name__ == "__main__":
    run_streamlit_app()
